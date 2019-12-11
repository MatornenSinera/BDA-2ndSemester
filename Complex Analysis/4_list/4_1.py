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

def MaxDeletionCloseness(G, proportion):
    #print(G.degree)
    #print(nx.closeness_centrality(G))
    ListOfNodes=sorted(nx.closeness_centrality(G).items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    NumberOfNodes=G.number_of_nodes()
    Sample=round(proportion*NumberOfNodes)
    MaxSample=[x[0] for x in ListOfNodes[:Sample]]
    G.remove_nodes_from(MaxSample)
    return G

def MaxDeletionBetweenness(G, proportion):
    ListOfNodes=sorted(nx.betweenness_centrality(G).items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    NumberOfNodes=G.number_of_nodes()
    Sample=round(proportion*NumberOfNodes)
    MaxSample=[x[0] for x in ListOfNodes[:Sample]]
    G.remove_nodes_from(MaxSample)
    return G


f= open("datas.txt","w+")

Probabilities=[float(x) for x in np.linspace(0.001, 0.98, num=20)]
print(Probabilities)
K=[5]
Sizes=10000
GeneratedWatts=[]

f.write(str(Probabilities))
f.write('\n')
for j in range(10):
    GW=nx.watts_strogatz_graph(Sizes, 5, 0.05)
    GeneratedWatts.append(GW)

i=605
print(len(GeneratedWatts))

i+=1
print(i)
plt.figure(i)
Pf=[0 for i in Probabilities]
for G in GeneratedWatts:
    giant = max(nx.connected_component_subgraphs(G), key=len)
    P0=giant.size()
    print (P0)
    k=0
    for prob in Probabilities:
        print(prob)
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
plt.xlabel('Fraction of randomly deleted nodes.')
plt.ylabel('P∞(f)/P∞(0)')
plt.savefig(str(i)+'.png')


##DEGREE CENTRALITY


i+=1
print(i)
plt.figure(i)
Pf=[0 for i in Probabilities]
for G in GeneratedWatts:
    giant = max(nx.connected_component_subgraphs(G), key=len)
    P0=giant.size()
    print (P0)
    k=0
    for prob in Probabilities:
        print(prob)
        G2=MaxDeletionCloseness(G.copy(), prob)
        giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
        P1=giantreduced.size()
        Pf[k]+=float(P1/P0)
        k+=1
Pf=[i/10 for i in Pf]
plt.plot(Probabilities, Pf)
plt.title('Watts, Max, Closeness: <k>='+str(5))
plt.legend([Sizes])
plt.xlabel('Fraction of randomly deleted nodes.')
plt.ylabel('P∞(f)/P∞(0)')
plt.savefig(str(i)+'.png')
f.write(str(Pf))

f.write('\n')
# for GraphFamily, k in zip (GeneratedWatts, K):
#     i+=1
#     print(i)
#     plt.figure(i)
#     for G in GraphFamily:
#         giant = max(nx.connected_component_subgraphs(G), key=len)
#         P0=giant.size()
#         Pf=[]
#         print (P0)
#         for prob in Probabilities:
#             print(prob)
#             G2=MaxDeletionCloseness(G.copy(), prob)
#             giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
#             P1=giantreduced.size()
#             Pf.append(float(P1/P0))
#         plt.plot(Probabilities, Pf)
#     plt.title('Watts, Max, Closeness: <k>='+str(k))
#     plt.legend([str(i) for i in Sizes])
#     plt.xlabel('Fraction of randomly deleted nodes.')
#     plt.ylabel('P∞(f)/P∞(0)')
#     plt.savefig(str(i)+'.png')

##CLOSENESS CENTRALITY

i+=1
print(i)
plt.figure(i)
Pf=[0 for i in Probabilities]
for G in GeneratedWatts:
    giant = max(nx.connected_component_subgraphs(G), key=len)
    P0=giant.size()
    print (P0)
    k=0
    for prob in Probabilities:
        print(prob)
        G2=MaxDeletionBetweenness(G.copy(), prob)
        giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
        P1=giantreduced.size()
        Pf[k]+=float(P1/P0)
        k+=1
Pf=[i/10 for i in Pf]
plt.plot(Probabilities, Pf)
plt.title('Watts, Max, Betweenness: <k>='+str(5
    ))

f.write(str(Pf))
f.write('\n')

plt.legend([Sizes])
plt.xlabel('Fraction of randomly deleted nodes.')
plt.ylabel('P∞(f)/P∞(0)')
plt.savefig(str(i)+'.png')


# for GraphFamily, k in zip (GeneratedWatts, K):
#     i+=1
#     print(i)
#     plt.figure(i)
#     for G in GraphFamily:
#         giant = max(nx.connected_component_subgraphs(G), key=len)
#         P0=giant.size()
#         Pf=[]
#         print (P0)
#         for prob in Probabilities:
#             print(prob)
#             G2=MaxDeletionBetweenness(G.copy(), prob)
#             giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
#             P1=giantreduced.size()
#             Pf.append(float(P1/P0))
#         plt.plot(Probabilities, Pf)
#     plt.title('Watts, Max, Betweenness : <k>='+str(k))
#     plt.legend([str(i) for i in Sizes])
#     plt.xlabel('Fraction of randomly deleted nodes.')
#     plt.ylabel('P∞(f)/P∞(0)')
#     plt.savefig(str(i)+'.png')

##BETWEENNESS CENTRALITY

plt.show()

f.close()