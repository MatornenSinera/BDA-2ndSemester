import networkx as nx 
import matplotlib.pyplot as plt

huuugeList=[]
with open('Alice In Wonderland.txt', encoding='utf8') as f:
    huuugeList=f.read().split()
    huuugeList=[word.lower() for word in huuugeList]

import re
Text=' '.join(huuugeList)
regex=r"([0-9A-Za-z\'\d]+)[\s.\":,!;]"
m=re.findall(regex, Text)
m=[word.lower() for word in m]
with open('stopwords_en.txt') as f:
	stopwords=f.read().split()
	stopwords=[word.lower() for word in stopwords]
m=[x for x in m if x not in stopwords]

### Loops above search for words that end with space or special characters: .",!;
### THen all stop words are thrown out.

Nodes=[]
DictOfEdges={}
for i in range(len(m)-1):
	if m[i] not in DictOfEdges:
		DictOfEdges[m[i]]=[]
	if m[i+1] not in DictOfEdges:
		DictOfEdges[m[i+1]]=[]
	if m[i+1] not in DictOfEdges[m[i]]:
		DictOfEdges[m[i]].append(m[i+1])
	if m[i] not in DictOfEdges[m[i+1]]:
		DictOfEdges[m[i+1]].append(m[i])

### From table m, consisting of words, we gather for every word a table of words appearing next to it, thus creating a handy dictionary.

		
SortedWords=sorted(DictOfEdges.items(), key=lambda v: len(v[1]), reverse=True)
f=open('Alice - 10 words with most degree.txt', 'w')
Edges=[]
for i in range(10):
	if i!='ll':
		f.write(SortedWords[i][0]+' '+str(len(SortedWords[i][1]))+' '+'\n')
	for j in DictOfEdges[SortedWords[i][0]]:
		Nodes.append(j)
		Edges.append((SortedWords[i][0], j))

#For every thing in dictionary of edges, we can add a node and words connected with said node.

f.close()
G=nx.Graph()
G.add_nodes_from(Nodes)
G.add_edges_from(Edges)
nx.draw(G, node_color='grey',  font_size=12, alpha=0.8, with_labels=True, arrows=True)
plt.show()
