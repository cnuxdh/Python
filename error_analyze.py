# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:59:46 2016

@author: xdh
"""

import fileio
import numpy as np

#data = fileio.readtxt(r"c:\temp\pana-cam.txt", " ")

data = fileio.readtxt(r"c:\temp\epipolarError.txt", " ")

print( np.min(data[:,0]) )
print( np.max(data[:,0]) )
print( np.mean(data[:,0]) )


#calculate the std using the errors directly
num = data[:,0].size
dist  = np.sqrt(  np.sum(np.square(data[:,0])) / num ) 
#dist1 = np.linalg.norm(data[:,0]) / np.sqrt(num)
#print(dist, dist1)
#print( np.nanstd(data[:,0]) )
print(dist)

meanError = np.mean(data[:,0])


wd = 2048
radius = wd / (2*np.pi)
print( (dist/radius)/np.pi*180)


#print(data)




