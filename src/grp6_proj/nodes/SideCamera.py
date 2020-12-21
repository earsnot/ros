#!/usr/bin/env python
import cv2
import numpy as np
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32

#Hue has value from 0-180 (value from Photoshop/2)
#Saturation 255 is full color, 0 is white (photoshop values is in %)
#Value/brightness interval from 0-255. 255 is full color, 0 is black (photoshop values is in %)


#inputColor = 'green'
#Threshold values



def ColorDetector(Color):
    # Read image
    frame = cv2.imread('/home/ros/catkin_repo/ros/src/grp6_proj/nodes/side5')

    #resize frame
    frame = cv2.resize(frame, (640,480))
    #convert til HSV colorspace
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # Show image on screen
    #cv2.imshow('frame', frame)
    #wait untill keypress
    #cv2.waitKey()
    
    while not rospy.is_shutdown():
        # Range for green
        #Hue has value from 0-180 (value from Photoshop/2)
        #Saturation 255 is full color, 0 is white (photoshop values is in %)
        #Value/brightness interval from 0-255. 255 is full color, 0 is black (photoshop values is in %)
        green_lower = np.array([40,65,1])
        green_upper = np.array([110,255,150])
        mask_green = cv2.inRange(hsv, green_lower, green_upper)
        # Range for lower red
        red_lower = np.array([0,150,1])
        red_upper = np.array([10,255,255])
        mask_red1 = cv2.inRange(hsv, red_lower, red_upper)
        # Range for upper range
        red_lower = np.array([170,150,1])
        red_upper = np.array([180,255,255])
        mask_red2 = cv2.inRange(hsv, red_lower, red_upper)
        mask_red = mask_red1 + mask_red2
        # Range for blue
        blue_lower = np.array([105,50,30])
        blue_upper = np.array([125,255,150])
        mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)
        # Range for yellow
        yellow_lower = np.array([25,80,20])
        yellow_upper = np.array([35,255,255])
        mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)



        exr_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
        exr_green = cv2.bitwise_and(frame, frame, mask=mask_green)
        exr_red = cv2.bitwise_and(frame, frame, mask=mask_red)
        exr_yellow = cv2.bitwise_and(frame, frame, mask=mask_yellow)
        exr_all = exr_blue + exr_green + exr_red + exr_yellow
        # Used for test to show image
        # cv2.imshow("blue", exr_blue)
        # cv2.waitKey()
        # cv2.imshow("green", exr_green)
        # cv2.waitKey()
        # cv2.imshow("red", exr_red)
        # cv2.waitKey()
        # cv2.imshow("yellow", exr_yellow)
        # cv2.waitKey()
        # cv2.imshow("exr_all", exr_all)
        # cv2.waitKey()


        #Isolate Value/brightness from HSV
        hsv1 = cv2.cvtColor(exr_all, cv2.COLOR_BGR2HSV)
        h, s, v1 = cv2.split(hsv1)
        # cv2.imshow("gray-image",v1)
        # cv2.waitKey()
        

        im_bw = v1 #because im lazy and dont want tp change variable names
        (thresh, im_bw) = cv2.threshold(im_bw, 10, 255, 0) #converts gray to black and white. A value of 10 is chosen because we have very low light in out picture
        # cv2.imshow('bw_1', im_bw)
        # cv2.waitKey()


        contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) [-2:]


        for c in contours:
            x,y,w,h = cv2.boundingRect(c)
            if (w>30 and w<110) and h>30:
                cv2.rectangle(exr_all,(x,y),(x+w,y+h),(255,0,255),1)
                #cv2.imshow('X',X)
                print(h)
         
        cv2.imshow('cnt_1', exr_all)
        cv2.waitKey()
            
    return
ColorDetector('height')   #used for test

