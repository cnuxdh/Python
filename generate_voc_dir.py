# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:47:37 2016

@author: xdh
"""


import os
import sys

def mkdir(path):
   path=path.strip()
   path=path.rstrip("/")
   isExists=os.path.exists(path)
   if not isExists:
       os.makedirs(path) 
       return True
   else:
       return False

if __name__ == '__main__':
   num = len(sys.argv)
   if (num == 2):
     path = sys.argv[1]
     print(path)
     
     root = path+'/VOCdevkit' 
     mkdir(root)
     
     voc = root+'/VOCmy'
     mkdir(voc)
     
     mkdir(voc+'/Annotations')
     mkdir(voc+'/ImageSets')
     mkdir(voc+'/JPEGImages')
     mkdir(voc+'/SegmentationClass')   
     mkdir(voc+'/ImageSets/Main')
     mkdir(voc+'/ImageSets/Segmentation')  
     
   else:
     print('input error')
   



