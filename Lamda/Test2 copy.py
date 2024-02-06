import boto3
import json

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # Describe instances
    # response = ec2.describe_instances()

    # Convert the response to JSON format
    response_json = json.dumps(response, default=str, indent=2)
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

  
    # Write the JSON response to a file

######################################################################################
    # with open('Ec2_output2.txt', 'w') as output_file:
    #     output_file.write(response_json)
#######################################################################################
    
    print(instances_response)

if __name__ == "__main__":
    list_ec2_instances()
