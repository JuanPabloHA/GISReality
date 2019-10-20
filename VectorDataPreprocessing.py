# Vector data preprocessing 
# Author: Juan Pablo Herrera
# MDSI - UTS Srping 2019 
# GIS Reality

# The script contains the data preprocessing corresponding to the vector data

# Libraries
import os
import qgis

# Working directory
os.chdir('/Users/juanpablo/OneDrive/UTS/iLab1')

# Generates Study Area Outline
Input = 'QGIS/Network/ClipData/StudyArea.shp'
processing.run("native:dissolve", {'FIELD':[], 
    'INPUT': Input,
    'OUTPUT': 'Temp/Dissolved.shp'})

# Merges the layers with the road network and the layer with only predestrian network
layer1 = 'QGIS/Network/ClipData/Roads.shp'
layer2 = 'QGIS/Network/ClipData/Pedestrians.shp'
pedestrianroad = 'Temp/PedestrianRoad.shp'

processing.run('qgis:mergevectorlayers', #we use run because we dont want to load the layer in the canvas yet
    {'LAYERS':[layer1, layer2],
    'OUTPUT':pedestrianroad})

# Deletes all non-required fields  
layer = iface.addVectorLayer(pedestrianroad, "", "ogr")
fields = layer.dataProvider().fields() # List containing all the fiels in the pedestrianroad layer

KeepList = ['STREET', 'STREET_TYPE', 'STREET_LAB', 'START_NODE', 'END_NODE', # List containing the fields to keep
    'DRIVE_TIME', 'WALK_TIME', 'SPEED', 'ROUTE_CLASS']
DeleteList = []
for field in fields:
    if field.name() not in KeepList:
        DeleteList.append(field.name())

temp = "Temp/Temp.shp"
processing.run('qgis:deletecolumn',  # Deletes all the fields stored in DeleteList
    {'INPUT':pedestrianroad,
    'COLUMN' : DeleteList,
    'OUTPUT':temp})

# Removes pedestrianroad from map canvas
QgsProject.instance().removeAllMapLayers()

# Generate a new OBJECTID 
FPRoadTemp = 'Temp/FPRoadTemp.shp'
processing.run('qgis:fieldcalculator',
    {'INPUT': temp,
    'FIELD_NAME': 'OBJECTID',
    'FIELD_TYPE': 1,                    # 0: Float, 1: Intger, 2: String, 3: DAte 
    'FIELD_PRECISION': 3,
    'NEW_FIELD': True,
    'FORMULA': '@row_number',
    'OUTPUT': FPRoadTemp})

# Generate segment lenght
FinalPedestrianRoad = 'Temp/FinalPedestrianRoad.shp'
processing.run('qgis:fieldcalculator',
    {'INPUT': FPRoadTemp,
    'FIELD_NAME': 'LenghtKM',
    'FIELD_TYPE': 0,                    # 0: Float, 1: Intger, 2: String, 3: DAte 
    'FIELD_PRECISION': 3,
    'NEW_FIELD': True,
    'FORMULA': '$length  / 1000',
    'OUTPUT': FinalPedestrianRoad})