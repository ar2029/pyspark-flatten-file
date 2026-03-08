import pyspark.sql.functions as f
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('flatten').getOrCreate()

df1 = spark.read.csv("C:/Users/HP/Desktop/flatten.csv", multiLine=True, header = True)

df1.show()

df2 = df1.select("id",f.when(f.col("ind") == f.lit("FN"), f.col("fname")).otherwise("null").alias("fname"), 
                 f.when(f.col("ind") == f.lit("LN"), f.col("fname")).otherwise("null").alias("lname"), 
                 f.when(f.col("ind") == f.lit("AD"), f.concat_ws(",", f.col("fname"), f.col("lname"), 
                 f.col("apartment"), f.col("street"))).otherwise("null").alias("address"), 
                 f.when(f.col("ind") == f.lit("PH"), f.col("fname")).otherwise("null").alias("phone") )
df2.show(truncate=False)

df3 = df2.groupby("id").agg(f.min("fname").alias("fname"), f.min("lname").alias("lname"), f.min("address").alias("address"), f.min("phone").alias("phone"))
df3.show(truncate=False)

df4 = df3.filter((f.col("fname") != f.lit("null")) & (f.col("lname") != f.lit("null")))
df4.show()

df5 = df4.withColumn("apartment", f.split(f.col("address"), ',').getItem(0)).withColumn('street', f.split(f.col("address"), ',').getItem(1)).withColumn('city', f.split(f.col("address"), ',').getItem(2)).withColumn('country',f.split(f.col("address"), ',').getItem(3))
df5.select("id", "fname", "lname", "apartment", "street", "city", "country", "phone").show(truncate=False)
df5.show(100)