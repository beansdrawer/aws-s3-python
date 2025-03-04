import boto3
from botocore.client import Config
from dotenv import dotenv_values

config = dotenv_values('.env') 

s3 = boto3.client(
    's3',
    aws_access_key_id=config['AWS_ACCESS_KEY'],
    aws_secret_access_key=config['AWS_SECRET_KEY'],
    config=Config(signature_version='s3v4')
)

with open('./banana.jpg', 'rb') as data:
  s3.upload_fileobj(data, config['AWS_BUCKET_NAME'], 'banana.jpg')
