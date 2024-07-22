import boto3
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Function to delete files from S3
def delete_files_from_s3(bucket_name, file_names):
    # Initialize a session using Amazon S3
    s3 = boto3.client('s3')
    
    # Iterate over the file names and delete each file
    for file_name in file_names:
        try:
            s3.delete_object(Bucket=bucket_name, Key=file_name)
            print(f"Deleted {file_name} from {bucket_name}")
        except Exception as e:
            print(f"Error deleting {file_name} from {bucket_name}: {e}")

# Read file names from CSV
def get_file_names_from_csv(csv_file, column_name):
    df = pd.read_csv(csv_file)
    file_names = df[column_name].tolist()
    return file_names

# Example usage
bucket_name = 'artisanbucketoregon184340-qa'
csv_file = 'output_files.csv'
column_name = 'File Name'  # Change as necessary

# Get the file names from the CSV file
file_names = get_file_names_from_csv(csv_file, column_name)

# Delete the files from the S3 bucket
delete_files_from_s3(bucket_name, file_names)
