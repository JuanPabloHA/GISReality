#Learinig Material 

import networkx as nx
import matplotlib.pyplot as plt
import nxviz as nv
from nxviz import MatrixPlot

G = nx.erdos_renyi_graph(n=20, p=0.2)

## Quick draw of G
nx.draw(G, with_labels = True)
plt.show()

# Graph properties 
G.nodes()

len(G.edges())
len(G.nodes())

## Degree centrality and betweenne centrality
nx.degree_centrality(G) # Returns a dictionary 
plt.hist(list(nx.degree_centrality(G).values()))
plt.show()

nx.betweenness_centrality(G)
plt.hist(list(nx.betweenness_centrality(G).values()))
plt.show()

# Visualizatio
largest_ccs = sorted(nx.connected_component_subgraphs(G), key=lambda x: len(x))[-1]
h = MatrixPlot(graph=G)
h.draw()
plt.show()
nx.degree(G)

nx.draw(G, with_labels  = True)
plt.show()


