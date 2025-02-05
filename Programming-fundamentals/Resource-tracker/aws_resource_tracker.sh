#!/bin/bash


####################
# Author: Adebola
# Date: 05/02/25
#
# Version: V1
#
# This script will report the AWS resource usage
# #################

# AWS S3
# AWS EC2
# AWS Lambda
# AWS IAM Users

set -x

# List s3 buckets
echo "print list of s3 buckets"
aws s3 ls > resourceTracker
aws s3 ls

# List Ec2 Instances
echo "print list of ec2 instances"
aws ec2 describe-instances

# List Aws Lambda
echo "print list of lambda functions"
aws lambda list-functions >> resourceTracker:q!

# List IAM Users
echo "print list of IAM users"
aws iam-users > resourceTracker
