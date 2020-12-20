#!/usr/bin/env python
from __future__ import division
import numpy as np


def trajectory(start_cord, stop_cord):
	if start_cord[0] == stop_cord[0]:
		xarr = start_cord[0]*np.ones(20)
	else:
		xarr = np.arange(start_cord[0],stop_cord[0], (stop_cord[0]-start_cord[0])/20)
	

	if start_cord[1] == stop_cord[1]:
		yarr = start_cord[1]*np.ones(20)
	else:
		yarr = np.arange(start_cord[1],stop_cord[1], (stop_cord[1]-start_cord[1])/20)
	

	if start_cord[2] == stop_cord[2]:
		zarr = start_cord[2]*np.ones(20)
	else:
		zarr = np.arange(start_cord[2],stop_cord[2], (stop_cord[2]-start_cord[2])/20)

	return [xarr,yarr,zarr]