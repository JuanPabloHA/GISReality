# Shortest Path
# Author: Juan Pablo Herrera
# MDSI - UTS Srping 2019 
# GIS Reality

# The following code produces the results for the shortest path using the Dijkstra  and A* algorithms
# using a weighted approach

# Import libraries
import os
import networkx as nx
import matplotlib.pyplot as plt
import gdal 

# Defines working environment
os.chdir("/Users/juanpablo/OneDrive/UTS/iLab1")

# Remove all layers from map canvas
QgsProject.instance().removeAllMapLayers()

# First we generate the cost of visiting each segment two objectives with a 50 % weight each
slope = 'Temp/FinalSlope.shp' # Input layer 
cost = 'Temp/WeightedApproach.shp' # Output layer 
processing.runAndLoadResults('qgis:fieldcalculator',
    {'INPUT': slope,
    'FIELD_NAME': 'Cost',
    'FIELD_TYPE': 0,        # 0: float, 1: Integer
    'FIELD_PRECISION': 3,
    'NEW_FIELD': True,
    'FORMULA': '(0.5*("Length"/max("Length")))+(0.5 * "slope")',
    'OUTPUT': cost})

# Imports pedestrian network
PNet = nx.read_shp(cost)

# Convert PNet to undirected graph
PNet = nx.Graph(PNet)

# Dijkstra solution
Dijkstra = nx.astar_path(PNet, (9697447.814007638, 4435672.778366395),
                      (9685398.3253, 4437041.440300001), weight='Cost')
#print('Dijkstra: 'len(Dijkstra))
DPath = PNet.subgraph(Dijkstra)

DijkstraSol = [ DPath.edges[u,v]['SPLITID'] for u, v, d in DPath.edges(data=True) ]
DijkstraCost = [ DPath.edges[u,v]['Cost'] for u, v, d in DPath.edges(data=True) ]
print('Dijkstra total cost: '+str(sum(DijkstraCost)))

Dsol = 'Temp/Dsol.shp'
processing.runAndLoadResults('native:extractbyexpression', 
    {'INPUT':cost,
    'EXPRESSION': '"SPLITID" IN '+str(tuple(DijkstraSol)),
    'OUTPUT':Dsol})

# A* solution 
## Heuristic
## The difference with the Dijktra approach is that in here we are using the heuristic distance
def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

Astar = nx.astar_path(PNet, (9697447.814007638, 4435672.778366395),
                      (9685398.3253, 4437041.440300001), heuristic=dist, weight='Cost')
#print(len(Astar))
APath = PNet.subgraph(Astar)

AstarSol = [ APath.edges[u,v]['SPLITID'] for u, v, d in APath.edges(data=True) ]
AstarCost = [ APath.edges[u,v]['Cost'] for u, v, d in APath.edges(data=True) ]
print('Astar total cost: ' + str(sum(AstarCost)))

Asol = 'Temp/Asol.shp'
processing.runAndLoadResults('native:extractbyexpression', 
    {'INPUT':cost,
    'EXPRESSION': '"SPLITID" IN '+str(tuple(AstarSol)),
    'OUTPUT':Asol})
