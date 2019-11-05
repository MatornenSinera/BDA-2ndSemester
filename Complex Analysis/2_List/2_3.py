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

def Draw1(G):
	print("<k> = "+str(sum(d for n,d in G.degree())/len(G)))
	print(len(G))
	nx.draw_circular(G, node_color='grey',  font_size=12, alpha=0.5, with_labels=True, arrows=True)
	#plt.show()

def Draw2(G):

	degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
	degreeCount = collections.Counter(degree_sequence)
	deg, cnt = zip(*degreeCount.items())

	fig, ax = plt.subplots()
	plt.bar(deg, cnt, width=0.80, color='b')

	plt.title("Degree Histogram")
	plt.ylabel("Count")
	plt.xlabel("Degree")
	ax.set_xticks([d + 0.4 for d in deg])
	ax.set_xticklabels(deg)

	# draw graph in inset
	plt.axes([0.4, 0.4, 0.5, 0.5])
	Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
	pos = nx.spring_layout(G)
	plt.axis('off')
	nx.draw_networkx_nodes(G, pos, node_size=20)
	nx.draw_networkx_edges(G, pos, alpha=0.4)
	plt.show()

def Clustering(G):
	nx.draw_circular(G, node_color='grey',  font_size=12, alpha=0.5, with_labels=True, arrows=True)
	#print('Clustering: '+str(nx.clustering(G)))
	print('Average Clustering: '+str(nx.average_clustering(G)))

def ShortestPaths(G):
	#print('ShortestPaths: ')
	#[print(n) for n in nx.all_pairs_shortest_path(G)]
	print('Diameter: '+str(nx.diameter(G)))
	print('Average path length: '+str(nx.average_shortest_path_length(G)))
	
Nodes=[]
Edges=[]
f=open("facebook_combined.txt", 'r')
for x in f:
	z=x[:-1].split(' ')
	for i in z:
		if i not in Nodes:
			Nodes.append(i)
	Edges.append([z[0], z[1]])

G=nx.Graph()
G.add_nodes_from(Nodes)
G.add_edges_from(Edges)
Draw1(G)
Clustering(G)
ShortestPaths(G)
Draw2(G)