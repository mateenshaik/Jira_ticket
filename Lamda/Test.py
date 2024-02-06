import boto3

def list_ec2_instances():
    ec2 = boto3.client('ec2')

    # Describe instances
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()

    # Extract and print volume IDs
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}")
            for volume in instance['BlockDeviceMappings']:
                print(f"  Volume ID: {volume['Ebs']['VolumeId']}")
                

if __name__ == "__main__":
    list_ec2_instances()
