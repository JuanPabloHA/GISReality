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
PNet = nx.read_shp('Roads.shp')

# Network properties
type(PNet)

# Convert PNet to undirected graph
PNet2 = nx.Graph(PNet)

type(PNet2)

len(PNet2.nodes())
len(PNet2.edges())

edge_Leng = nx.get_edge_attributes(PNet2, "Shape_Leng")
edge_Leng
for n1, n2, d in PNet2.edges(data=True):
    for att in att_list:
        if att in d:
            del d[att]

list(PNet2.edges(data=True))[-1]

### PART 1 A star
Astar = nx.astar_path(PNet2, (9678908.590599999, 4438590.548900001), (9685398.3253, 4437041.440300001))
Astar

###




