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

with open('graphrandom.txt') as f:
    connectionsIn=eval(f.read())

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Learning_Spark") \
    .getOrCreate()
sc=SparkContext.getOrCreate()


def CustomMap1(x):
	connections=[i for i in x[3] if i in x[1]]
	return [x[0], (len(x[1]), len(connections))]

def CustomMap2(x):
	sum2=float(x[1][1]/(x[1][0]*(x[1][0]-1)))
	return(x[0], (x[1][0], sum2))


def CustomMap3(x):
	count=0
	lists=[]
	print(x)
	for z in x[1]:
	  	triv=RDD1.filter(lambda row: row[0] == z)
	  	print(triv.take(1))#lists.append(triv[1][1])
	return x



RDD=sc.parallelize(connectionsIn)
RDD2=RDD.groupByKey().map(lambda x: (x[0], list(x[1]))).sortByKey(1, 1)
RDD1=RDD2
RDD2=RDD2.map(CustomMap3)
print(RDD2.take(5))

# dfnew=df.join(df1, on='To').join(df2, on='From')
# dfnew2=dfnew.select(dfnew.From, dfnew.ConnectsFrom, dfnew.To, dfnew.Connects)
# dfnew2.sort(col("From")).show()

# RDDEdit=dfnew2.rdd.map(CustomMap1)
# RDDEdit2=RDDEdit.reduceByKey(lambda x, y: (x[0], x[1]+y[1]))
# print(RDDEdit2.take(15))
# RDDEdit3=RDDEdit2.map(CustomMap2)
# print(RDDEdit3.take(15))
# B=RDDEdit3.count()
# RDDAverage=RDDEdit3.map(lambda x: (1, (x[1][0], x[1][1]))).reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1])).map(lambda x: (x[1][0]/B, x[1][1]/B))
# print(RDDAverage.take(1))