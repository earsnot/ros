#!/usr/bin/env python
from cameraNode1 import getImage
from cameraNode2 import getImage2
from colorDetection2 import ColorDetector
from cameraNodeFrameTest import SingleFrame

SingleFrame('test')
ColorDetector('blue')
#getImage(0)
#getImage2('http://192.168.1.100/video.cgi')
