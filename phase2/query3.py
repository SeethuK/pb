import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.functions import udf
from pyspark.sql.types import *
import pandas as pd
import matplotlib.pyplot as plt
import requests
if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("HashtagCount")\
        .getOrCreate()
    df = spark.read.json("E:/phase2/data2.json")
    # df.select('text').where('(upper(text) LIKE "%KHOLI%" or upper(text) LIKE "%VIRAT%")').show()
    df.createOrReplaceTempView("cricketplayer_count")
    sqlhash = spark.sql("SELECT 'Virat' player,count(text) as count  \
        FROM cricketplayer_count\
        WHERE 1=1\
        AND (upper(text) LIKE '%KHOLI%' or upper(text) LIKE '%VIRAT%' or upper(text) LIKE '%VIR%')\
        GROUP BY player\
        UNION\
        SELECT 'Dhoni' player,count(text) as count \
        FROM cricketplayer_count\
        WHERE 1=1\
        AND (upper(text) LIKE '%MSD%' or upper(text) LIKE '%DHONI%')\
        GROUP BY player\
        UNION\
        SELECT 'Russell' player,count(text) as count \
        FROM cricketplayer_count\
        WHERE 1=1\
        AND (upper(text) LIKE '%RUSSELL%' or text LIKE '%russell%')\
        GROUP BY player\
        UNION\
        SELECT 'Sachin' player,count(text) as count\
        FROM cricketplayer_count\
        WHERE 1=1\
        AND (upper(text) LIKE '%SACHIN%' or upper(text) LIKE '%TENDULKAR%')\
        GROUP BY player\
        UNION\
        SELECT 'ABD' player,count(text) as count \
        FROM cricketplayer_count\
        WHERE 1=1\
        AND (upper(text) LIKE '%ABD%' or text LIKE '%abd%')\
        GROUP BY player\
        UNION\
        SELECT 'Shikar' player,count(text) as count \
        FROM cricketplayer_count\
        WHERE 1=1\
        AND (upper(text) LIKE '%SHIKAR%DAWAN%' or upper(text) LIKE '%SHIKAR%' or upper(text) LIKE '%DHAWAN%')\
        GROUP BY player")
    sqlhash.show()
    sqlhash.toPandas().to_csv('3.csv')

#Code for bar graph
data = pd.read_csv('3.csv')
data.plot(kind="bar",x='player',y='count',legend=None)
plt.ylabel('votes')
plt.xlabel('Name of the player')
plt.title('Trending Players')
plt.xticks(fontsize=5, rotation=30)
plt.yticks(fontsize=5)
plt.show()