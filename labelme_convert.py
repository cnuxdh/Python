# -*- coding: utf-8 -*-
from labelme.cli.json_to_dataset import main,convert
import os 
import re
import sys
import shutil

#jsons in one dir
jsons = []

#json_dir = '/media/xdh/Work/Data/Deeplearning/Karst/NewKarst/Json'
#png_dir = '/media/xdh/Work/Data/Deeplearning/Karst/NewKarst/SegmentationClassNew'

json_dir = '/media/xdh/SanDisk/Data/deeplearning/lane'
png_dir = '/media/xdh/SanDisk/Data/deeplearning/lane/label'


files = os.listdir(json_dir)
for file in files:
    if '.json' in file:
       convert(json_dir+'/'+file)


for file in files:
    if '.json' in file:
        jsonID = os.path.splitext(file)[0]
	print(jsonID)
        ResultFolderName = jsonID + '_json'
        Labelpath = json_dir + '/' + ResultFolderName + '/label.png'
        shutil.copy(Labelpath, png_dir + '/' + jsonID + '.png')  
