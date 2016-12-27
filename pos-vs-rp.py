# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:59:56 2016

@author: xdh

to evaluate the error based on POS data

"""


import fileio
import numpy as np
import matplotlib.pyplot as plt

#for pos data


rpfile = r'c:\Work\Papers\Pano\data\5point_relativepose.txt'
rpdata = fileio.readtxt(rpfile, " ")
rp_pitch = rpdata[:,0]
rp_roll  = rpdata[:,1]
rp_yaw   = rpdata[:,2]  


   
   
posfile = r'c:\Work\Papers\Pano\data\pana-cam.txt'
posdata = fileio.readtxt(posfile, " ")
pos_pitch = posdata[:,0]
pos_roll  = posdata[:,1]
pos_yaw   = posdata[:,2]  
   

pitcherror = abs(rp_pitch - pos_pitch)
print("pitch")
print(np.min(pitcherror))
print(np.max(pitcherror))
num = pitcherror.size
#print(num)
dist = np.sqrt(  np.sum(np.square(pitcherror)) / num )  
print(dist)
#plt.hist(pitcherror, bins=40, normed=True)
#print(np.nanstd(pitcherror))


rollerror = abs(rp_roll - pos_roll)
print("roll")
print(np.min(rollerror))
print(np.max(rollerror))
num = rollerror.size
dist = np.sqrt(  np.sum(np.square(rollerror)) / num )  
print(dist)
#print(np.nanstd(rollerror))


yawerror = abs(rp_yaw - pos_yaw)
print("yaw")
print(np.min(yawerror))
print(np.max(yawerror))
#print(np.nanstd(yawerror))
num = yawerror.size
dist = np.sqrt(  np.sum(np.square(yawerror)) / num )  
print(dist)


#for translation
print('*************** translation **********************')
numimage = (rpdata.shape)[0]
angleArray = np.zeros(numimage)
for i in range(0, numimage):
    a = rpdata[i, 3:5]
    b = posdata[i, 3:5]
    na = np.sqrt(np.dot(a,a))
    nb = np.sqrt(np.dot(b,b))
    #print( np.sqrt(np.dot(a,a)) )
    #print( np.sqrt(np.dot(b,b)) )
    dotValue = np.dot(a,b) / (na*nb)    
    #print( np.arccos(dotValue) / np.pi * 180 )
    angleArray[i] = np.arccos(dotValue) / np.pi * 180 
    
#print(angleArray)

print( np.min( angleArray ) )
print( np.max( angleArray ) )
num = angleArray.size
dist = np.sqrt(  np.sum(np.square(angleArray)) / num )  
print(dist)

#save the errors
#plt.figure(figsize=(4,3),dpi=300)
#plt.hist(pitcherror, bins=20, normed=True)
#print(pitcherror)

    
    
