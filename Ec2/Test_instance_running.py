# import boto3

# def list_ec2_instances():
#     ec2 = boto3.client('ec2')

#     # Describe instances
#     response = ec2.describe_instances()

#     # Extract and print instance information
#     for reservation in response['Reservations']:
#         for instance in reservation['Instances']:
#             instance_id = instance['InstanceId']
#             state = instance['State']['Name']

#             print(f"Instance ID: {instance_id}")
#             print(f"  State: {state}")

#             if state == 'running':
#                 print("  The instance is running.")
#             else:
#                 print("  The instance is not running.")
#     # print(response)
# if __name__ == "__main__":
#     list_ec2_instances()



import boto3, json


def ec2_instance_list():
    ec2 = boto3.client('ec2')

    response = ec2.describe_instances()
    response2 = ec2.describe_snapshots(OwnerIds=['self'])
    for i in response2['Snapshots']:
      snapshot_id = i['SnapshotId']
      volume_id = snapshot_id.get('VolumeId')
    # for reservation in response['Reservations']: 
    #   for instance in reservation ['Instances']:
    #     instance_id = instance['InstanceId']
    #     state = instance['State']['Name']
                
    #     print(f"Instance ID: {instance_id}")
    #     print(f"  State: {state}")
        
    #     if state == 'running':
    #             print("  The instance is running.")
    #     else:
    #             print("  The instance is not running.")
      print(snapshot_id)
      print(volume_id)





     # print(instance_id)
    # print(response)
    






if __name__ == "__main__":
    ec2_instance_list()