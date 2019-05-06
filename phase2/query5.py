# Python version 2.7.6
# Import the datetime and pytz modules.
import datetime, pytz
import time
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace
from pyspark.sql.functions import split
from pyspark.sql.functions import udf
from pyspark.sql.types import *
import sys,tweepy,csv,re
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches
datetime_obj = datetime.datetime.strptime('Sun Oct 12 10:53:51 +0000 2014', '%a %b %d %H:%M:%S +0000 %Y')
print (type(datetime_obj), datetime_obj.isoformat())
ts = time.strftime('%Y-%m-%d', time.strptime('Sun Oct 12 10:53:51 +0000 2014','%a %b %d %H:%M:%S +0000 %Y'))
print(type(ts))
spark = SparkSession\
.builder\
.appName("HashtagCount")\
.getOrCreate()
df = spark.read.json("E:/phase2/data2.json")
df.createOrReplaceTempView("football")
sqldf = spark.sql("SELECT 'MESSI' player,count(text) as count  \
    FROM football\
    WHERE 1=1\
    AND (upper(text) LIKE '%LIONEL%' or upper(text) LIKE '%MESSI%' or text like '%messi%')\
    GROUP BY player\
    UNION\
    SELECT 'Ronaldo' player,count(text) as count \
    FROM football\
    WHERE 1=1\
    AND (upper(text) LIKE '%RONALDO%' or upper(text) LIKE '%CRISTIANO%' or text like '%ronaldo%')\
    GROUP BY player")
sqldf.show(150)

sqldf.toPandas().to_csv('5.csv')

#Code for bar graph
data = pd.read_csv('5.csv')
data.plot(kind="bar",x='player',y='count',legend=None)
plt.ylabel('votes')
plt.xlabel('Name of the player')
plt.title('Trending Players')
plt.xticks(fontsize=5, rotation=30)
plt.yticks(fontsize=5)
plt.show()