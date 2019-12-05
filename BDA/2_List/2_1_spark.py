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

def word_TokenizeFunct(x):
    regex=r"([0-9A-Za-z'\d]+)[\s.\":,!;]"
    m=re.findall(regex, x)
    m=[word.lower() for word in m]
    return m

def removeStopWordsFunct(x):
    filteredSentence = [w for w in x if not w in stop_words]

    return [(' ').join(filteredSentence)]


data = spark.read.text('Gone With The Wind - Part 1.txt')
data.show(20)
dataselect=data.select('value').rdd.flatMap(lambda x: x)
dataselect.collect()
wordTokenizeRDD = dataselect.map(word_TokenizeFunct)
stop_words=set(stopwords.words('english'))


print (wordTokenizeRDD.take(20))
wordTokenizeRDD=wordTokenizeRDD.filter(lambda row: row!=[])
print (wordTokenizeRDD.take(20))
stopwordRDD = wordTokenizeRDD.map(removeStopWordsFunct)
print (stopwordRDD.take(20))
stopwordRDD2 = stopwordRDD.flatMap(lambda line: line[0].split(' ')).map(lambda word: (word, 1))
print(stopwordRDD2.take(20))
