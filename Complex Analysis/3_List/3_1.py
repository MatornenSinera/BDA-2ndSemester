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

def Gilbert(NumNodes, Probability):
    Nodes=[i for i in range(NumNodes)]
    Edges=[]
    for l1 in range(len(Nodes)):
        for l2 in range(l1, len(Nodes)):
            if l1!=l2 and random.random()<float(Probability):
                Edges.append([l1,l2])
    G=nx.Graph()
    G.add_nodes_from(Nodes)
    G.add_edges_from(Edges)           
    return G


def WattsStrogatz(NumNodes, Neighbours, Probability):
    Nodes=[i for i in range(NumNodes)]
    Edges=[]
    for index in range(len(Nodes)):
        for i in range(1, int(Neighbours/2+1)):
            Neighbour=Nodes[(index+i)%len(Nodes)]
            if Nodes[index]<Nodes[Neighbour]:
                Edges.append([Nodes[index], Nodes[Neighbour]])
            else:
                Edges.append([Nodes[Neighbour], Nodes[index]])
    for i in Edges:
        if random.random()<float(Probability):
            if random.random()<0.5: ##LeftNumberChange
                flag=0
                while flag==0:
                    c=i[1]
                    b=random.randint(0, len(Nodes)-1)
                    if b!=c:
                        if c<b:
                            b,c=c,b
                        if [b,c] not in Edges:
                            #print("Left change: "+str(i[0])+','+str(i[1])+" -> "+str(b)+','+str(c))
                            i[0]=b
                            i[1]=c
                            flag=1
            else:
                flag=0
                while flag==0:
                    c=i[0]
                    b=random.randint(0, len(Nodes)-1)
                    if b!=c:
                        if c<b:
                            b,c=c,b
                        if [b,c] not in Edges:
                            #print("Right change: "+str(i[0])+','+str(i[1])+" -> "+str(b)+','+str(c))
                            i[0]=b
                            i[1]=c
                            flag=1
    G=nx.Graph()
    G.add_nodes_from(Nodes)
    G.add_edges_from(Edges)           
    return G

def Degree(G):
    print("<k> = "+str(sum(d for n,d in G.degree())/len(G)))

def RandomDeletion(G, proportion):
    ListOfNodes=G.nodes()
    NumberOfNodes=G.number_of_nodes()
    Sample=round(proportion*NumberOfNodes)
    RandomSample=random.sample(ListOfNodes, Sample)
    G.remove_nodes_from(RandomSample)
    return G

def MaxDeletion(G, proportion):
    ListOfNodes=sorted(G.degree, key=lambda x: x[1], reverse=True)
    NumberOfNodes=G.number_of_nodes()
    Sample=round(proportion*NumberOfNodes)
    MaxSample=[x[0] for x in ListOfNodes[:Sample]]
    # print(ListOfNodes[:Sample])
    # print(MaxSample)
    G.remove_nodes_from(MaxSample)
    return G

# G1=nx.barabasi_albert_graph(1000, 2)
# G2=Gilbert(1000, 0.01)
# G3=WattsStrogatz(1000, 4, 0.01)

# G1=nx.barabasi_albert_graph(1000, 2)
# G2=Gilbert(1000, 0.01)
# G3=WattsStrogatz(1000, 4, 0.01)
Probabilities=[float(x) for x in np.logspace(-2, -0.02, num=15)]
K=[4,10,20]
Sizes=[1000, 10000, 100000, 200000]
#Sizes=[1000, 10000]
GeneratedBarabasi=[[] for i in range(len(K))]
GeneratedGilbert=[[] for i in range(len(K))]
GeneratedWatts=[[] for i in range(len(K))]

# #k==4
# for i in Sizes:
#     GB=nx.barabasi_albert_graph(i, 2)
#     GeneratedBarabasi[0].append(GB)
#     Degree(GB)
#     # GG=nx.gnp_random_graph(i, float(4/i))
#     # GeneratedGilbert[0].append(GG)
#     # Degree(GG)
#     # GW=nx.watts_strogatz_graph(i, 4, 0.01)
#     # GeneratedWatts[0].append(GW)
#     # Degree(GW)
#     print(i)
    
