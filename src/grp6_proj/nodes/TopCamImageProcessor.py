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
    pub = rospy.Publisher('XandY', Float32, queue_size=10)
    rospy.init_node('TopCamImageProcessor') #The next line, rospy.init_node(NAME, ...), is very important as it tells rospy the name of your node -- until rospy has this information, it cannot start communicating with the ROS Master. In this case, your node will take on the name talker. NOTE: the name must be a base name, i.e. it cannot contain any slashes "/".
    thresholdValueGreen = 50
    thresholdValueRed = 50
    thresholdValueYellow = 50
    thresholdValueBlue = 65
    # Read image
    frame = cv2.imread('/home/ros/catkin_repo/ros/src/grp6_proj/nodes/top1')

    #resize frame
    frame = cv2.resize(frame, (640,480))
    #convert til HSV colorspace
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # Show image on screen
    cv2.imshow('frame', frame)
    #wait untill keypress
    cv2.waitKey()
    
    #find color green
    if Color == 'green':
        # Range for green
        #Hue has value from 0-180 (value from Photoshop/2)
        #Saturation 255 is full color, 0 is white (photoshop values is in %)
        #Value/brightness interval from 0-255. 255 is full color, 0 is black (photoshop values is in %)
        green_lower = np.array([40,65,100])
        green_upper = np.array([75,255,255])
        mask_green = cv2.inRange(hsv, green_lower, green_upper)

        exr = cv2.bitwise_and(frame, frame, mask=mask_green)
        cv2.imshow("Frame", exr)

        #HSVtoGRAY(exr)
        exr = cv2.cvtColor(exr,cv2.COLOR_HSV2BGR)
        exr = cv2.cvtColor(exr, cv2.COLOR_BGR2GRAY)
        #Threshold for hvornaar farven bliver talt med
        thresholded = ((exr>thresholdValueGreen)*255).astype('uint8')

    
    elif Color == 'red':
        # Range for lower red
        red_lower = np.array([0,150,100])
        red_upper = np.array([10,255,255])
        mask_red1 = cv2.inRange(hsv, red_lower, red_upper)

        # Range for upper range
        red_lower = np.array([170,150,50])
        red_upper = np.array([180,255,255])
        mask_red2 = cv2.inRange(hsv, red_lower, red_upper)

        mask_red = mask_red1 + mask_red2
        exr = cv2.bitwise_and(frame, frame, mask=mask_red)
    
        cv2.imshow("Frame", exr)

        exr = cv2.cvtColor(exr,cv2.COLOR_HSV2BGR)
        exr = cv2.cvtColor(exr, cv2.COLOR_BGR2GRAY);
        
        
        thresholded = ((exr>thresholdValueRed)*255).astype('uint8')
        
    
    elif Color == 'blue':
        # Range for blue
        blue_lower = np.array([105,50,50])
        blue_upper = np.array([125,255,255])
        mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

        exr = cv2.bitwise_and(frame, frame, mask=mask_blue)
        cv2.imshow("Frame", exr)

        exr = cv2.cvtColor(exr,cv2.COLOR_HSV2BGR)
        cv2.imshow("1", exr)
        exr = cv2.cvtColor(exr, cv2.COLOR_BGR2GRAY);
        cv2.imshow("2", exr)
        #noise reduction usuin blurfilter
        kernel = np.ones((5,5),np.float32)/25
        exr = cv2.filter2D(exr,-1,kernel)
        cv2.imshow("3", exr)
        
        
        thresholded = ((exr>thresholdValueBlue)*255).astype('uint8')
    
    elif Color == 'yellow':
        # Range for yellow
        yellow_lower = np.array([25,80,20])
        yellow_upper = np.array([35,255,255])
        mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

        exr = cv2.bitwise_and(frame, frame, mask=mask_yellow)
        cv2.imshow("Frame", exr)

        exr = cv2.cvtColor(exr,cv2.COLOR_HSV2BGR)
        exr = cv2.cvtColor(exr, cv2.COLOR_BGR2GRAY);
        #noise reduction usuin blurfilter
        kernel = np.ones((5,5),np.float32)/25
        exr = cv2.filter2D(exr,-1,kernel)
        
        thresholded = ((exr>thresholdValueYellow)*255).astype('uint8')
    else: 
        print('***Please choose a valid color***')

    
    # show those areas
    #cv2.imshow('exrWithThreshold', thresholded)
    cv2.waitKey()

    #dette kode er taget fra undervisningen - Skrevet af: Mads Dyrmann and Henrik Skov Midtiby
    # Find connected components
    _, contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # loop through all components, one at the time
    for cnt in contours:
        # Whats the area of the component?
        areal = cv2.contourArea(cnt)
        
        # Do something is area is > 1
        if(areal > 1):
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
                print (cx)
                print (cy)
            
            #print ('x:', cx,'y:', cy)
            
            #publish coordinates
            while not rospy.is_shutdown():
                pub.publish(cx)    #publish coordinates
                pub.publish(cy)
                rospy.Rate(1).sleep() #publish every 1 sec

            # Tegn et sigtekorn paa billedet, der markerer elementet.
            # <alter these lines>
            frame = cv2.drawMarker(frame, (cx, cy), (255,0,255),markerType=cv2.MARKER_CROSS, thickness=2)
            # </alter these lines>        
    #viser billede med kryds paa
    cv2.imshow('frame annotated', frame)

    cv2.waitKey(0)   
    
    return
ColorDetector('green')   #used for test

