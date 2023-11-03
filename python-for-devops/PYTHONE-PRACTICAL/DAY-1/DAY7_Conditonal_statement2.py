import sys

ec2_instance_type = sys.argv[1]

if ec2_instance_type == "t2.micro":
    print("It will charge you 2 Dollars a Day")
elif ec2_instance_type == "t2.medium":
    print("It will charge you 4 Dollars a Day")
elif ec2_instance_type == "t2.xlarge":
    print("It will charge you 8 Dollar a Day")
else:
    print("Please provide a Valid Instance Type")