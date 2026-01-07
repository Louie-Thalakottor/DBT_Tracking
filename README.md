# Databricks Data Engineering Project

This repository contains Databricks notebooks, workflows, and configuration files for the data engineering pipeline.

## Structure

- `notebooks/` - Databricks notebooks for data processing
- `sql/` - SQL scripts for table creation and queries
- `conf/` - Cluster and configuration files
- `jobs/` - Job definitions for scheduled workflows
- `pipelines/` - Delta Live Tables pipelines
- `src/` - Reusable Python modules

## Setup

1. Configure Databricks CLI:
   ```bash
   databricks configure --token
   ```

2. Deploy the bundle:
   ```bash
   databricks bundle deploy
   ```

3. Run the ETL pipeline:
   ```bash
   databricks jobs run-now --job-id <job-id>
   ```

## Notebooks

- `ETL_Pipeline.py` - Main ETL workflow using PySpark
- `DataAnalysis.scala` - Analytics queries in Scala
- `create_tables.sql` - Database schema setup

## Delta Live Tables

The `pipelines/` directory contains DLT definitions for streaming data pipelines with built-in quality checks.
