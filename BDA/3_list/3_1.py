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

with open('graphy.txt') as f:
    connections=eval(f.read())

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Learning_Spark") \
    .getOrCreate()
sc=SparkContext.getOrCreate()

rdd=sc.parallelize(connections)
df=rdd.toDF(['where', 'bbbb'])
df.show()
print(type(df.bbbb))
df2=df.withColumn('bbbb', explode("bbbb"))
df2.show()

flat=df2.rdd.map(lambda x: [x[1], x[0]]).groupByKey().map(lambda x: [x[0], list(x[1])])
print(flat.take(5))
df3=flat.toDF(['invTo', 'invWhere'])
df3.show()


