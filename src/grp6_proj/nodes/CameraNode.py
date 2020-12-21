#!/usr/bin/env python
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class CameraNode():
    def __init__(self, topic_name, node_name, img_source):
        self.topic_name = topic_name
        self.node_name = node_name
        self.img_source = img_source
        rospy.init_node(self.node_name, anonymous=True)
        self.pub = rospy.Publisher(topic_name, Image, queue_size=10)
    def getImage(self):
        capt = cv2.VideoCapture(self.img_source)
        while 1:
            ret, frame = capt.read()
            if ret:
                while not rospy.is_shutdown():
                    bridge = CvBridge()
                    img = bridge.cv2_to_imgmsg(frame, 'bgr8')
                    self.pub.publish(img)
            else:
                break

