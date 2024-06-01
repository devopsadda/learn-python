#!/bin/python3.11
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
	ImageId='ami-00beae93a2d981137',
	MinCount=1,
	MaxCount=1,
	InstanceType='t2.micro')
print(instance[0].id)
