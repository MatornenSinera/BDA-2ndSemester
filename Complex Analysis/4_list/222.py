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

G=nx.watts_strogatz_graph(1000, 2, 0.002)
closeness=nx.betweenness_centrality(G)
print(closeness)