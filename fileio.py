# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:47:37 2016

@author: xdh
"""
import numpy as np

def readtxt(filename, seperator):
    
    fp = open(filename, "r")
    lines = fp.readlines()
    fp.close()
    
    #seperator = " " 
    
    rows = 0;
    for line in lines:
        rows = rows + 1
        
    temp1 = lines[0].strip('\n') 
    temp1 = temp1.rstrip()
    temp2 = temp1.split(seperator)
    #print(temp2)
    cols = len(temp2)
    print("rows= ", rows, " cols= ", cols)        
    
    data = np.zeros( (rows, cols) )
    
    index = 0
    for line in lines:
        temp1 = line.strip('\n') 
        temp1 = temp1.rstrip()
        temp2 = temp1.split(seperator)
        for i in range(0, cols):
            data[index][i] = float(temp2[i])
        index = index + 1    
        
    return data
        