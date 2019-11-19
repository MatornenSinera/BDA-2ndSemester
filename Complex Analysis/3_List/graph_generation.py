import pandas
import ast
import collections
import networkx as nx 
import matplotlib.pyplot as plt
import pydot
import random
import matplotlib.image as mpimg
from numpy import sqrt
import time

start = time.time()

def Degree(G):
    print("<k> = "+str(sum(d for n,d in G.degree())/len(G)))

Sizes=[1000, 10000, 100000, 200000]
GeneratedBarabasi=[[] for i in range(3)]
GeneratedGilbert=[[] for i in range(3)]
GeneratedWatts=[[] for i in range(3)]
K=[4,10,20]
#k==4
for i in Sizes:
    GB=nx.barabasi_albert_graph(i, 2)
    GeneratedBarabasi[0].append(GB)
    Degree(GB)
    start1=time.time()
    GG=nx.gnp_random_graph(i, float(4/i))
    GeneratedGilbert[0].append(GG)
    end1=time.time()
    print(end1-start1)
    Degree(GG)
    GW=nx.watts_strogatz_graph(i, 4, 0.01)
    GeneratedWatts[0].append(GW)
    Degree(GW)
    print(i)


#k==10
for i in Sizes:
    GB=nx.barabasi_albert_graph(i, 5)
    GeneratedBarabasi[1].append(GB)
    Degree(GB)
    start1=time.time()
    GG=nx.gnp_random_graph(i, float(10/i))
    GeneratedGilbert[1].append(GG)
    end1=time.time()
    print(end1-start1)
    Degree(GG)
    GW=nx.watts_strogatz_graph(i, 10, 0.01)
    GeneratedWatts[1].append(GW)
    Degree(GW)
    print(i)
#k==20
for i in Sizes:
    GB=nx.barabasi_albert_graph(i, 10)
    GeneratedBarabasi[2].append(GB)
    Degree(GB)
    start1=time.time()
    GG=nx.gnp_random_graph(i, float(20/i))
    GeneratedGilbert[2].append(GG)
    Degree(GG)
    end1=time.time()
    print(end1-start1)
    print(i)
    GW=nx.watts_strogatz_graph(i, 20, 0.01)
    GeneratedWatts[2].append(GW)
    Degree(GW)
    

for GraphFamily, k in zip(GeneratedBarabasi, K):
    for G, size in zip(GraphFamily, Sizes):
        nx.write_gml(G, "Barabasi_"+str(k)+"_"+str(size)+".gml")
for GraphFamily, k in zip(GeneratedGilbert, K):
    for G, size in zip(GraphFamily, Sizes):
        nx.write_gml(G, "Gilbert_"+str(k)+"_"+str(size)+".gml")
for GraphFamily, k in zip(GeneratedWatts, K):
    for G, size in zip(GraphFamily, Sizes):
        nx.write_gml(G, "Watts_"+str(k)+"_"+str(size)+".gml")
end=time.time()
print(end-start)

# for k in K:
#     for size in Sizes:
#         start1=time.time()
#         H=nx.read_gml("Barabasi_"+str(k)+"_"+str(size)+".gml")
#         Degree(H)
#         H=nx.read_gml("Gilbert_"+str(k)+"_"+str(size)+".gml")
#         Degree(H)
#         H=nx.read_gml("Watts_"+str(k)+"_"+str(size)+".gml")
#         Degree(H)
#         end1=time.time()
#         print(end1-start1)
# now=time.time()
# print(now-end)