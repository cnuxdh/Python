# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import fileio
import numpy as np
import matplotlib.pyplot as plt

# for simulated data


data = fileio.readtxt(r"C:\temp\posepano-angle.txt", ',')
pitchErrors = data[:,6]
rollErrors  = data[:,7]
yawErrors   = data[:,8]

print("pitch angle:")
print( np.min(pitchErrors))
print( np.max(pitchErrors))
#print( np.nanstd(pitchErrors))
num = pitchErrors.size
dist = np.sqrt(  np.sum(np.square(pitchErrors)) / num )  
print(dist)

print("roll angle:")
print( np.min(rollErrors))
print( np.max(rollErrors))
#print( np.nanstd(rollErrors))
num = rollErrors.size
dist = np.sqrt(  np.sum(np.square(rollErrors)) / num )  
print(dist)

print("yaw angle")
print( np.min(yawErrors))
print( np.max(yawErrors))
#print( np.nanstd(yawErrors))
num = yawErrors.size
dist = np.sqrt(  np.sum(np.square(yawErrors)) / num )  
print(dist)



#hist = np.histogram(pitchErrors, 40)
#plt.figure(figsize=(4,3),dpi=300)
#plt.hist(pitchErrors, bins=40, normed=True)
#plt.hist(rollErrors, bins=40, normed=True)
#plt.hist(yawErrors, bins=40, normed=True)



    