#!/usr/bin/env python
import cv2


def SingleFrame(OutputName):
	cap0 = cv2.VideoCapture(0) #VideoCapture from source 0
	ret0, frame0 = cap0.read() #Read next frame

	cv2.imwrite(OutputName+'.png', frame0) #saves a single frame

#SingleFrame('test3')
