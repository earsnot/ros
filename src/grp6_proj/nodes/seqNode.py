#!/usr/bin/env python
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction
from control_msgs.msg import FollowJointTrajectoryFeedback
from control_msgs.msg import FollowJointTrajectoryResult
from control_msgs.msg import FollowJointTrajectoryGoal
from block_coords_array.msg import Coords
from trajectory_msgs.msg import JointTrajectoryPoint
from trajectory_msgs.msg import JointTrajectory
from utils.trajectory import trajectory

class SequenceNode:
	def __init__(self, node_name):
		self.node_name = node_name
		self.joint_names = rospy.get_param("parameters/joint_names")
		self.client = actionlib.SimpleActionClient("action_server", FollowJointTrajectoryAction)
		rospy.init_node(self.node_name)
		self.start_pos = [0,0, (rospy.get_param("/parameters/d1")+
								rospy.get_param("/parameters/a2")+
								rospy.get_param("/parameters/d4"))]
		self.send_command(self.start_pos)
		self.target_pos = rospy.get_param("/parameters/target_pos")
		self.actuator_target_pos = rospy.get_param("/parameters/above_taret_pos")
		self.seq_num = 0
		self.gripper_open = rospy.get_param("/parameters/gripper_open")
		self.gripper_close = rospy.get_param("/parameters/gripper_closed")
		rospy.Subscriber('Coordinates', coord_msg, self.callback)
		
	def callback(self, data):
		self.latest_block_coords = data.data

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




	def place_blocks(self):

		blocks_coords = self.latest_block_coords

		for single_block_coords in blocks_coords:
			if self.current_arm_position == invkin(self.start_pos) and last_pos != single_block_coords:
				start_to_square = trajectory(start_pos,single_block_coords)
				send_command(start_to_square)
				seq_num = 101
				# lav inver kinematik og smid det til robot

			if self.current_arm_position == invkin(single_block_coords):
				send_gripper_command(self.gripper_close)
				
				#Close Catcher 
				seq_num = 102

			if self.current_arm_position == self.gripper_close:
				square_to_Above_cross = trajectory(single_block_coords,above_cross_pos)
				send_command(square_to_Above_cross)
				# lav inver kinematik og smid det til robot
				seq_num = 103


			if self.current_arm_position == invkin(above_cross_pos):
				down_to_cross = trajectory(above_cross_pos,cross_pos)
				send_command(down_to_cross)
				# lav inver kinematik og smid det til robot
				seq_num = 104


			if self.current_arm_position == invkin(cross_pos):
				self.send_gripper_command(self.gripper_open)

			if self.current_arm_position == self.gripper_open:
				back_to_start = trajectory(cross_pos,start_pos)
				send_command(back_to_start)
				seq_num = 100
				last_pos = single_block_coords


