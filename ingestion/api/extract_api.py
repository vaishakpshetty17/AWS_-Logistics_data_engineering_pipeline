#To read data from API's into s3 (bronze)
import requests
import boto3
import json
from datetime import datetime

API_URL = "http://127.0.0.1:5000/shipments"
bucket_name = "data-engineering-project-storage"
s3_folder = "bronze/api_data/"

s3 = boto3.client("s3")


def fetch_api_data():
    response = requests.get(API_URL)
    return response.json()


def upload_to_s3(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    date = datetime.now().strftime("%Y-%m-%d")

    file_name = f"{s3_folder}{date}/shipments_{timestamp}.json"

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(data)
    )

    print(f"API Data uploaded: {file_name}")


if __name__ == "__main__":
    data = fetch_api_data()
    upload_to_s3(data)
