#To read data from database to s3 (bronze)
import psycopg2  #library to connect python with postgresSQL
import pandas as pd 
import boto3
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

database_config = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

#S3 bucket comfig
bucket_name = 'data-engineering-project-storage'
s3_folder = 'bronze/db_data/'

#connect to db:
def fetch_db_data():
    connection = psycopg2.connect(**database_config)

    query = 'SELECT * FROM SHIPMENTS;'
    df = pd.read_sql(query, connection)

    connection.close()
    return df

#upload to S3
def upload_to_s3(df):
    s3 = boto3.client('s3')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    date = datetime.now().strftime("%Y-%m-%d")

    file_name = f'{s3_folder}{date}/shipments_{timestamp}.json'

    s3.put_object(
        Bucket = bucket_name,
        Key = file_name,
        Body = df.to_json(orient='records')
    )
    
    print(f'DB data upload to S3 : {file_name}')


if __name__ == '__main__':
    df = fetch_db_data()
    upload_to_s3(df)