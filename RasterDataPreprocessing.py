# Raster Data Preprocessing
# Author: Juan Pablo Herrera
# MDSI - UTS Srping 2019 
# GIS Reality

# The following code has the intention of carry out the preprocessing for the raster layers
# containing the Digital Elevation Model DEM 

# Libraries 
import os 
import qgis 
import gdal 

# Working directory 
os.chdir('/Users/juanpablo/OneDrive/UTS/iLab1')

# Un-zips all the tiles that contain the DEM for our study area, One use only.
def un_zipFiles(path):
    '''
    Un-zip all the tiles that contain the DEM for our study are
    '''
    files=os.listdir(path)
    for file in files:
        if file.endswith('.zip'):
            filePath=path+'/'+file
            zip_file = zipfile.ZipFile(filePath)
            for names in zip_file.namelist():
                zip_file.extract(names,path)
            zip_file.close() 

#dir = '/Users/juanpablo/OneDrive/UTS/iLab1/1Metre'
#un_zipFiles(dir)

# Genrates list containig all the paths for the DEM
def loadrasters(path):
    '''
    Generates a list with all the file paths for the different segments of the DEM
    '''
    rasterlist = []
    files = os.listdir(path)
    for file in files:
        if file.endswith('.asc'):
            filepath = os.getcwd() + '/' + path + '/' + file 
            rasterlist.append(filepath)
    return rasterlist

# Merge all the DEM into a single file
dir = '1Metre' # Folder cotaining un-zipped files
Rasters = loadrasters(dir)

# Merges all the tiles that conform the DEM into a single file
processing.run('gdal:merge',
    {'INPUT': Rasters,
    'OUTPUT':'Temp/mergedDEM.tif'})

# CLips the global DEM to the size of the Study area using the study area shapefile
## Requieres VectorDataPreprocessing to be completed first
## Optional step, is mostly used for presentation purposes
processing.run("gdal:cliprasterbymasklayer",
        {'INPUT': 'Temp/mergedDEM.tif',
        'MASK': 'Temp/Dissolved.shp',   
        'NODATA': 0,
        'CROP_TO_CUTLINE': True,
        'KEEP_RESOLUTION': True,
        'OPTIONS': "",
        'DATA_TYPE': 0,
        'OUTPUT': 'Temp/FinalDEM.tif'})