#!/usr/bin/env python
import cv2
import numpy as np
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from grp6_proj.msg import XYArray

pub = rospy.Publisher('XYTopic', XYArray, queue_size=10)
rospy.init_node('TopCamImageProcessor') #The next line, rospy.init_node(NAME, ...), is very important as it tells rospy the name of your node -- until rospy has this information, it cannot start communicating with the ROS Master. In this case, your node will take on the name talker. NOTE: the name must be a base name, i.e. it cannot contain any slashes "/".

# Read image
frame = cv2.imread('/home/ros/catkin_repo/ros/top1')

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
    green_lower = np.array([40,65,100])
    green_upper = np.array([75,255,255])
    mask_green = cv2.inRange(hsv, green_lower, green_upper)
    #use the mask
    exr_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    #cv2.imshow("green", exr_green)
    #cv2.waitKey()


    # Range for lower red
    red_lower = np.array([0,150,100])
    red_upper = np.array([10,255,255])
    mask_red1 = cv2.inRange(hsv, red_lower, red_upper)
    # Range for upper range
    red_lower = np.array([170,150,50])
    red_upper = np.array([180,255,255])
    mask_red2 = cv2.inRange(hsv, red_lower, red_upper)
    mask_red = mask_red1 + mask_red2
    exr_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    #cv2.imshow("red", exr_red)
    #cv2.waitKey()
    
            
            
            # Range for blue
    blue_lower = np.array([105,50,50])
    blue_upper = np.array([125,255,255])
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

    exr_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    #cv2.imshow("blue", exr_blue)
    #cv2.waitKey()

    
    # Range for yellow
    yellow_lower = np.array([25,80,20])
    yellow_upper = np.array([35,255,255])
    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    exr_yellow = cv2.bitwise_and(frame, frame, mask=mask_yellow)
    #cv2.imshow("YELLOW", exr_yellow)
    #cv2.waitKey()
            
    
    #combine all masks
    exr_all = exr_blue + exr_green + exr_red + exr_yellow

    #cv2.imshow("Samlet", exr_all)
    #cv2.waitKey()   

    #Isolate Value/brightness from HSV
    hsv1 = cv2.cvtColor(exr_all, cv2.COLOR_BGR2HSV)
    h, s, v1 = cv2.split(hsv1)
    #cv2.imshow("gray-image",v1)
    #cv2.waitKey()
    

    im_bw = v1 #because im lazy and dont want tp change variable names
    (thresh, im_bw) = cv2.threshold(im_bw, 110, 255, 0) #converts gray to black and white. First value is the threshold for when a color is deamed to be white
    #cv2.imshow('bw_1', im_bw)
    #cv2.waitKey()



# show those areas
#cv2.imshow('exrWithThreshold', im_bw)
#cv2.waitKey()

#dette kode er taget fra undervisningen - Skrevet af: Mads Dyrmann and Henrik Skov Midtiby
# Find connected components
contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) [-2:]


coordinates=[]
# loop through all components, one at the time
for cnt in contours:
    # Whats the area of the component?
    areal = cv2.contourArea(cnt)
    
    # Do something is area is > 10
    if(areal > 10):
        # get the center of mass
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        #print(cx, cy)
        #coordinates = "x: %s, y: %d" % (cx,cy)

        #alternativ
        # cx=sum(cnt[:,0][:,0])/len(cnt[:,0][:,0])
        # cy=sum(cnt[:,0][:,1])/len(cnt[:,0][:,1])

        #Print the coordinates that are within our limits/table
        A1 = (cy>34 and cy<310) and (cx>1 and cx<237)
        A2 = (cy>34 and cy<310) and (cx>381 and cx<600)
        A3 = (cy>34 and cy<233) and (cx>237 and cx<381)
        if (A1 or A2 or A3):
            #print (cx)
            #print (cy)
            coords = XYArray(Coords=[cx,cy])
            coordinates.append(coords)
            pub.publish(coords)
        
        #print ('x:', cx,'y:', cy)
        
        

        # Tegn et sigtekorn paa billedet, der markerer elementet.
        # <alter these lines>
        frame = cv2.drawMarker(frame, (cx, cy), (255,0,255),markerType=cv2.MARKER_CROSS, thickness=2)
        # </alter these lines>        
#viser billede med kryds paa
#cv2.imshow('frame annotated', frame)

#cv2.waitKey(0)

