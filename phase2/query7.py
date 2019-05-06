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
import sys, tweepy, csv, re
from textblob import TextBlob
import matplotlib.pyplot as plt
import matplotlib.patches
import pandas as pd

datetime_obj = datetime.datetime.strptime('Sat Apr 13 10:53:51 +0000 2014', '%a %b %d %H:%M:%S +0000 %Y')
print(type(datetime_obj), datetime_obj.isoformat())
ts = time.strftime('%Y-%m-%d', time.strptime('Sat Apr 13 10:53:51 +0000 2014', '%a %b %d %H:%M:%S +0000 %Y'))
print(type(ts))
spark = SparkSession \
    .builder \
    .appName("HashtagCount") \
    .getOrCreate()
df = spark.read.json("E:/phase2/data2.json")
df.createOrReplaceTempView("sports")
sqldf = spark.sql(
    "SELECT name,SUM(cnt) as retweet FROM (SELECT quoted_status.user.screen_name AS name,quoted_status.retweet_count AS cnt FROM sports WHERE quoted_status.retweet_count>0)GROUP BY name ORDER BY retweet DESC LIMIT 10")
sqldf.show(150)

sqldf.toPandas().to_csv('7.csv')
# Code for bar graph
data = pd.read_csv('7.csv')

tournament_data = data["name"]
count_data = data["retweet"]
colors = ["#808080","#FA8072","#33FF3F","#334CFF","#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b","#FFFF00"]
#explode = (0.1, 0, 0, 0, 0)
total_count= (sum(count_data))
data=[]
handles = []
for i, l  in enumerate(tournament_data):
    handles.append(matplotlib.patches.Patch(color=colors[i]))
    data.append(tournament_data[i]+"-"+str("{0:.2f}".format(float(count_data[i]*100)/total_count))+"%")



plt.legend(handles,data, bbox_to_anchor=(0.85,1.025), loc="upper left")
plt.pie(count_data, colors=colors, shadow=False, startangle=90)
plt.title("Count of retweets ")
plt.show()