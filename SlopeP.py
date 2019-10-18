'''
The Present Script genertes the slope for the diferent roand segments that compose the network
Author: Juan Pablo Herrera Alvarez
GIS Reality
'''

# Import libraries into python
import os 
import qgis 
import gdal

# Defines working directory
os.chdir('/users/juanpablo/OneDrive/UTS/iLab1')

# First we merge the layers with the road network and the layer with only predestrian network
layer1 = 'QGIS/Network/ClipData/Roads.shp'
layer2 = 'QGIS/Network/ClipData/Pedestrians.shp'
pedestrianroad = 'Temp/PedestrianRoad.shp'
dem = 'Temp/mergedDEM.tif'

processing.run('qgis:mergevectorlayers', #we use run because we dont want to load the layer in the canvas yet
    {'LAYERS':[layer1, layer2],
    'OUTPUT':pedestrianroad})

# After this step we proceed to delete all the fields in the layer 
layer = iface.addVectorLayer(pedestrianroad, "", "ogr")

fields = layer.dataProvider().fields()

KeepList = ['STREET']
DeleteList = []
for field in fields:
    if field.name() not in KeepList:
        DeleteList.append(field.name())

temp = "Temp/Temp.shp"
processing.run('qgis:deletecolumn', 
    {'INPUT':pedestrianroad,
    'COLUMN' : DeleteList,
    'OUTPUT':temp})

# Split lines by maximun length
splitted = 'Temp/Splitted.shp'
processing.run('native:splitlinesbylength',
    {'INPUT': temp,
    'LENGTH': 20,
    'OUTPUT': splitted})

# Drape Z value form raster
# Fisrt we calculate the values using the DEM
Zvalue = 'Temp/Zvalue.shp'
Extracted = 'Temp/Extracted.shp'
processing.run('native:setzfromraster',
    {'INPUT':splitted,
    'BAND': 1,
    'RASTER':dem,
    'OUTPUT':Zvalue})

# Then we make create a column showing
processing.run('native:extractzvalues',
    {'INPUT': Zvalue,
    'SUMMARIES': [0, 1],
    'COLUMN_PREFIX': 'z_',
    'OUTPUT': Extracted})

# Extract vertices: We are doing this in order to manually calculate the slope
#nodes = 'Temp/Nodes.shp'                            # MAYBE NOT YET I HAVE TO FIND A SOLUTION USING CODE
#processing.run('qgis:extractspecificvertices',
#    {'INPUT':Extracted,
#    'VERTICES' : '-1',
#    'OUTPUT':nodes})

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

# Calculate the slope using in percentage
slope = 'Temp/PedestrianSlope.shp'
processing.run('qgis:fieldcalculator',
    {'INPUT': length,
    'FIELD_NAME': 'slope',
    'FIELD_TYPE': 0,
    'FIELD_PRECISION': 3,
    'NEW_FIELD': True,
    'FORMULA': 'abs( "z_first" - "z_last" )/"Length"',
    'OUTPUT': slope})








