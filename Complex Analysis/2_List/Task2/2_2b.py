import pandas
import ast
import collections
import networkx as nx 
import matplotlib.pyplot as plt
import pydot
import random as rd
import numpy as np
from numba import jit
import math

def WaltzStogatz(NumNodes, Neighbours, Probability):
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
		if rd.random()<float(Probability):
			if rd.random()<0.5: ##LeftNumberChange
				flag=0
				while flag==0:
					c=i[1]
					b=rd.randint(0, len(Nodes)-1)
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
					b=rd.randint(0, len(Nodes)-1)
					if b!=c:
						if c<b:
							b,c=c,b
						if [b,c] not in Edges:
							#print("Right change: "+str(i[0])+','+str(i[1])+" -> "+str(b)+','+str(c))
							i[0]=b
							i[1]=c
							flag=1
	return [Nodes, Edges]


def ShortestPaths(Result):
	Nodes=Result[0]
	Edges=Result[1]
	G=nx.Graph()
	G.add_nodes_from(Nodes)
	G.add_edges_from(Edges)
	avgk=(sum(d for n,d in G.degree())/len(G))
	#b=nx.diameter(G)
	b=1
	c=nx.shortest_path(G)
	return [avgk, b, c]

ks=[]
d1=[]
d2=[]
another=[]
samples=np.linspace(100, 4000, num=30)
samples=[round(i) for i in samples]
for i in samples:
	sumpath=0
	lenpath=0
	flag=0
	b=0
	print(i)
	while (flag==0):
		Result=WaltzStogatz(int(i), 4, 1)
		Result2=ShortestPaths(Result)
		ks.append(Result2[0])
		maxd1=0
		for a1 in Result2[2]:
			for a2 in Result2[2][a1]:
				if len(Result2[2][a1][a2])>maxd1:
					maxd1=len(Result2[2][a1][a2])
				sumpath+=len(Result2[2][a1][a2])
				lenpath+=1
		d1.append(maxd1)
		d2.append(sumpath/lenpath)
		another.append(math.log(i)/math.log(Result2[0]))
		flag=1
#print(d2)
#print(d1)
#print(samples)
#print(another)

d1np=np.asarray(d1)
anothernp=np.asarray(another)
coefs=np.polyfit(anothernp, d1np, 1)
d3=[coefs[0]*i+coefs[1] for i in another]
plt.plot(samples, d1, samples, d2, samples, d3)
plt.xscale('log')
plt.show()
plt.plot(another, d1, another, d3, another, d2)
plt.legend(["Diameter of graph", "Fitted diameter of graph - linear regression", "Average path length"])
plt.xlabel("Ln(N)/Ln(<k>)")
plt.show()
