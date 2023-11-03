import sys

ec2_instance_type = sys.argv[1]

if ec2_instance_type == "t2.micro":
    print("OK YOU WILL CREATE EC2 INSTANCE IN FREE TIER ACCOUNT")

else:
    print("DON'T CREATE EC2 INSTANCE IN FREE TIER ACCOUNT")