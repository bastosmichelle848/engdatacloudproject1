import boto3
import pandas as pd

#Criar um cliente para interagir com s3

s3_client = boto3.client('s3')

s3_client.download_file("raw-data-igti", 
                         "enem/year=2020/MICRODADOS_ENEM_2020.csv",
                         "C:/Users/Michelle/Documents/IGTI/data/MICRODADOS_ENEM_2020.csv")

s3_client.upload_file("C:/Users/Michelle/Documents/IGTI/data/MICRODADOS_ENEM_2020.csv",

"datalake-michelle-igti-edc",

"data/MICRODADOS_ENEM_2020.csv")

df=pd.read_csv("C:/Users/Michelle/Documents/data/MICRODADOS_ENEM_2020.csv",encoding="utf-8",sep=";")
print(df)