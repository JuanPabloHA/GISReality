# Network Analysis
# Juan Pablo Herrera Alvarez
# iLab 1 - GIS Reality / UTS Startups

# Import libraries
import os
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import gdal 

# Defines working environment
print(os.getcwd())
os.chdir("/Users/juanpablo/OneDrive/UTS/iLab1/QGIS/Network/ClipData")

# Imports pedestrian network
G = nx.read_shp('Roads.shp')
G2 = nx.read_shp('Roads.shp', simplify=True)

# Convert the network to matrix format 
pNetwork = nx.to_numpy_matrix(G)
pNetwork.shape[1]

pNetwork2 = nx.to_numpy_matrix(G2)
pNetwork2.shape[1]
