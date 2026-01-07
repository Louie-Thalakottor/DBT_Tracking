# Databricks Delta Live Tables pipeline

import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="raw_customers",
    comment="Raw customer data from source system"
)
def raw_customers():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("/mnt/data/incoming/customers")
    )

@dlt.table(
    name="cleaned_customers",
    comment="Cleaned customer data with quality checks"
)
@dlt.expect("valid_email", "email IS NOT NULL")
@dlt.expect_or_drop("valid_id", "customer_id IS NOT NULL")
def cleaned_customers():
    return (
        dlt.read("raw_customers")
        .withColumn("processed_timestamp", current_timestamp())
        .dropDuplicates(["customer_id"])
    )

@dlt.table(
    name="customer_gold",
    comment="Gold layer customer dimension"
)
def customer_gold():
    return (
        dlt.read("cleaned_customers")
        .select(
            "customer_id",
            "name",
            "email",
            "created_at",
            "processed_timestamp"
        )
    )
