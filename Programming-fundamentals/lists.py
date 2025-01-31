# List of EC2 instance
instance_ids = ["i-1234", "i-5678", "i-9012"]

# List of IP addresses for a security group
ip_addresses = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "10.0.0.4"]

# List of availability zones in a region
availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

# Print the lists
print(f"EC2 instances to terminate: {instance_ids}")
print(f"first IP addresses: {ip_addresses}")
print(f"Number of AZs: {availability_zones}")

# Add new EC2 instance ID
instance_ids.append("i-3456")
print("after adding a new instance ID")
print("EC2 Instances:", instance_ids)

# Remove EC2 instance ID
instance_ids.remove('i-3456')
print("after removing an instance ID")
print("EC2 Instances:", instance_ids)

# Check if an item is in a list
if "10.0.0.4" in ip_addresses:
    print("Yes 10.0.0.4 is in and allowed")
else:
   print("No 10.0.0.4 is not allowed")
print("ip_addresses:", ip_addresses)

# Slicing a list
# First two AZ
first_two_az = availability_zones[:1]
print("first two AZ:", first_two_az)

# Sorting
instance_ids.sort()
print("sorted EC2 Instances", instance_ids)


# Finding length of a list
number_of_ips = len(ip_addresses)
print(f"Number of IP addresses: {number_of_ips}")

# Accessing list of Items by Index
first_az = availability_zones[0]
last_az = availability_zones[-1]
print(f"First AZ: {first_az}")
print(f"Last AZ: {last_az}")