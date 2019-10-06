# Digital Elevation Maps - Slope 
# Juan Pablo Herrera 

# Import Libraries
import os 
import zipfile

# Laod vector layer
fn = '/Users/juanpablo/OneDrive/UTS/iLab1/QGIS/Network/ClipData/StudyArea.shp'
vlayer = iface.addVectorLayer(fn, '', 'ogr') # ogr for most shapefiles

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

un_zipFiles(dir)

# Load Raster layer
def load_rasters(path):
    files=os.listdir(path)
    for file in files:
        if file.endswith('.asc'):
            filePath =  path + '/' + file
            rlayer = iface.addRasterLayer(filePath, '')

load_rasters(dir)
