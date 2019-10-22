import networkx as nx 
import matplotlib.pyplot as plt


H = nx.read_gml('karate.gml', label='id')

nx.draw(H, node_color='grey',  font_size=12, alpha=0.8, with_labels=True, arrows=True)
plt.show()

print(len(nodes))