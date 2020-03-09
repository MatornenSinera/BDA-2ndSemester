from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
from functools import reduce
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
import pandas as pd
import re
from nltk.corpus import stopwords
from operator import add
import string
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
import re

table=[]
with open('web-Stanford.txt') as f:
    for x in f:
    	res=re.findall("([0-9]+)\t([0-9]+)", x)
    	table.append(res)
#print(table)

dic={}
for x in table:
	a=int(x[0][0])
	b=int(x[0][1])
	#print(x[0][0], x[0][1])
	if a not in dic:
		dic[a]=[[],[]]
		dic[a][0].append(b)
	else:
		dic[a][0].append(b)
	if b not in dic:
		dic[b]=[[],[]]
		dic[b][1].append(a)
	else:
		dic[b][1].append(a)


connectionsIn=[]
for x in dic.keys():
	row=[x, dic[x][0], dic[x][1]]
	connectionsIn.append(row)

for i, j in zip(connectionsIn, range(10)):
	print(i)

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Learning_Spark") \
    .getOrCreate()
sc=SparkContext.getOrCreate()

RDD=sc.parallelize(connectionsIn, numSlices=1000)
df=RDD.toDF(['Node', 'From', 'To'])
df.show()


RDDDegree=RDD.map(lambda x: [x[0], len(x[1]), len(x[2])])
print(RDDDegree.take(3))

B=RDD.count()
print(B)
DataAverage=RDDDegree.map(lambda x: (1, (x[1], x[2]))).reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1])).map(lambda x: (float(x[1][0]/B), float(x[1][1]/B)))
print(DataAverage.take(1))


# print(type(df.bbbb))
# df2=df.withColumn('bbbb', explode("bbbb"))
# df2.show()

# flat=df2.rdd.map(lambda x: [x[1], x[0]]).groupByKey().map(lambda x: [x[0], list(x[1])])
# print(flat.take(5))
# df3=flat.toDF(['invTo', 'invWhere'])
# df3.show()


