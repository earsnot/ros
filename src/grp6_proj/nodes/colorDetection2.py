# -*- coding: utf-8 -*-
"""

"""
#!/usr/bin/env python
import cv2
import numpy as np

#inputColor = 'green'
#Threshold values
thresholdValueGreen = 10
thresholdValueRed = 170
thresholdValueYellow = 150
thresholdValueBlue = 1


def ColorDetector(Color):
    
    # Read image
    frame = cv2.imread('test.png')

    #resize frame
    frame = cv2.resize(frame, (640,480))
    #convert til HSV colorspace
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # Show image on screen
    cv2.imshow('frame', frame)
    #wait untill keypress
    cv2.waitKey()
    
    #finder farven grøn
    if Color == 'green':
        # Range for green
        green_lower = np.array([30,50,50])
        green_upper = np.array([90,255,255])
        mask_green = cv2.inRange(hsv, green_lower, green_upper)

        exr = cv2.bitwise_and(frame, frame, mask=mask_green)
        cv2.imshow("Frame", exr)

        #HSVtoGRAY(exr)
        exr = cv2.cvtColor(exr,cv2.COLOR_HSV2BGR)
        exr = cv2.cvtColor(exr, cv2.COLOR_BGR2GRAY)
        #Threshold for hvornår farven bliver talt med
        thresholded = ((exr>thresholdValueGreen)*255).astype('uint8')

    
    elif Color == 'red':
        # Range for lower red
        red_lower = np.array([0,150,100])
        red_upper = np.array([10,255,255])
        mask_red1 = cv2.inRange(hsv, red_lower, red_upper)

        # Range for upper range
        red_lower = np.array([170,150,100])
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
        blue_lower = np.array([94,150,100])
        blue_upper = np.array([126,255,255])
        mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

        exr = cv2.bitwise_and(frame, frame, mask=mask_blue)
        cv2.imshow("Frame", exr)

        exr = cv2.cvtColor(exr,cv2.COLOR_HSV2BGR)
        exr = cv2.cvtColor(exr, cv2.COLOR_BGR2GRAY);
        
        
        thresholded = ((exr>thresholdValueBlue)*255).astype('uint8')
    
    elif Color == 'yellow':
        # Range for yellow
        yellow_lower = np.array([10,80,20])
        yellow_upper = np.array([30,255,255])
        mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

        exr = cv2.bitwise_and(frame, frame, mask=mask_yellow)
        cv2.imshow("Frame", exr)

        exr = cv2.cvtColor(exr,cv2.COLOR_HSV2BGR)
        exr = cv2.cvtColor(exr, cv2.COLOR_BGR2GRAY);
        
        thresholded = ((exr>thresholdValueYellow)*255).astype('uint8')
    else: 
        print("***Please choose a valid color***")

    
    # show those areas
    cv2.imshow('exr', thresholded)
    cv2.waitKey()

    #dette kode er taget fra undervisningen - Skrevet af: Mads Dyrmann and Henrik Skov Midtiby
    # Find connected components
    contours, hierarchy = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # loop through all components, one at the time
    for cnt in contours:
        # Whats the area of the component?
        areal = cv2.contourArea(cnt)
        
        # Gør noget hvis arealet er større end 1.
        if(areal > 1):
            # get the center of mass
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #print(cx, cy)
            
            #alternativ
            # cx=sum(cnt[:,0][:,0])/len(cnt[:,0][:,0])
            # cy=sum(cnt[:,0][:,1])/len(cnt[:,0][:,1])
            # print cx1,cy1
            
            
            # Tegn et sigtekorn på billedet, der markerer elementet.
            # <alter these lines>
            frame = cv2.drawMarker(frame, (cx, cy), (255,0,255),markerType=cv2.MARKER_CROSS, thickness=2)
            # </alter these lines>        
    #viser billede med kryds på
    cv2.imshow('frame annotated', frame)

    cv2.waitKey(0)

    return    
# kan ikke bruges af en eller anden ¨grund
# def HSVtoGRAY(exr):
#     exr = cv2.cvtColor(exr,cv2.COLOR_HSV2BGR)
#     exr = cv2.cvtColor(exr, cv2.COLOR_BGR2GRAY)
#     thresholded = ((exr>thresholdValueGreen)*255).astype('uint8')
#     print("1")