# #k==10
# for i in Sizes:
#     GB=nx.barabasi_albert_graph(i, 5)
#     GeneratedBarabasi[1].append(GB)
#     Degree(GB)
#     # GG=nx.gnp_random_graph(i, float(10/i))
#     # GeneratedGilbert[1].append(GG)
#     # Degree(GG)
#     # GW=WattsStrogatz(i, 10, 0.01)
#     # GeneratedWatts[1].append(GW)
#     # Degree(GW)
#     print(i)
# #k==20
# for i in Sizes:
#     GB=nx.barabasi_albert_graph(i, 10)
#     GeneratedBarabasi[2].append(GB)
#     Degree(GB)
#     # GG=nx.gnp_random_graph(i, float(20/i))
#     # GeneratedGilbert[2].append(GG)
#     # Degree(GG)
#     # GW=nx.watts_strogatz_graph(i, 20, 0.01)
#     # GeneratedWatts[2].append(GW)
#     # Degree(GW)
#     print(i)



for k, i in zip(K, range(len(K))):
    for size in Sizes:
        print("Loading: "+str(k)+" "+str(size))
        H=nx.read_gml("Watts_"+str(k)+"_"+str(size)+".gml")
        GeneratedWatts[i].append(H)

i=19

# for GraphFamily, k in zip(GeneratedBarabasi, K):
#     i+=1
#     start=time.time()
#     print(i)
    
#     plt.figure(i)
#     for G in GraphFamily:
#         giant = max(nx.connected_component_subgraphs(G), key=len)
#         P0=giant.size()
#         Pf=[]
#         print (P0)
#         for prob in Probabilities:
#             G2=RandomDeletion(G.copy(), prob)
#             giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
#             P1=giantreduced.size()
#             Pf.append(float(P1/P0))
#         plt.loglog(Probabilities, Pf)
#     plt.title('Barabasi, Random: <k>='+str(k))
#     plt.legend([str(i) for i in Sizes])
#     plt.xlabel('Fraction of randomly deleted nodes.')
#     plt.ylabel('P∞(f)/P∞(0)')
#     print(time.time() - start)
#     plt.savefig(str(i)+'.png')
 

# for GraphFamily, k in zip (GeneratedGilbert, K):
#     i+=1
#     start=time.time()
#     print(i)
#     plt.figure(i)
#     for G in GraphFamily:
#         giant = max(nx.connected_component_subgraphs(G), key=len)
#         P0=giant.size()
#         Pf=[]
#         print (P0)
#         for prob in Probabilities:
#             G2=RandomDeletion(G.copy(), prob)
#             giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
#             P1=giantreduced.size()
#             Pf.append(float(P1/P0))
#         plt.loglog(Probabilities, Pf)
#     plt.title('Gilbert, Random: <k>='+str(k))
#     plt.legend([str(i) for i in Sizes])
#     plt.xlabel('Fraction of randomly deleted nodes.')
#     plt.ylabel('P∞(f)/P∞(0)')
#     print(time.time() - start)
#     plt.savefig(str(i)+'.png')


for GraphFamily, k in zip (GeneratedWatts, K):
    i+=1
    start=time.time()
    print(i)
    plt.figure(i)
    for G in GraphFamily:
        giant = max(nx.connected_component_subgraphs(G), key=len)
        P0=giant.size()
        Pf=[]
        print (P0)
        for prob in Probabilities:
            G2=RandomDeletion(G.copy(), prob)
            giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
            P1=giantreduced.size()
            Pf.append(float(P1/P0))
        plt.loglog(Probabilities, Pf)
    plt.title('Watts, Random: <k>='+str(k))
    plt.legend([str(i) for i in Sizes])
    plt.xlabel('Fraction of randomly deleted nodes.')
    plt.ylabel('P∞(f)/P∞(0)')
    print(time.time() - start)
    plt.savefig(str(i)+'.png')

# for GraphFamily, k in zip(GeneratedBarabasi, K):
#     i+=1
#     start=time.time()
#     print(i)
    
