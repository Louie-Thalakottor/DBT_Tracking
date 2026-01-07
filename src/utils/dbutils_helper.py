"""
Databricks utilities helper functions
"""

def get_dbutils(spark):
    """Get dbutils from spark session"""
    try:
        from pyspark.dbutils import DBUtils
        return DBUtils(spark)
    except ImportError:
        import IPython
        return IPython.get_ipython().user_ns["dbutils"]

def read_secret(scope, key):
    """Read secret from Databricks secret scope"""
    dbutils = get_dbutils(spark)
    return dbutils.secrets.get(scope=scope, key=key)

def mount_storage(container_name, storage_account, mount_point):
    """Mount Azure storage to DBFS"""
    dbutils = get_dbutils(spark)
    
    configs = {
        f"fs.azure.account.key.{storage_account}.dfs.core.windows.net": 
        dbutils.secrets.get(scope="azure-storage", key="storage-key")
    }
    
    dbutils.fs.mount(
        source=f"abfss://{container_name}@{storage_account}.dfs.core.windows.net/",
        mount_point=mount_point,
        extra_configs=configs
    )
