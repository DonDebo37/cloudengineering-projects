# Define the AWS account ID
account_id = "123456789"

# Define the project name
project_name = "cloud_project"

# Concatenate strings to form the s3 bucket name 
bucket_name = account_id + "-" + project_name + "-bucket"

# Print the resulting bucket name
print(f"S3 Bucket Name: {bucket_name}")



# EXERCISE EC2 STRING CONCATENATION

# Environment name, production, staging, development

environment = "dev"

# Application name.

application = "appserver"

# instance number

instance_number = "976353546253"

instance_name = environment + "-" + application + "-instance-" + instance_number

print("EC2 instance name: " + instance_name)