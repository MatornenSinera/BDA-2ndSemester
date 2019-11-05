import pandas
import ast
import collections
import networkx as nx 
import matplotlib.pyplot as plt
import pydot
import random as rd
import numpy as np
from numba import jit

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

def Zadanie2(Result):
	Nodes=Result[0]
	Edges=Result[1]
	G=nx.Graph()
	G.add_nodes_from(Nodes)
	G.add_edges_from(Edges)
	return [nx.shortest_path(G), nx.average_clustering(G)]

Result=WaltzStogatz(1000, 4, 0)
Result2=Zadanie2(Result)
d0=Result2[1]
sumpath=0
lenpath=0
for a1 in Result2[0]:
	for a2 in Result2[0][a1]:
		sumpath+=len(Result2[0][a1][a2])
		lenpath+=1
C0=sumpath/lenpath



samples=np.logspace(-4, 0, num=50)
print (samples)

Clusters=[]
Distances=[]
for i in samples:
	sumpath=0
	lenpath=0
	flag=0
	print(i)
	b=0
	while (flag==0):
		try:
			Result=WaltzStogatz(1000, 4, i)
			Result2=Zadanie2(Result)
			#Clusters.append(Result2[0]/C0)
			Distances.append(Result2[1]/d0)
			flag=1
			for a1 in Result2[0]:
				for a2 in Result2[0][a1]:
					sumpath+=len(Result2[0][a1][a2])
					lenpath+=1
			Clusters.append((sumpath/lenpath)/C0)
		except:
			print("Dangit: "+str(b))
			b+=1
			flag=0

plt.plot(samples, Clusters, samples, Distances)
plt.xscale('log')
plt.show()