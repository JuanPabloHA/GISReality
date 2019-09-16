# Network Analysis
# Juan Pablo Herrera Alvarez
# iLab 1 - GIS Reality / UTS Startups

# Import libraries
import os
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from nxviz import ArcPlot, CircosPlot
import gdal 

# Defines working environment
print(os.getcwd())
os.chdir("/Users/juanpablo/OneDrive/UTS/iLab1/QGIS/Network/ClipData")

# Imports pedestrian network
PNet = nx.read_shp('Roads.shp')

# Convert PNet to undirected graph
PNet = nx.Graph(PNet)

# Network properties
type(PNet)

len(PNet.nodes()) # number of nodes
len(PNet.edges()) # number of edges

### PART 1 A-star algorithm
# Heuristic
def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


Astar = nx.astar_path(PNet, (9678908.590599999, 4438590.548900001),
                      (9685398.3253, 4437041.440300001), weight='Shape_Leng')
len(Astar)

# Plots the results of the A* algorithm 
APath = PNet.subgraph(Astar)
nx.draw(APath)
plt.show()

PNet.edges(data=True)
