#!/usr/bin/env python
import rospy
import actionlib
import math
from control_msgs.msg import FollowJointTrajectoryAction
from control_msgs.msg import FollowJointTrajectoryFeedback
from control_msgs.msg import FollowJointTrajectoryResult
from control_msgs.msg import FollowJointTrajectoryGoal
from grp6_proj.msg import XYArray
from grp6_proj.msg import ZArray
from trajectory_msgs.msg import JointTrajectoryPoint
from trajectory_msgs.msg import JointTrajectory
from utils import Trajectory

class SequenceNode:
	def __init__(self, node_name):
		self.node_name = node_name
		self.joint_names = rospy.get_param("parameters/joint_names")
		self.client = actionlib.SimpleActionClient("action_server", FollowJointTrajectoryAction)
		rospy.init_node(self.node_name)
		self.d1 = rospy.get_param("/parameters/d1")
		self.a2 = rospy.get_param("/parameters/a2")
		self.d4 = rospy.get_param("/parameters/d4")
		self.last_pos = 0
		self.start_pos = [0,0, (self.d1+self.a2+self.d4)]
		self.send_command(self.start_pos)
		self.target_pos = rospy.get_param("/parameters/target_pos")
		self.above_target_pos = rospy.get_param("/parameters/above_taret_pos")
		self.seq_num = 0
		self.gripper_open = rospy.get_param("/parameters/gripper_open")
		self.gripper_close = rospy.get_param("/parameters/gripper_closed")
		rospy.Subscriber('XYTopic', XYArray, self.xy_callback)
		rospy.Subscriber('ZTopic', ZArray, self.z_callback)
		
	def xy_callback(self, data):
		self.latest_xy_coords = data.data

	def z_callback(self, data):
		self.latest_z_coords = data.data

	def send_command(self,coords):
		joint_positions = []
		duration = rospy.Duration(1)
		for coord in coords:

			joint_trajectory_point = JointTrajectoryPoint(positions=self.invkin(coord),
													  		velocities=[0.5]*4,
													  		time_from_start=duration)
			duration += rospy.Duration(2)
			joint_positions.append(joint_trajectory_point)
		joint_trajectory = JointTrajectory(joint_names=self.joint_names,
											points=joint_positions)
		goal = FollowJointTrajectoryGoal(trajectory=joint_trajectory,
											goal_time_tolerance=duration+rospy.Duration(2))
		self.client.wait_for_server()
		self.client.send_goal(goal)
		self.client.wait_for_result()
		self.current_arm_position = self.client.get_result()

	def send_gripper_command(self, radians):
		#joint_positions = []
		duration = rospy.Duration(1)

		joint_trajectory_point = JointTrajectoryPoint(positions=radians,
													  		velocities=[0.5]*4,
													  		time_from_start=duration)
		duration += rospy.Duration(2)
		joint_trajectory = JointTrajectory(joint_names='gripper',
											points=joint_trajectory_point)
		goal = FollowJointTrajectoryGoal(trajectory=joint_trajectory,
											goal_time_tolerance=duration+rospy.Duration(2))
		self.client.wait_for_server()
		self.client.send_goal(goal)
		self.client.wait_for_result()
		self.current_arm_position = self.client.get_result()			

	def invkin(self, coords):
		x = coords[0]
		y = coords[1]
		z = coords[2]
		
		s2 = (x)**2+(y)**2
		r = (z-self.d1)
		D = (s2+r**2-self.a2**2-self.d4**2)/(2*self.a2*self.d4)

		q1 = math.atan2(y,x)
		q3 = math.atan2(-math.sqrt(1-D**2), D)
		q2 = math.atan2(math.sqrt(s2),r) - math.atan2(self.d4*math.sin(q3), self.a2 + self.d4*math.cos(q3)) # Eqn. (9,10,11)
		q4 = 0 #disregarding orientation atm
		return q1,q2,q3,q4






	def place_blocks(self):

		blocks_coords = [self.latest_xy_coords, self.latest_z_coords]

		for single_block_coords in blocks_coords:
			if self.current_arm_position == self.invkin(self.start_pos) and self.last_pos != single_block_coords:
				start_to_square = Trajectory.trajectory(self.start_pos,single_block_coords)
				self.send_command(start_to_square)

			if self.current_arm_position == self.invkin(single_block_coords):
				self.send_gripper_command(self.gripper_close)

			if self.current_arm_position == self.gripper_close:
				square_to_Above_cross = Trajectory.trajectory(single_block_coords,self.above_target_pos)
				self.send_command(square_to_Above_cross)

			if self.current_arm_position == self.invkin(self.above_target_pos):
				down_to_cross = Trajectory.trajectory(self.above_target_pos,self.target_pos)
				self.send_command(down_to_cross)

			if self.current_arm_position == self.invkin(self.target_pos):
				self.send_gripper_command(self.gripper_open)

			if self.current_arm_position == self.gripper_open:
				back_to_start = Trajectory.trajectory(self.target_pos,self.start_pos)
				self.send_command(back_to_start)
				self.last_pos = single_block_coords


