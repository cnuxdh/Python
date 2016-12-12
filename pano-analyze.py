# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt



#f = open("C:\\temp\\posepano-angle.txt","r")  
f = open('C:\Work\Papers\Pano\data\posepano-angle-noise is 0.5.txt',"r")  
lines = f.readlines()  #读取全部内容  
pitchErrors = np.zeros(100)
rollErrors = np.zeros(100);
yawErrors = np.zeros(100);
index = 0
for line in lines : 
    temp1 = line.strip('\n')       #去掉每行最后的换行符'\n'
    temp2 = temp1.split(' ')       #以','为标志，将每行分割成列表
    #print( temp2[6] )  
    pitchErrors[index] = float(temp2[9])
    rollErrors[index] = float(temp2[10])
    yawErrors[index] = float(temp2[11])
    index = index + 1
    
print("pitch angle:")
print( np.min(pitchErrors))
print( np.max(pitchErrors))
print( np.nanstd(pitchErrors))

print("roll angle:")
print( np.min(rollErrors))
print( np.max(rollErrors))
print( np.nanstd(rollErrors))

print("yaw angle")
print( np.min(yawErrors))
print( np.max(yawErrors))
print( np.nanstd(yawErrors))


#hist = np.histogram(pitchErrors, 40)
#plt.figure(figsize=(4,3),dpi=300)
#plt.hist(pitchErrors, bins=40, normed=True)
#plt.hist(rollErrors, bins=40, normed=True)
#plt.hist(yawErrors, bins=40, normed=True)



    