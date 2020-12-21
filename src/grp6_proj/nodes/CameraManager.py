from CameraNode import CameraNode

topcam = CameraNode('TopCam', 'TopCam', 'nodes/top1.png')
sidecam = CameraNode('SideCam', 'SideCam', 'nodes/top1.png')

topcam.getImage()
sidecam.getImage()

