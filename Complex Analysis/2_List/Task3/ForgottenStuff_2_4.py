import pandas
import ast
import collections
import networkx as nx 
import matplotlib.pyplot as plt
import pydot
import random as rd
import matplotlib.image as mpimg
from numpy import sqrt

img=mpimg.imread('dci.PNG')
imgc=mpimg.imread('dci2.PNG')
imgg =mpimg.imread('good.PNG')
imgb =mpimg.imread('bad.PNG')
G=nx.barabasi_albert_graph(200, 2)


pos=nx.spring_layout(G,k=3/sqrt(3))
# draw with images on nodes
nx.draw_networkx(G,pos)
ax=plt.gca()
fig=plt.gcf()
trans = ax.transData.transform
trans2 = fig.transFigure.inverted().transform
imsize = 0.06 # this is the image size
for n in G.nodes():
    (x,y) = pos[n]
    xx,yy = trans((x,y)) # figure coordinates
    xa,ya = trans2((xx,yy)) # axes coordinates
    a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize ])
    a.imshow(img)
    a.set_aspect('equal')
    a.axis('off')
plt.show()

G=nx.barabasi_albert_graph(100, 2)
pos=nx.spring_layout(G,k=3/sqrt(3))
# draw with images on nodes
imsize = 0.06
nx.draw_networkx(G,pos, nodesize=1)
for n in G.nodes():

    (x,y) = pos[n]
    xx,yy = trans((x,y)) # figure coordinates
    xa,ya = trans2((xx,yy)) # axes coordinates
    a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize])
    if G.degree()[n]%2==0:
        a.imshow(imgg)
    else:
        a.imshow(imgb)  
    a.set_aspect('equal')
    a.axis('off')
plt.show()


G=nx.barabasi_albert_graph(70, 2)
pos=nx.spring_layout(G,k=3/sqrt(3))
# draw with images on nodes
imsizemax= 0.10
maxdeg=max([G.degree()[n] for n in G.nodes()])
print(maxdeg)
nx.draw_networkx(G,pos, nodesize=1)
for n in G.nodes():
    imsize=((G.degree()[n]/maxdeg)*imsizemax)+0.04
    (x,y) = pos[n]
    xx,yy = trans((x,y)) # figure coordinates
    xa,ya = trans2((xx,yy)) # axes coordinates
    a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize])
    if G.degree()[n]%2==0:
        a.imshow(imgc)
    else:
        a.imshow(imgc)  
    a.set_aspect('equal')
    a.axis('off')
plt.show()