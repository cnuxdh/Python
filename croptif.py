# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import gdal
from osgeo import gdal
import numpy as np
import cv2


import gdal
import numpy as np
def writeTiff(im_data,im_width,im_height,im_bands,im_geotrans,im_proj,path):
    if 'int8' in im_data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in im_data.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32

    if len(im_data.shape) == 3:
        im_bands, im_height, im_width = im_data.shape
    elif len(im_data.shape) == 2:
        im_data = np.array([im_data])
    else:
        im_bands, (im_height, im_width) = 1,im_data.shape
    
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(path, im_width, im_height, im_bands, datatype)
    if(dataset!= None):
        dataset.SetGeoTransform(im_geotrans) #写入仿射变换参数
        dataset.SetProjection(im_proj) #写入投影
    for i in range(im_bands):
        dataset.GetRasterBand(i+1).WriteArray(im_data[i])
    del dataset


def readTif(fileName):
    dataset = gdal.Open(fileName)
    if dataset == None:
        print(fileName+" can not open!")
        return
        
    im_width  = dataset.RasterXSize
    im_height = dataset.RasterYSize
    im_bands  = dataset.RasterCount
    
    im_geotrans = dataset.GetGeoTransform()
    im_proj = dataset.GetProjection()
    
    #print(im_width, im_height, im_bands, im_geotrans, im_proj)
    print(im_geotrans, im_proj)
    
  
    im_data   = dataset.ReadAsArray(0,0,im_width,im_height)
    
    x = 515
    y = 5527
    crop_data = np.zeros( (3,500,500), dtype=np.uint16 )
    print(crop_data.shape)
    
    crop_data[0,:,:]   =  im_data[3,y:y+500,x:x+500]
    crop_data[1,:,:]   =  im_data[5,y:y+500,x:x+500]
    crop_data[2,:,:]   =  im_data[7,y:y+500,x:x+500]
    #im_nirBand   =  im_data[3,0:im_height,0:im_width]
    
    #print(im_blueBand.shape)
    
    #return crop_data, im_geotrans, im_proj
    return im_data,
    #cv2.imwrite(r"c:\Han\Data\blue.jpg", im_blueBand)
    
    

if __name__=='__main__':
    print("crop tif .... ")
    
    filename = r"D:\Data\Karst-Landsat\Guilin\GL-30\Guilin-layer-30.tif"
    print(filename)

    '''
    image = cv2.imread(filename)
    cv2.imshow("image", image)
    cv2.waitKey()
    '''
    
    crop_data, im_geotrans, im_proj = readTif(filename)
        
    print(im_data.shape)
    
    writeTiff(crop_data,500,500,3,im_geotrans,im_proj, r"c:\Han\Data\out.tif")
    
    
    