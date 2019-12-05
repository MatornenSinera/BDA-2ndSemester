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

Nodes=[]
Edges=[]
f=open("web-Stanford.txt", 'r')
for x in f:
	z=x[:-1].split('\t')
	for i in z:
		if i not in Nodes:
			Nodes.append(i)
	Edges.append([z[0], z[1]])

print('done')
output=[]
dicin={}
dicout={}

imax=len(Edges)
print(imax)
i=0

for edge in Egdes:
	if i%1000==0:
		print(i/imax)
	if edge[0] not in dicin:
		dicin[edge[0]]=[]
	dicin[edge[0]].append(edge[1])
	if edge[1] not in dicout:
		dicout[edge[1]]=[]
	dicout[edge[1]].append(edge[0])
print(dicin[1])
print(dicout[1])




