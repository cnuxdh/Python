#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# author:"Zhang Shuyu"

"""使用skimage模块读取图片，不改变图片数据类型uint16，保存为uint8类型"""

import os
import cv2
import natsort
import numpy as np
from skimage import io
from matplotlib import pylab as plt

#input_file = "/media/xdh/Work/Data/Deeplearning/Karst/NewKarst/SegmentationClassNew/"  #文件路径
input_file = "/media/xdh/SanDisk/Data/deeplearning/lane/label/"
img_type = ".png"
 
for root, dirs, files in os.walk(input_file,topdown=True):
    #print(root, dirs, files)
    print(files)

    for name in natsort.natsorted(files):  #natsort,自然排序
        #print(len(name))
        #nl = len(name)
        #print(name[:nl-5])        
        
        
        #file_name = os.path.join(input_file + name, "label" + img_type)
        file_name = input_file + name
        print(file_name)
        
        img = io.imread(file_name)  #Todo:使用skimage模块读取图片不会改变图片的数据格式
        #print(img.dtype)
        img = img.astype(np.uint8)
        #print(img.dtype)
        #outfile = os.path.join(input_file + name, img_type)
        #outfile = input_file + name[:nl-5] + img_type
	#outfile = input_file + name[:nl-5] + img_type
        #print(outfile)
        
        cv2.imwrite(file_name, img)

