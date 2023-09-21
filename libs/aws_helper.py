import os
import boto3

# Initialize a session using Amazon S3.
session = boto3.Session(
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'),
    region_name=os.environ.get('AWS_REGION')
)


# Create an S3 client using the session.
s3 = session.client('s3')

# Specify the S3 bucket name and file path on S3 where you want to upload the file.
bucket_name = os.environ.get('AWS_BUCKET')

s3_file_path = 'local/commands.txt'

# Specify the local file you want to upload.
local_file_path = 'commands.txt'

try:
    # Upload the local file to S3.
    s3.upload_file(local_file_path, bucket_name, s3_file_path)
    print(f'Successfully uploaded {local_file_path} to {bucket_name}/{s3_file_path}')
except Exception as e:
    print(f'Error uploading file: {str(e)}')