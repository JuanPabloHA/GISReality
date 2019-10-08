# Vector data preprocessing 
# GIS Reality
# Author: Juan Pablo Herrera

# The script contains the data preprocessing corresponding to the vector data

# Libraries
import os
import qgis

# Working Directory
os.chdir('/Users/juanpablo/OneDrive/UTS/iLab1')

# Generates Study Area Outline
Input = 'QGIS/Network/ClipData/StudyArea.shp'
processing.run("native:dissolve", {'FIELD':[], 
    'INPUT': Input,
    'OUTPUT': 'Temp/Dissolved.shp'})