import binascii
import random
def ShingleList(table, k):
    Shingles=[]
    for i in range(len(table)-k):
        Shingle=[]
        for j in range(k):
            Shingle.append(table[i+j])
        Shingles.append(' '.join(Shingle))
    return Shingles


def Jaccard(Shingle1, Shingle2):
    union=Shingle1.union(Shingle2)
    intersection=Shingle1.intersection(Shingle2)
    #print(intersection)
    return len(intersection)/len(union)


ListOfChapterNames=['1','1b','2','2b','3','3b','4','4b','5','5b', '11b']
ListOfWordsInChapters=[[] for i in range(len(ListOfChapterNames))]
DictOfWordsInChapters=[{} for i in range(len(ListOfChapterNames))]
SetOfWordsInChapters=[set() for i in range(len(ListOfChapterNames))]
ListOfShinglesInChapters=[[] for i in range(len(ListOfChapterNames))]
for i,place,num in zip(ListOfChapterNames, ListOfWordsInChapters, range(len(ListOfChapterNames))):
    NameOfChapter = 'Gone With The Wind - Part '+i+'.txt'
    with open(NameOfChapter) as f:
        place=f.read().split()
        place=[word.lower() for word in place if word!='CHAPTER' and word!='PART']
    import re
    Text=' '.join(place)
    regex=r"([0-9A-Za-z'\d]+)[\s.\":,!;]"
    m=re.findall(regex, Text)
    m=[word.lower() for word in m]
    Result=ShingleList(m, 7)
    #print(len(Result), num)
    ListOfShinglesInChapters[num]=set(Result)
    #print(len(ListOfShinglesInChapters[num]), num)

for i in range(len(ListOfShinglesInChapters)):
    for j in range(i, len(ListOfShinglesInChapters)):
        if i!=j:
            #print(ListOfChapterNames[i], ListOfChapterNames[j])
            Jaccard(ListOfShinglesInChapters[i], ListOfShinglesInChapters[j])


#print (ListOfShinglesInChapters[0])


###### MINHASH


numHashes=250

maxShingleID = 2**32-1

nextPrime = 4294967311
def pickRandomCoeffs(k):
    randList = []
  
    while k > 0:
        # Get a random shingle ID.
        randIndex = random.randint(0, maxShingleID) 
      
        # Ensure that each random number is unique.
        while randIndex in randList:
          randIndex = random.randint(0, maxShingleID) 
        
        # Add the random number to the list.
        randList.append(randIndex)
        k = k - 1
        
    return randList


coeffA = pickRandomCoeffs(numHashes)
coeffB = pickRandomCoeffs(numHashes)

signatures = []
shingleID=[[] for i in range(len(ListOfShinglesInChapters))]

for num in range(len(ListOfShinglesInChapters)):
    print(num)
    for shingle in ListOfShinglesInChapters[num]:
        b=binascii.crc32(bytes(shingle, encoding='utf8')) & 0xffffffff
        shingleID[num].append(b)
    shingleID[num]=set(shingleID[num])

    signature=[]

    for i in range(numHashes):
        minHashCode=nextPrime+1
        for ID in shingleID[num]:
            #print(ID, coeffA[i], coeffB[i])
            hashCode=(coeffA[i]*ID+coeffB[i])%nextPrime
            if hashCode<minHashCode:
                minHashCode=hashCode
        signature.append(minHashCode)
    signatures.append(signature)

for i in range(0, 11):
    print(i)
    signature1=signatures[i]
    for j in range(i+1, 11):
        signature2=signatures[j]
        count=0
        if i!=j:
            for k in range(numHashes):
                count=count+(signature1[k]==signature2[k])
            print(i, j, count, numHashes, float(count/numHashes))
            print(i, j, Jaccard(ListOfShinglesInChapters[i], ListOfShinglesInChapters[j]))

#print(signatures)

