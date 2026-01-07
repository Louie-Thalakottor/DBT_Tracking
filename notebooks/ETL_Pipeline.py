# Databricks notebook source
# MAGIC %md
# MAGIC # ETL Pipeline
# MAGIC This notebook performs ETL operations on the data lake

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM delta.`/mnt/data/raw_table`

# COMMAND ----------

df = spark.read.format("delta").load("/mnt/data/raw_table")
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Transformation

# COMMAND ----------

transformed_df = df.withColumn("processed_date", lit(current_date()))
transformed_df.write.format("delta").mode("overwrite").save("/mnt/data/processed_table")
