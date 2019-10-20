# Digital Elevation Maps - Slope 
# Juan Pablo Herrera 
# The present code is the raw version of the final product

# Import Libraries
import os 
import qgis
import zipfile
import gdal

# Define working directory
os.chdir('/Users/juanpablo/OneDrive/UTS/iLab1')

# Loads vector layer with Study Area 
fn = 'QGIS/Network/ClipData/StudyArea.shp'
#vlayer = iface.addVectorLayer(fn, '', 'ogr') # ogr for most shapefiles
QgsVectorLayer(fn, '', 'ogr')

# Dissolve the study area to generete single outline
processing.runAndLoadResults("native:dissolve", 
    {'FIELD':[], 
    'INPUT': fn,
    'OUTPUT': 'memory:'})



## Unzips all the folders containing the raster layers
dir = '/Users/juanpablo/OneDrive/UTS/iLab1/1Metre'

def un_zipFiles(path):
    files=os.listdir(path)
    for file in files:
        if file.endswith('.zip'):
            filePath=path+'/'+file
            zip_file = zipfile.ZipFile(filePath)
            for names in zip_file.namelist():
                zip_file.extract(names,path)
            zip_file.close() 

#un_zipFiles(dir)

# Load Raster layers
def load_rasters(path):
    files=os.listdir(path)
    for file in files:
        if file.endswith('.asc'):
            filePath =  path + '/' + file
            rlayer = iface.addRasterLayer(filePath, '')


