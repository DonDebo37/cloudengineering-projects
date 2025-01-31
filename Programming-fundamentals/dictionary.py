# Dictionaries
# - Store and retrieve information
# - Key and Values

# EC2
ec2_instance = {
    "InstanceId": "i-123456abce",
    "InstanceType": "t2.micro",
    "State": "running",
    "publicIpAddress": "201.0.111.6"  
}

instance_id = ec2_instance["InstanceId"]
print(f"this is a {instance_id} instance")

public_ip = ec2_instance.get("PublicIpAddress", "No Public Ip address is here")
print(f"Public IP address: {public_ip}")

# Adding a new key-value pair
ec2_instance["AvailabilityZone"] = "eu-west-2"
ec2_instance["State"] = "stopped"

print(ec2_instance)

# Removing a key-value pair

# Using pop(removes and returns the value)
availability_zone = ec2_instance.pop("AvailabilityZone")
print(f"Removed Availability Zone: {availability_zone}")
print(ec2_instance)

# Using del (removes the key-value pair)
del ec2_instance["publicIpAddress"]
print(ec2_instance)