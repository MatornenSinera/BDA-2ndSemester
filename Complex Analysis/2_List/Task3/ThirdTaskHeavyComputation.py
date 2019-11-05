import pandas
import ast
import collections
import networkx as nx 
import matplotlib.pyplot as plt
import pydot
import random as rd
import matplotlib.image as mpimg
from numpy import sqrt
from scipy.stats import norm

def ShortestPaths(G):
	c=nx.shortest_path(G)
	lengths={}
	for a1 in c:
		#print(a1)
		for a2 in c[a1]:
			if (len(c[a1][a2])) not in lengths:
				lengths[len(c[a1][a2])]=1
			else:
				lengths[len(c[a1][a2])]+=1
	x=[]
	y=[]
	for i in lengths:
		x.append(i)
		y.append(lengths[i])
	y2=[]
	for i in y:
		y2.append(i/sum(y))
	plt.bar(x, y)
	plt.show()
	plt.bar(x, y2)
	plt.show()



G=nx.barabasi_albert_graph(10000, 6)

def Distribution(G):
    Degrees = []
    Probabilities = []
    Distrs = {}
    for i in G.nodes():
        Distrs.setdefault(len(list(G.neighbors(i))), 0)
        Distrs[len(list(G.neighbors(i)))] += 1
    cnt = sum(Distrs.values())
    Degrees = [i for i in Distrs.keys()]
    Probabilities = [Distrs[i]/cnt for i in Degrees]
    return Degrees, Probabilities

def Distribution2(G):
    counts = []
    for node in G.nodes():
        connections = 0
        set_of_neighbors = set(G.neighbors(node))
        
        for neighbor in set_of_neighbors:
            for neighbor_of_neighbor in G.neighbors(neighbor):
                if neighbor_of_neighbor in set_of_neighbors:
                    connections += 1

        counts.append([connections, len(set_of_neighbors)])
    
    coefficients_counts = {}
    for item in counts:
        if item[1] == 1:
            coefficients_counts.setdefault(0, 0)
            coefficients_counts[0] += 1
            continue
        if item[1]!=0:
            c = item[0]/(item[1]*(item[1]-1))
            coefficients_counts.setdefault(c, 0)
            coefficients_counts[c] += 1

    return coefficients_counts


def Degree(G):
    print(len(G))
    d, p = Distribution(G)
    plt.bar(d, p)
    plt.show()

def Cluster(G):



    print(len(G))
    from more_itertools import sort_together
    d = Distribution2(G)
    x = [item[0] for item in d.items()]
    y = [item[1] for item in d.items()]
    sum_y = sum(y)
    y_d = [i/sum_y for i in y]
    x, y_d = sort_together([x,y_d])
    c_results=([x, y, y_d])
    plt.plot(c_results[0], c_results[2], 'bo')
    plt.show()
    plt.hist(c_results[0], density=True)
    plt.show()


Degree(G)
ShortestPaths(G)
Cluster(G)

