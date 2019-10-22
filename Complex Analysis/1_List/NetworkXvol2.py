import pandas
import ast
import networkx as nx 
import matplotlib.pyplot as plt
import pydot

Nodes=[]
DictOfEdges={}


DictionaryOfNames={} 
DictionaryOfEdges={}

RowList=[]

###TODO-EDGES

KT = pandas.read_csv('ph_emps_scopus.csv', header=0)
CS = pandas.read_csv('cs_emps_scopus.csv', header=0)
for index, rows in KT.iterrows():
	Row=[rows[0], rows[1], rows[2], rows[3], rows[4]]
	#print(Row)
	Key=rows[1][0]+'. '+rows[2]
	Key=Key
	DictionaryOfNames[rows[3]]=Key
	if Key not in DictionaryOfEdges:
		DictionaryOfEdges[Key]=[]
	if rows[4]!='None':
		List = ast.literal_eval(rows[4])
		for i in List:
			for j in i:
				if j!=rows[3] and j not in DictionaryOfEdges[Key]:
					DictionaryOfEdges[Key].append(j)
	Nodes.append(Key)
	
for index, rows in CS.iterrows():
	Row=[rows[0], rows[1], rows[2], rows[3], rows[4]]
	#print(Row)
	Key=rows[1][0]+'. '+rows[2]
	DictionaryOfNames[rows[3]]=Key
	if Key not in DictionaryOfEdges:
		DictionaryOfEdges[Key]=[]
	if rows[4]!='None':
		List = ast.literal_eval(rows[4])
		for i in List:
			for j in i:
				if j!=rows[3] and j not in DictionaryOfEdges[Key]:
					DictionaryOfEdges[Key].append(j)
	Nodes.append(Key)

#print(DictionaryOfNames)
#print(DictionaryOfEdges)
Edges=[]
for i in DictionaryOfEdges:
	#print(i)
	for j in DictionaryOfEdges[i]:
		#print(i, j)
		if j in DictionaryOfNames:
			Edges.append((i, DictionaryOfNames[j]))

#print(Nodes)

G=nx.Graph()

G.add_nodes_from(Nodes)
G.add_edges_from(Edges)

for i in Edges:
	print(i)

nx.draw_circular(G, node_color='grey',  font_size=12, alpha=0.5, with_labels=True, arrows=True)
A=nx.nx_pydot.to_pydot(G)
A.write_png('lul.png')
plt.show()
