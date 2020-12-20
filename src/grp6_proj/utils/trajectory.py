#!/usr/bin/env python
import numpy as np

def trajectory(start_cord, stop_cord):
	if(start_cord(1) == stop_cord(1)):
		xarr = start_cord(1)*np.ones(20)
	else:
		xarr = range(start_cord(1),(start_cord(1)-stop_cord(1))/20,stop_cord(1))
	

	if start_cord(2) == stop_cord(2):
		yarr = start_cord(2)*np.ones(20)
	else:
		yarr = range(start_cord(2),(start_cord(2)-stop_cord(2))/20,stop_cord(2))
	

	if start_cord(3) == stop_cord(3):
		zarr = start_cord(3)*np.ones(20)
	else:
		zarr = range(start_cord(3),(start_cord(3)-stop_cord(3))/20,stop_cord(3))

	return [xarr,yarr,zarr]	
	