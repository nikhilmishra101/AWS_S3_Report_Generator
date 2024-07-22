import boto3
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def list_s3_files(bucket_name, output_csv):
    # Initialize a session using Amazon S3
    s3 = boto3.client('s3')
    
    # List all objects in the specified S3 bucket
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
    except Exception as e:
        print(f"Error fetching objects from bucket {bucket_name}: {e}")
        return
    
    # Check if the bucket is empty
    if 'Contents' not in response:
        print(f"The bucket {bucket_name} is empty or does not exist.")
        return

    # Open a CSV file to write the details
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Key", "Size (bytes)", "Last Modified"])

        # Iterate through each object and write its details to the CSV
        for obj in response['Contents']:
            key = obj['Key']
            size = obj['Size']
            last_modified = obj['LastModified']
            writer.writerow([key, size, last_modified])
    
    print(f"File details from bucket {bucket_name} have been written to {output_csv}")

# Example usage
bucket_name = "Your Bucket Name"
output_csv = 's3_bucket_files.csv'
list_s3_files(bucket_name, output_csv)
