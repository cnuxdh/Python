# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:59:56 2016

@author: xdh

to evaluate the error based on POS data

"""



import numpy as np
import matplotlib.pyplot as plt



numlines = 39

rp_pitch = np.zeros(numlines)
rp_roll  = np.zeros(numlines)
rp_yaw   = np.zeros(numlines)


rpfile = r'c:\Work\Papers\Pano\data\5point_relativepose.txt'
fp = open(rpfile, "r")
lines = fp.readlines()
index = 0;
for line in lines:
    temp1 = line.strip('\n') 
    temp2 = temp1.split(" ")
    #print(temp2)
    rp_pitch[index] = float(temp2[0])
    rp_roll[index] = float(temp2[1])
    rp_yaw[index] = float(temp2[2])  
    index = index + 1

    
pos_pitch = np.zeros(numlines)
pos_roll  = np.zeros(numlines)
pos_yaw   = np.zeros(numlines)        
posfile = r'c:\Work\Papers\Pano\data\pana-cam.txt'
fp = open(posfile, "r")
lines = fp.readlines()
index = 0;
for line in lines:
    temp1 = line.strip('\n') 
    temp2 = temp1.split(" ")
    #print(temp2)
    pos_pitch[index] = float(temp2[0])
    pos_roll[index] = float(temp2[1])
    pos_yaw[index] = float(temp2[2]) 
    index = index + 1

    
    
    

pitcherror = abs(rp_pitch - pos_pitch)
print("pitch")
print(np.min(pitcherror))
print(np.max(pitcherror))
num = pitcherror.size
#print(num)
dist = np.sqrt(  np.sum(np.square(pitcherror)) / num )  
print(dist)
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



#save the errors


#plt.figure(figsize=(4,3),dpi=300)
#plt.hist(pitcherror, bins=20, normed=True)
#print(pitcherror)

    
    
