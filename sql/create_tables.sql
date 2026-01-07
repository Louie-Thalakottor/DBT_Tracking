-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Create Database Tables

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS production;

-- COMMAND ----------

CREATE OR REPLACE TABLE production.customers (
  customer_id STRING,
  name STRING,
  email STRING,
  created_at TIMESTAMP
)
USING DELTA
LOCATION '/mnt/data/customers';

-- COMMAND ----------

CREATE OR REPLACE TABLE production.orders (
  order_id STRING,
  customer_id STRING,
  order_date DATE,
  amount DECIMAL(10,2)
)
USING DELTA
PARTITIONED BY (order_date);

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dbutils.notebook.exit("Tables created successfully")
