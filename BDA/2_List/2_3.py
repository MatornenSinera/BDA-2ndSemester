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

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Learning_Spark") \
    .getOrCreate()
sc=SparkContext.getOrCreate()

def word_TokenizeFunct(x):
    regex=r"([0-9A-Za-z'\d]+)[\s.\":,!;]"
    m=re.findall(regex, x)
    m=[word.lower() for word in m]
    return m

def removeStopWordsFunct(x):
    filteredSentence = [w for w in x if not w in stop_words]

    return [(' ').join(filteredSentence)]  

def maprow(x):
	if x[0]>x[1]:
		return [x[1],x[0]]
	else:
		return [x[0],x[1]]

with open('stopwords_en.txt') as f:
    stopwords=f.read().split()
    stopwords=[word.lower() for word in stopwords]
    		
with open('GoneWithTheWInd-Fixed.txt') as f:
    huuugeList=f.read().split()
    huuugeList=[word.lower() for word in huuugeList if word not in stopwords]




Text=' '.join(huuugeList)
regex=r"([0-9A-Za-z'\d]+)[\s.\":,!;]"
m=re.findall(regex, Text)
m=[word.lower() for word in m]
table=[]
for i in range(len(m)-1):
	table.append([m[i], m[i+1]])

rdd=sc.parallelize(table)
rdd=rdd.map(maprow).map(lambda a: ((a[0], a[1]), 1)).reduceByKey(lambda a, b: a+b).map(lambda a: (a[1], a[0])).sortByKey(0, 1)
print(rdd.take(20))