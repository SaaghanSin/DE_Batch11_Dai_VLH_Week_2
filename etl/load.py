import boto3
from botocore.exceptions import NoCredentialsError
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

AWS_S3_BUCKET_NAME ='ex3-de-pass11'
AWS_REGION ='ap-southeast-2'
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
LOCAL_FILE = 'recalls_cleaned.csv'

def load_data_to_s3(df, bucket_name, s3_path):
    try:
        with open(LOCAL_FILE, 'a') as f:
            df.to_csv(f, header=f.tell()==0, index=False)
    except FileNotFoundError:
        df.to_csv(LOCAL_FILE, index=False)
    
    # Add timestamp to S3 path
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    s3_path_with_timestamp = f"{s3_path}_{timestamp}.csv"
    
    # Upload the file to S3
    s3_client = boto3.client(
        service_name='s3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    try:
        s3_client.upload_file(LOCAL_FILE, bucket_name, s3_path_with_timestamp)
        print(f"Data uploaded to s3://{bucket_name}/{s3_path_with_timestamp}")
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")