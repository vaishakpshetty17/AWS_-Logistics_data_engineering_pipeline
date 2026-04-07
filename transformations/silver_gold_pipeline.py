from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark Session FIRST
spark = SparkSession.builder.appName("LogisticsPipeline").getOrCreate()

# Configure S3 (AFTER spark creation)
spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", "YOUR_KEY")
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "YOUR_SECRET")
spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.amazonaws.com")

# Load Data
api_df = spark.read.json("s3a://your-bucket/bronze/api_data/")
db_df = spark.read.json("s3a://your-bucket/bronze/db_data/")
file_df = spark.read.json("s3a://your-bucket/bronze/file_data/")

# Clean each dataset
api_df = api_df.dropDuplicates()
db_df = db_df.dropDuplicates()
file_df = file_df.dropDuplicates()

# Join datasets
df = db_df.join(api_df, "shipment_id", "left") \
          .join(file_df, "shipment_id", "left")

# Transform
result = df.groupBy("status").count()

# Save to S3
result.write.mode("overwrite").parquet("s3a://your-bucket/gold/status_summary/")

print("✅ Transformation completed")
