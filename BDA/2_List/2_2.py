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

def avg_reduce_func(value1, value2):
	return(value1[0]+value2[0], value1[1]+value2[1])

def avg_map_func(row):
	return (1, (row[0], row[1]))

data = spark.read.text('integers.txt')
data.show(10)
dataselect=data.select('value').rdd.flatMap(lambda x: x)
dataselect=dataselect.filter(lambda row: row!='')
#print(dataselect.take(5))

dataIntegers=dataselect.flatMap(lambda line: line.split(', ')).map(lambda integer: (int(integer), 1))
#print(dataIntegers.take(20))
dataIntegers=dataIntegers.reduceByKey(lambda a,b : a+b).sortByKey(1, 1)
print(dataIntegers.map(lambda a: a[0]).take(1))
print(dataIntegers.sortByKey(0, 1).map(lambda a: a[0]).take(1))
print(dataIntegers.map(lambda a: a[0]).collect())
dataAverage=dataselect.flatMap(lambda line: line.split(', ')).map(lambda integ: (1, int(integ))).reduceByKey(lambda x, y: x+y).collect()[0][1]
dataMean=dataAverage/dataselect.count()
print(dataMean)