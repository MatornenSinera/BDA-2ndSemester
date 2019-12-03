import numpy as np
import random
from numba import jit
import matplotlib.pyplot as plt
N=[200]
ps=[0.2, 0.4]
conc=[0.9, 0.8, 0.7, 0.6]
pmodel=14
q=2
np.set_printoptions(threshold=np.inf)

@jit
def CreateModel(N, p, mag):
	Lattice=np.zeros((N, p*4))
	for i in range(0, N):
		print(i)
		k=0
		for j in range(i, N):
			if i!=j and random.random()<float(p/N):
				Lattice[i][len(Lattice[i][Lattice[i]!=0])]=j+1
				Lattice[j][len(Lattice[j][Lattice[j]!=0])]=i+1
	Spins=np.ones(N)
	for i in range(len(Spins)):
		if random.random()>mag:
			Spins[i]=-1
	return [Lattice, Spins, N]

@jit
def ElementarChange(Model, Spins, N, q, p):
	a=random.randint(0, N-1)
	X=Model[a]
	#print (B)
	samp= random.sample(list(X), q)
	#print(samp)
	opinion=0
	b=random.random()
	if b<p/2:
		Spins[a]=1
	elif b<p:
		Spins[a]=-1
	else:
		for i in samp:
			opinion+=Spins[int(i)-1]
		if opinion==q:
			Spins[a]=1
		if opinion==-1*q:
			Spins[a]=-1
	return [Model, Spins, N]


def concentration(A):
	return sum(A[1])/len(A[1])


A=CreateModel(2000, 14, 0.5)
print(A[1])
ploty=[]
plotx=[]
for i in range(2000*200):
	A=ElementarChange(A[0],A[1], A[2], 8, 0)
	if i%(2000)==0:
		print(i/2000)
		plotx.append(i/2000)
		ploty.append(concentration(A))
plt.plot(plotx, ploty)
plt.show()
print(A[1])



