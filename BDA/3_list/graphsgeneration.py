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
import random

V=[]
for i in range(25):
	for j in range(i, 25):
		if i!=j and random.random()<0.3:
			V.append([i+1, j+1])

print(V)
print(len(V))

