# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:47:37 2016

@author: xdh
"""


def readtxt(filename):
    fp = open(filename, "r")
    lines = fp.readlines()
    rows = 0;
    for line in lines:
        rows = rows + 1
        
    temp1 = lines[0].strip('\n') 
    temp2 = temp1.split(",")
    cols = len(temp2)
    print(rows, cols)        