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
#print(len(m))




Dict={}
for i in m:
    if i in Dict:
        Dict[i]+=1
    else:
        Dict[i]=1
    #print(i)

#print (Dict['alice'])
#print (Dict)

Dict=sorted(Dict.items(),key = lambda kv: kv[1], reverse=True)
#print (Dict)

RankDictX=[i for i in range(1,len(Dict)+1)]
RankDictY=[]
for i in range(len(Dict)):
	RankDictY.append(Dict[i][1])

plt.plot(RankDictX, RankDictY)
plt.show()
plt.plot(RankDictX, RankDictY)
plt.yscale('log')
plt.xscale('log')
plt.show()

print(numpy.polyfit(RankDictX, numpy.log(RankDictY), 1))

