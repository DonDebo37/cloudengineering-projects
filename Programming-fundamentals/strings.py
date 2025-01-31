aws_region = 'eu-west-2'
instance_type = "t3-micro"

IAM_policy = """
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::*"
            ]
        }
    ]
}
"""

print(aws_region)
print(instance_type)
print(IAM_policy)
