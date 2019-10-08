# Raster Data Preprocessing
# GIS Reality
# Author: Juan Pablo Herrera 

# The code following has the intention of carry out the preprocessing for the raster layers
# containing the Digital Elevation Model DEM 

# Libraries 
import os 
#import qgis 
import gdal 

# Working Directory 
os.chdir('/Users/juanpablo/OneDrive/UTS/iLab1')

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

processing.runAndLoadResults('gdal:merge',
    {'INPUT': Rasters,
    'OUTPUT':'Temp/merged.tif'})

