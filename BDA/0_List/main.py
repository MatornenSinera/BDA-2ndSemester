huuugeList=[]
with open('C:/Users/Michał/Desktop/BDA-2Semester/BDA/0_List/GoneWithTheWInd.txt') as f:
    huuugeList=f.read().split()
    [word.lower() for word in huuugeList]

import re
Text=' '.join(huuugeList)
regex=r"([0-9A-Za-z'\d]+)[\s.\":,;]"
m=re.findall(regex, Text)
m=[word.lower() for word in m]
with open('C:/Users/Michał/Desktop/BDA-2Semester/BDA/0_List/stopwords_en.txt') as f:
    stopwords=f.read().split()
    [word.lower() for word in stopwords]

print (stopwords)


result = [x for x in m if x not in stopwords and x!="'"]
print (result)

Dict={}
for i in result:
    if i in Dict:
        Dict[i]+=1
    else:
        Dict[i]=1

print (Dict['scarlet'])

i=2
flag=True
while (len(Dict)>200):
    print(len(Dict))
    Dict={k: v for k, v in Dict.items() if v>=i}
    i+=1

print (Dict)
f=open('C:/Users/Michał/Desktop/BDA-2Semester/BDA/0_List/listofwords.txt', "w")
for i in Dict:
    for j in range(0, Dict[i]):
        f.write(i + '\n')
f.close()