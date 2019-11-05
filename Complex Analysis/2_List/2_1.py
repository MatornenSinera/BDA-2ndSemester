import pandas
import ast
import collections
import networkx as nx 
import matplotlib.pyplot as plt
import pydot
import random as rd

def ErdosRewyi(NumNodes, NumEdges):
	Nodes=[i for i in range(NumNodes)]
	Edges=[]

	while len(Edges)<NumEdges:
		l1=rd.randint(0, NumNodes-1)
		l2=rd.randint(0, NumNodes-1)
		if l2<l1:
			l1,l2=l2,l1
		if l1!=l2 and (l1, l2) not in Edges:
			Edges.append([l1,l2])
	return [Nodes, Edges] 



def Gilbert(NumNodes, Probability):
	Nodes=[i for i in range(NumNodes)]
	Edges=[]
	for l1 in range(len(Nodes)):
		for l2 in range(l1, len(Nodes)):
			if l1!=l2 and rd.random()<float(Probability):
				Edges.append([l1,l2])
	return [Nodes,Edges]

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

def Draw1(Result):
	Nodes=Result[0]
	Edges=Result[1]
	G=nx.Graph()
	G.add_nodes_from(Nodes)
	G.add_edges_from(Edges)
	print("<k> = "+str(sum(d for n,d in G.degree())/len(G)))
	print(len(G))
	nx.draw_circular(G, node_color='grey',  font_size=12, alpha=0.5, with_labels=True, arrows=True)
	#plt.show()

def Clustering(Result):
	Nodes=Result[0]
	Edges=Result[1]
	G=nx.Graph()
	G.add_nodes_from(Nodes)
	G.add_edges_from(Edges)
	nx.draw_circular(G, node_color='grey',  font_size=12, alpha=0.5, with_labels=True, arrows=True)
	print('Clustering: '+str(nx.clustering(G)))
	print('Average Clustering: '+str(nx.average_clustering(G)))

def Draw2(Result):
	Nodes=Result[0]
	Edges=Result[1]
	G=nx.Graph()
	G.add_nodes_from(Nodes)
	G.add_edges_from(Edges)

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


def ShortestPaths(Result):
	Nodes=Result[0]
	Edges=Result[1]
	G=nx.Graph()
	G.add_nodes_from(Nodes)
	G.add_edges_from(Edges)
	print('ShortestPaths: ')
	[print(n) for n in nx.all_pairs_shortest_path(G)]
	print('Diameter: '+str(nx.diameter(G)))
	print('Average path length: '+str(nx.average_shortest_path_length(G)))
	



Result=ErdosRewyi(10, 15)
Draw1(Result)
Clustering(Result)
ShortestPaths(Result)
Draw2(Result)


#print(len(Result[1]))
Result=Gilbert(10, 0.66)
Draw1(Result)
Clustering(Result)
ShortestPaths(Result)
Draw2(Result)

#print(len(Result[1]))

Draw1(Result)
Clustering(Result)
ShortestPaths(Result)
Draw2(Result)
#print(len(Result[1]))



