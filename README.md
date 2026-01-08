# DBT_Tracking

Testing Databricks presence in the repo.

This is a dummy repository that mimics Databricks structure for testing detection scripts.

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
