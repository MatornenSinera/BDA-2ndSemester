import matplotlib.pyplot as plt
import numpy

huuugeList=[]
with open('Alice In Wonderland.txt', encoding='utf8') as f:
    huuugeList=f.read().split()
    huuugeList=[word.lower() for word in huuugeList]

import re
Text=' '.join(huuugeList)
regex=r"([0-9A-Za-z'\d]+)[\s.\":,!;]"
m=re.findall(regex, Text)
m=[word.lower() for word in m]


### Find all words that end with space or special characters.

Dict={}
for i in m:
    if i in Dict:
        Dict[i]+=1
    else:
        Dict[i]=1
###For every word - create a indicator of frequency

Dict=sorted(Dict.items(),key = lambda kv: kv[1], reverse=True)
RankDictX=[i for i in range(1,len(Dict)+1)]
RankDictY=[]
for i in range(len(Dict)):
	RankDictY.append(Dict[i][1])

###Create data for both axis of the plot

plt.plot(RankDictX, RankDictY)
plt.show()
plt.plot(RankDictX, RankDictY)
coefs=numpy.polyfit(numpy.log10(RankDictX), numpy.log10(RankDictY), 1)
print(coefs)
RankDictYReg=[10**(numpy.log10(x)*coefs[0]+coefs[1]) for x in RankDictX]
plt.plot(RankDictX, RankDictYReg)
plt.yscale('log')
plt.xscale('log')
plt.show()

###Create plot, then fit a line of log-log plot.



