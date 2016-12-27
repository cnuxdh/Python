# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:59:46 2016

@author: xdh
"""

import fileio
import numpy as np

#data = fileio.readtxt(r"c:\temp\pana-cam.txt", " ")

#epipolar image error
#data = fileio.readtxt(r"c:\temp\epipolarError.txt", " ")

#simulated data translation angle
data = fileio.readtxt(r"c:\temp\posepano-translate.txt", " ")



print('min:', np.min(data[:,0]) )
print('max:', np.max(data[:,0]) )
print('mean:', np.mean(data[:,0]) )


#calculate the std using the errors directly
num = data[:,0].size
dist  = np.sqrt(  np.sum(np.square(data[:,0])) / num ) 
#dist1 = np.linalg.norm(data[:,0]) / np.sqrt(num)
#print(dist, dist1)
#print( np.nanstd(data[:,0]) )
print('std:', dist)

meanError = np.mean(data[:,0])


wd = 2048
radius = wd / (2*np.pi)
#print( (dist/radius)/np.pi*180)


#print(data)




