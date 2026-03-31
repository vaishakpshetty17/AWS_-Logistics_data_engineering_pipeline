#To read data from file into s3 (bronze)
import boto3
from datetime import datetime

#config
file_path = 'C:/Users/vaish/Logistics_Data_Platform/data/sample_data/terminal_logs.json'
bucket_name = 'data-engineering-project-storage'
s3_folder = 'bronze/file_data/'

def upload_file():
    s3 = boto3.client('s3')

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") 
    date = datetime.now().strftime("%Y-%m-%d")

    file_name = f"{s3_folder}{date}/terminal_logs_{timestamp}.json"

    with open(file_path, 'r') as file:
        s3.put_object(Bucket = bucket_name,
        Key = file_name,
        Body = file.read()
        )

    print(f'File uploaded to s3: {file_name}')

if __name__ == "__main__":
    upload_file()