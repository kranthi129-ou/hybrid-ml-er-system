from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BlockingPhaseER") \
    .config("spark.jars", "C:/Spark/lib/postgresql-42.7.3.jar") \
    .getOrCreate()

url = "jdbc:postgresql://localhost:5432/er_db"
properties = {
    "user": "postgres",
    "password": "Jelly22fi$h",
    "driver": "org.postgresql.Driver"
}

abt_df = spark.read.jdbc(url=url, table="abt_products", properties=properties)
buy_df = spark.read.jdbc(url=url, table="buy_products", properties=properties)

abt_df = abt_df.withColumn("source", spark.sparkContext.broadcast("Abt").value)
buy_df = buy_df.withColumn("source", spark.sparkContext.broadcast("Buy").value)

combined_df = abt_df.unionByName(buy_df)
combined_df.show(5)
