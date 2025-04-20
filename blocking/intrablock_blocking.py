from pyspark.sql import SparkSession

# Step 1: Spark session with JDBC
spark = SparkSession.builder \
    .appName("BlockingPhaseER") \
    .config("spark.jars", "lib/postgresql-42.7.3.jar") \
    .getOrCreate()

url = "jdbc:postgresql://localhost:5432/er_db"
properties = {
    "user": "postgres",
    "password": "your_password",  # Replace securely
    "driver": "org.postgresql.Driver"
}

# Step 2: Load from DB
abt_df = spark.read.jdbc(url=url, table="abt_products", properties=properties)
buy_df = spark.read.jdbc(url=url, table="buy_products", properties=properties)

# Step 3: Add source labels
abt_df = abt_df.withColumn("source", spark.sparkContext.broadcast("Abt").value)
buy_df = buy_df.withColumn("source", spark.sparkContext.broadcast("Buy").value)

# Step 4: Combine
combined_df = abt_df.unionByName(buy_df)

combined_df.show(5)
