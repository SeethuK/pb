from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()
# spark is an existing SparkSession
df = spark.read.json("E:/phase2/data2.json")
# Displays the content of the DataFrame to stdout

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("Sports")
sqlDF = spark.sql("SELECT 'Cricket' as sport, count(*) as Count from Sports where text like '%cricket%' or text like '%ipl%' or upper(text) like '%CRICKET%' or upper(text) like '%IPL'\
        UNION\
        SELECT 'Tennis' as sport, count(*) as Count from Sports where text like '%tennis%' or upper(text) like '%TENNIS%'\
        UNION\
        SELECT 'Football' as sport, count(*) as Count from Sports where text like '%football%' or upper(text) like '%FOOTBALL%' or text like '%fifa%' or upper(text) like '%FIFA%'")
pd = sqlDF.toPandas()
pd.to_csv('1.csv', index=False)
pd.plot(kind="bar",x="sport",y="Count")
plt.show()
sqlDF.show()