# Pedestrian Network road slope calculation
# Author: Juan Pablo Herrera
# MDSI - UTS Srping 2019 
# GIS Reality

# The Following code calculate the slope for the different road segments, in this particualar approach 
# we split the road segments into subsetion of 100 meters for better accuracy.

## Requires VectorDataPreporcessing and RasterDataPreprocessing to be completed first\

# Libraries
import os 
import qgis 

# Working directory
os.chdir('/users/juanpablo/OneDrive/UTS/iLab1')

# Split road segments by maximun length of 100, segments shorter thant 100 meters remain unchanged
FinalPedestrianRoad = 'Temp/FinalPedestrianRoad.shp'  # Pedestrian road product of the VectorDataPreprocessing 
splitted = 'Temp/Splitted.shp'
processing.run('native:splitlinesbylength',
    {'INPUT': FinalPedestrianRoad,
    'LENGTH': 100,
    'OUTPUT': splitted})

# Generate a new OBJECTID 
splittedID = 'Temp/splittedID.shp'
processing.run('qgis:fieldcalculator',
    {'INPUT': splitted,
    'FIELD_NAME': 'SPLITID',
    'FIELD_TYPE': 1,                    # 0: Float, 1: Intger, 2: String, 3: DAte 
    'FIELD_PRECISION': 3,
    'NEW_FIELD': True,
    'FORMULA': '@row_number',
    'OUTPUT': splittedID})

# Drape Z value form raster
# Fisrt we calculate the values using the DEM
Zvalue = 'Temp/Zvalue.shp'
dem = 'Temp/mergedDEM.tif' # Merged DEM product of the RasterDataPreprocessing 
processing.run('native:setzfromraster',
    {'INPUT':splittedID,
    'BAND': 1,
    'RASTER':dem,
    'OUTPUT':Zvalue})

# Then we make create a column showing
Extracted = 'Temp/Extracted.shp'
processing.run('native:extractzvalues',
    {'INPUT': Zvalue,
    'SUMMARIES': [0, 1],
    'COLUMN_PREFIX': 'z_',
    'OUTPUT': Extracted})

# Calculate a new field that corresponds to the length of each segment
length = 'Temp/Length.shp'
processing.run('qgis:fieldcalculator', 
    {'INPUT': Extracted,
    'FIELD_NAME': 'Length',
    'FIELD_TYPE': 0,
    'FIELD_PRECISION': 3,
    'NEW_FIELD': True,
    'FORMULA': '$length',
    'OUTPUT': length})

# Calculate the slope of the pedestrian network segments in percentage, 100 percent corresponds to 45 degrees slopes
slope = 'Temp/PedestrianSlope100M.shp'
processing.run('qgis:fieldcalculator',
    {'INPUT': length,
    'FIELD_NAME': 'slope',
    'FIELD_TYPE': 0,
    'FIELD_PRECISION': 3,
    'NEW_FIELD': True,
    'FORMULA': 'abs( "z_first" - "z_last" )/"Length"',
    'OUTPUT': slope})

# Deletes all non-required fields  
layer = iface.addVectorLayer(slope, "", "ogr")
fields = layer.dataProvider().fields() # List containing all the fiels in the pedestrianroad layer

KeepList = ['z_first', 'z_last', 'Length', 'slope', 'SPLITID']
DeleteList = []
for field in fields:
    if field.name() not in KeepList:
        DeleteList.append(field.name())

temp2 = "Temp/Temp2.shp"
processing.run('qgis:deletecolumn',  # Deletes all the fields stored in DeleteList
    {'INPUT':slope,
    'COLUMN' : DeleteList,
    'OUTPUT':temp2})

FinalSlope = 'Temp/FinalSlope.shp'
processing.run('native:joinattributestable',
    {'INPUT':splittedID,
    'FIELD':'SPLITID',
    'INPUT_2':temp2,
    'FIELD_2':'SPLITID',
    'METHOD': 1,
    'OUTPUT':FinalSlope})