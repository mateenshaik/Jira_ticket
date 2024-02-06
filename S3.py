import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='mateenshaikh6400',
            #################only for creating bucket requierd not need when u deleting bucket#################
             CreateBucketConfiguration={
                 'LocationConstraint': 'ap-south-1'  # Specify your desired region here
            }
)

print(response)
