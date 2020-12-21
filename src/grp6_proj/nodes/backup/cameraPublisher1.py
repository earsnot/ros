#!/usr/bin/env python
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
bridge = CvBridge()


pub = rospy.Publisher('CameraTopic', Image, queue_size=10)


#SideCameraAddress = 'http://192.168.x.xxx/video.cgi'
cap0 = cv2.VideoCapture('top1.png') #VideoCapture from source 0
while 1:
  ret0, frame0 = cap0.read() #Read next frame
  rospy.init_node('node_name', anonymous=True) #anonymous sikre at navnet er unikt
  rate = rospy.Rate(0.1)


while not rospy.is_shutdown():
  rospy.loginfo(frame0)
  img = bridge.cv2_to_imgmsg(frame0, 'bgr8')
  pub.publish(img)


#getImage('http://192.168.1.100/video.cgi')
