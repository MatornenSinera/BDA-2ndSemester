import math


def TFIDF(Word, Chapters, Sums):
	TFIDF=[0 for i in Chapters]
	IDF_Sum=0
	for chapter in Chapters:
		if Word in chapter:
			IDF_Sum+=1
	IDF=math.log(len(Chapters)/IDF_Sum)
	for dokumentnum in range(len(Chapters)):
		if Word in Chapters[dokumentnum]:
			#print(Chapters[dokumentnum][Word])
			TFIDF[dokumentnum]=Chapters[dokumentnum][Word]/Sums[dokumentnum]*IDF
		else:
			TFIDF[dokumentnum]=0
	TFIDF=[str(round(i, 5)) for i in TFIDF]
	return TFIDF


ListOfWordsInChapters=[[] for i in range(10)]
ListOfChapterNames=['1','1b','2','2b','3','3b','4','4b','5','5b']
DictOfWordsInChapters=[{} for i in range(10)]
SetOfWordsInChapters=[set() for i in range(10)]
for i,place,num in zip(ListOfChapterNames, ListOfWordsInChapters, range(10)):
	NameOfChapter = 'Gone With The Wind - Part '+i+'.txt'
	with open(NameOfChapter) as f:
		place=f.read().split()
		place=[word.lower() for word in place if word!='CHAPTER' and word!='PART']
	import re
	Text=' '.join(place)
	regex=r"([0-9A-Za-z'\d]+)[\s.\":,!;]"
	m=re.findall(regex, Text)
	m=[word.lower() for word in m]
	with open('stopwords_en.txt') as f:
		stopwords=f.read().split()
		stopwords=[word.lower() for word in stopwords]
	place=[]
	for x in m:
		if x not in stopwords and x!="'":
			place.append(x)
			if x not in DictOfWordsInChapters[num]:
				DictOfWordsInChapters[num][x]=1
			else:
				DictOfWordsInChapters[num][x]+=1
	SetOfWordsInChapters[num]=set(place)

#[print (len(SetOfWordsInChapters[i])) for i in range(10)]
WholeSet=set.union(*SetOfWordsInChapters)
#print (len(WholeSet))
Sums=[sum(i.values()) for i in DictOfWordsInChapters]


DictOfTFIDF={}
for Word in WholeSet:
	DictOfTFIDF[Word]=TFIDF(Word, DictOfWordsInChapters, Sums)
f=open('TFIDF.txt', "w")
f.write('Word:\t\t\t'+'\t'.join(ListOfChapterNames)+'\n')
for i in DictOfTFIDF:
	if len(i)>=8:
		f.write(i +'\t\t'+'\t'.join(DictOfTFIDF[i])+'\n')
	elif len(i)>=16:	
		f.write(i +'\t'+'\t'.join(DictOfTFIDF[i])+'\n')
	else:
		f.write(i +'\t\t\t'+'\t'.join(DictOfTFIDF[i])+'\n')
f.close()

for Name, Chapter in zip(ListOfChapterNames, DictOfWordsInChapters):
	i=2
	flag=True
	while (len(Chapter)>200):
		Chapter={k: v for k, v in Chapter.items() if v>=i}
		i+=1

	f=open('Listofwords - '+Name+'.txt', "w")
	f.write(str(len(Chapter))+'\n')
	for i in Chapter:
		for j in range(0, Chapter[i]):
			f.write(i + '\n')
	f.close()


for Name, num in zip(ListOfChapterNames, range(10)):
	NewDict=sorted(DictOfTFIDF.items(), key=lambda kv:kv[1][num], reverse=True)
	print(NewDict[:10])