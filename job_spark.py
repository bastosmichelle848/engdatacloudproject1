from pyspark.sql.functions import mean,max,min,col,count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

#Ler os dados do enem 2020

enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema",True)
    .option("delimiter",";")
    .load("s3://raw-data-igti/enem/year=2020/")

)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://raw-data-igti/staging/enem/")
)