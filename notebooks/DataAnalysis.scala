// Databricks notebook source
// MAGIC %md
// MAGIC # Data Analysis Notebook

// COMMAND ----------

import org.apache.spark.sql.functions._
import org.apache.spark.sql.SparkSession

// COMMAND ----------

val df = spark.read.format("delta").load("/mnt/data/sales")
df.show()

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW sales_summary AS
// MAGIC SELECT date, SUM(amount) as total_sales
// MAGIC FROM sales_table
// MAGIC GROUP BY date

// COMMAND ----------

val summary = spark.sql("SELECT * FROM sales_summary")
display(summary)
