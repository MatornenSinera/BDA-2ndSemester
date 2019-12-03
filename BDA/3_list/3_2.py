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

with open('RandomGraphDirected.txt') as f:
    connectionsIn=eval(f.read())

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Learning_Spark") \
    .getOrCreate()
sc=SparkContext.getOrCreate()

RDD=sc.parallelize(connectionsIn)
df=RDD.toDF(['Node', 'From', 'To'])
df.show()


RDDDegree=RDD.map(lambda x: [x[0], len(x[1]), len(x[2])])
print(RDDDegree.take(3))

B=RDD.count()
DataAverage=RDDDegree.map(lambda x: (1, (x[1], x[2]))).reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1])).map(lambda x: (float(x[1][0]/B), float(x[1][1]/B)))
print(DataAverage.take(1))


# print(type(df.bbbb))
# df2=df.withColumn('bbbb', explode("bbbb"))
# df2.show()

# flat=df2.rdd.map(lambda x: [x[1], x[0]]).groupByKey().map(lambda x: [x[0], list(x[1])])
# print(flat.take(5))
# df3=flat.toDF(['invTo', 'invWhere'])
# df3.show()


