#!/usr/bin/env python
import cv2
import rospy
import numpy
from std_msgs.msg import String
from std_msgs.msg import UInt8MultiArray
from rospy.numpy_msg import numpy_msg
from sensor_msgs.msg import Image

#UInt8MultiArray
#numpy.ndarray
pub = rospy.Publisher('CameraTopic', Image, queue_size=10)


#SideCameraAddress = 'http://192.168.x.xxx/video.cgi'
cap0 = cv2.VideoCapture('top1.png') #VideoCapture from source 0
while 1:
  X = ret0, frame0 = cap0.read() #Read next frame
  a = numpy.array([frame0], dtype=object)
  #print(frame0)
  
  rospy.init_node('node_name', anonymous=True) #anonymous sikre at navnet er unikt
  rate = rospy.Rate(10)


  while not rospy.is_shutdown():
  	#rospy.loginfo(frame0)
    img = bridge.cv2_to_imgmsg(cap0, 'bgr8')
    pub.publish(img)


#getImage('http://192.168.1.100/video.cgi')
