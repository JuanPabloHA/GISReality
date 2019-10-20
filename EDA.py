# Exploratory Data Analysis 
# Author: Juan Pablo Herrera
# MDSI - UTS Srping 2019 
# GIS Reality

# The following code produces some of the values used for the exploratory data analysis
## Requires vector and raster data preporcessing to be completed first

# Libraries
import os 
import networkx as nx
import gdal 
import matplotlib.pyplot as plt 

# Working directory
os.chdir('/Users/juanpablo/OneDrive/UTS/iLab1')

# Imports FinalPedestrianRoad into using NetworkX
G = 'Temp/FinalPedestrianRoad.shp'
PNet = nx.read_shp(G)

# Convert PNet to undirected graph
PNet = nx.Graph(PNet)

# Simple EDA
## Number of nodes and number of edges
NNodes = len(PNet.nodes()) # number of nodes
NEdges = len(PNet.edges()) # number of edges

print('Total number of nodes before splitting: ' + str(NNodes))
print('Total number of edges before splitting: ' + str(NEdges))

# Maximun and Minimun elvation of the network
## Load FinalSlope
FinalSlope = 'Temp/FinalSlope.shp'
G = nx.read_shp(FinalSlope)

# Elevation profile
# Elevation = [G.edges[u,v]['z_last'] for u, v, d in G.edges(data=True)]
# plt.title("Network's Road Elevation")
# plt.hist(Elevation, normed=True, bins=100)
# plt.show()

# Slope Profile
Slope = [G.edges[u,v]['slope'] for u, v, d in G.edges(data=True)]
Slope = [x for x in Slope if x <= 1]
plt.title("Network's Road Slope")
plt.hist(Slope, normed=True, bins=100)
plt.show()