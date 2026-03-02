from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("FirstSparkApp") \
    .getOrCreate()

# Sample Data
data = [("Ali", 50000),
        ("Sara", 60000),
        ("Ahmed", 45000)]

columns = ["Name", "Salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show Data
df.show()

# df_filtered = df.filter(df.Salary > 50000)
# df_filtered.show()
# df_filtered.explain()

df2 = df.filter(df.Salary > 40000).select("Name")
df2.explain()
df2.show()
# Stop Spark
spark.stop()