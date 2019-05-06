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
sqlDF = spark.sql("SELECT 'Cricket' as Domain, count(*) as Count from Sports where text like '%dhoni%' and text like '%cricket%'\
        UNION\
        SELECT 'Football' as Domain, count(*) as Count from Sports where text like '%Messi%' and text like '%football%'\
        UNION\
        SELECT 'Tennis' as Domain, count(*) as Count from Sports where text like '%serena%' and text like '%tennis%'")
pd = sqlDF.toPandas()
pd.to_csv('8.csv', index=False)
pd.plot(kind="bar",x="Domain",y="Count")
plt.show()
sqlDF.show()