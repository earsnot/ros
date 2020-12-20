#!/usr/bin/env python
import cv2

def getImage2(IP):
	TopCameraAddress = IP
	#SideCameraAddress = 'http://192.168.x.xxx/video.cgi'
	cap0 = cv2.VideoCapture(TopCameraAddress) #VideoCapture from source 0
	#cap1 = cv2.VideoCapture(0) #VideoCapture from source 1
	while 1:
	  ret0, frame0 = cap0.read() #Read next frame
	  #ret1, frame1 = cap1.read()


	  cv2.imshow('Top',frame0) #Show the frame
	  #cv2.imshow('Side',frame1)

	  if cv2.waitKey(1) & 0xff == 27: # wait for ESC key to exit. "& 0xff" is added for x64 machines
	    break

	#cap.release()
	cv2.destroyAllWindows() #destroys all the windows we created

#getImage('http://192.168.1.100/video.cgi')
