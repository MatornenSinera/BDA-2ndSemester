import pandas
import ast
import collections
import networkx as nx 
import matplotlib.pyplot as plt
import pydot
import random
import matplotlib.image as mpimg
from numpy import sqrt
import numpy as np
import time

def MaxDeletion(G, proportion):
    ListOfNodes=sorted(G.degree, key=lambda x: x[1], reverse=True)
    NumberOfNodes=G.number_of_nodes()
    Sample=round(proportion*NumberOfNodes)
    MaxSample=[x[0] for x in ListOfNodes[:Sample]]
    G.remove_nodes_from(MaxSample)
    return G

def MaxDeletionCloseness(G, proportion, Sort):
    NumberOfNodes=G.number_of_nodes()
    Sample=round(proportion*NumberOfNodes)
    MaxSample=[x[0] for x in ListOfNodes[:Sample]]
    G.remove_nodes_from(MaxSample)
    return G

def MaxDeletionBetweenness(G, proportion, Sort):
    ListOfNodes=Sort
    NumberOfNodes=G.number_of_nodes()
    Sample=round(proportion*NumberOfNodes)
    MaxSample=[x[0] for x in ListOfNodes[:Sample]]
    G.remove_nodes_from(MaxSample)
    return G

#Three functions working basically the same - given sorted dictionary of nodes, delete precise amount of them, repeated for every point on every plot.


Probabilities=[float(x) for x in np.linspace(0.001, 0.98, num=20)]
print(Probabilities)
K=[5]
Sizes=10000
GeneratedWatts=[]
#Basic Parameters

for j in range(10):
    GW=nx.watts_strogatz_graph(Sizes, 5, 0.02)
    GeneratedWatts.append(GW)
#Graph Generation

i=0
i+=1
print(i)
plt.figure(i)
Pf=[0 for i in Probabilities]
for G in GeneratedWatts:
    giant = max(nx.connected_component_subgraphs(G), key=len)
    P0=giant.size()
    k=0
    for prob in Probabilities:
        G2=MaxDeletion(G.copy(), prob)
        giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
        P1=giantreduced.size()
        Pf[k]+=float(P1/P0)
        k+=1
Pf=[i/10 for i in Pf]

f.write(str(Pf))
f.write('\n')
plt.plot(Probabilities, Pf)
plt.title('Watts, Max, Degree: <k>='+str(5))
plt.legend([Sizes])
plt.xlabel('Fraction of deleted nodes.')
plt.ylabel('P∞(f)/P∞(0)')
plt.savefig(str(i)+'.png')
##DEGREE CENTRALITY

#Figure 1 - Attack based on Degree Centrality

i+=1
print(i)
plt.figure(i)
Pf=[0 for i in Probabilities]
for G in GeneratedWatts:
    giant = max(nx.connected_component_subgraphs(G), key=len)
    P0=giant.size()
    k=0
    Sort=sorted(nx.closeness_centrality(G).items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    for prob in Probabilities:)
        G2=MaxDeletionCloseness(G.copy(), prob, Sort)
        giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
        P1=giantreduced.size()
        Pf[k]+=float(P1/P0)
        k+=1
Pf=[i/10 for i in Pf]
plt.plot(Probabilities, Pf)
plt.title('Watts, Max, Closeness: <k>='+str(5))
plt.legend([Sizes])
plt.xlabel('Fraction of deleted nodes.')
plt.ylabel('P∞(f)/P∞(0)')
plt.savefig(str(i)+'.png')

##CLOSENESS CENTRALITY

i+=1
plt.figure(i)
Pf=[0 for i in Probabilities]
for G in GeneratedWatts:
    giant = max(nx.connected_component_subgraphs(G), key=len)
    P0=giant.size()
    sort=sorted(nx.betweenness_centrality(G).items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    k=0
    for prob in Probabilities:
        G2=MaxDeletionBetweenness(G.copy(), prob, sort)
        giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
        P1=giantreduced.size()
        Pf[k]+=float(P1/P0)
        k+=1
Pf=[i/10 for i in Pf]
plt.plot(Probabilities, Pf)
plt.title('Watts, Max, Betweenness: <k>='+str(5))

f.write(str(Pf))
f.write('\n')

plt.legend([Sizes])
plt.xlabel('Fraction of deleted nodes.')
plt.ylabel('P∞(f)/P∞(0)')
plt.savefig(str(i)+'.png')


##BETWEENNESS CENTRALITY

plt.show()