#     plt.figure(i)
#     for G in GraphFamily:
#         giant = max(nx.connected_component_subgraphs(G), key=len)
#         P0=giant.size()
#         Pf=[]
#         print (P0)
#         for prob in Probabilities:
#             G2=MaxDeletion(G.copy(), prob)
#             giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
#             P1=giantreduced.size()
#             Pf.append(float(P1/P0))
#         plt.loglog(Probabilities, Pf)
#     plt.title('Barabasi, Max: <k>='+str(k))
#     plt.legend([str(i) for i in Sizes])
#     plt.xlabel('Fraction of randomly deleted nodes.')
#     plt.ylabel('P∞(f)/P∞(0)')
#     print(time.time() - start)
#     plt.savefig(str(i)+'.png')
 

# for GraphFamily, k in zip (GeneratedGilbert, K):
#     i+=1
#     start=time.time()
#     print(i)
#     plt.figure(i)
#     for G in GraphFamily:
#         giant = max(nx.connected_component_subgraphs(G), key=len)
#         P0=giant.size()
#         Pf=[]
#         print (P0)
#         for prob in Probabilities:
#             G2=MaxDeletion(G.copy(), prob)
#             giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
#             P1=giantreduced.size()
#             Pf.append(float(P1/P0))
#         plt.loglog(Probabilities, Pf)
#     plt.title('Gilbert, Max: <k>='+str(k))
#     plt.legend([str(i) for i in Sizes])
#     plt.xlabel('Fraction of randomly deleted nodes.')
#     plt.ylabel('P∞(f)/P∞(0)')
#     print(time.time() - start)
#     plt.savefig(str(i)+'.png')


for GraphFamily, k in zip (GeneratedWatts, K):
    i+=1
    start=time.time()
    print(i)
    plt.figure(i)
    for G in GraphFamily:
        giant = max(nx.connected_component_subgraphs(G), key=len)
        P0=giant.size()
        Pf=[]
        print (P0)
        for prob in Probabilities:
            G2=MaxDeletion(G.copy(), prob)
            giantreduced=max(nx.connected_component_subgraphs(G2), key=len)
            P1=giantreduced.size()
            Pf.append(float(P1/P0))
        plt.loglog(Probabilities, Pf)
    plt.title('Watts, Max: <k>='+str(k))
    plt.legend([str(i) for i in Sizes])
    plt.xlabel('Fraction of randomly deleted nodes.')
    plt.ylabel('P∞(f)/P∞(0)')
    print(time.time() - start)
    plt.savefig(str(i)+'.png')
plt.show()

####
# print (GeneratedBarabasi)
# for GraphFamily in GeneratedBarabasi:
#     for G in GraphFamily:
#         giant = max(nx.connected_component_subgraphs(G), key=len)
#         P0=giant.size()
#         Pf=[]
#         print (P0)
#         for prob in Probabilities:
#             G2=Maxeletion(G, prob)
#             giantreduced=max(nx.connected_component_subgraphs(G), key=len)
#             P1=giantreduced.size()
#             Pf.append(float(P1/P0))
#         plt.plot(Probabilities, Pf)
#     plt.show()

# for GraphFamily in GeneratedGilbert:
#     for G in GraphFamily:
#         giant = max(nx.connected_component_subgraphs(G), key=len)
#         P0=giant.size()
#         Pf=[]
#         print (P0)
#         for prob in Probabilities:
#             G2=MaxDeletion(G, prob)
#             giantreduced=max(nx.connected_component_subgraphs(G), key=len)
#             P1=giantreduced.size()
#             Pf.append(float(P1/P0))
#         plt.plot(Probabilities, Pf)
#     plt.show()

# for GraphFamily in GeneratedWatts:
#     for G in GraphFamily:
#         giant = max(nx.connected_component_subgraphs(G), key=len)
#         P0=giant.size()
#         Pf=[]
#         print (P0)
#         for prob in Probabilities:
#             G2=MaxDeletion(G, prob)
#             giantreduced=max(nx.connected_component_subgraphs(G), key=len)
#             P1=giantreduced.size()
#             Pf.append(float(P1/P0))
#         plt.plot(Probabilities, Pf)
#     plt.show()
