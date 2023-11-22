import boto3
from botocore.client import Config

# Uncomment Code blocks for thigns you want to test

# Create a boto3 resource
s3_client = boto3.resource('s3', aws_access_key_id="My Minio Access Key",
                           aws_secret_access_key="My Minio Secret Key", endpoint_url="http://My-Minio-IP:Port",
                           config=Config(signature_version='s3v4'))


# Print all buckets in Minio
# buckets = [bucket.name for bucket in s3_client.buckets.all()]
# print(buckets)

# Add a Bucket
# s3_client.create_bucket(Bucket='mybucket')

# Add a file to a bucket
# s3_client.Bucket("my cool bucket").upload_file("file/path/coolfile.text", "dump/file")
