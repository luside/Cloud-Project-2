# Author: liyu zhang liyuz@student.unimelb.edu.au
# Time: 10/May/2017
# Project: Clustering and Cloud Computing - Assignment 2
from boto.ec2.regioninfo import RegionInfo
import boto.ec2

# create region object to specify the endpoint connecting to and availability zone
region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')

# the access key and secret key to establish connection with nectar and get authority to modify.
# these two keys are downloaded from nectar dashboard -> Access&Security -> API Access -> Download EC2 Credentials
access_key = "24ae81c8cef743b5a12f6e64bcba6c2d"
secret_key = "103b7b1e74d84131b48aa22787249316"

# create a connection object to establish connection with nectar
ec2_conn = boto.connect_ec2(aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                            is_secure=True, region=region, port=8773,
                            path='/services/Cloud', validate_certs=False)

# show all available images on nectar
'''images = ec2_conn.get_all_images()
for img in images:
    print('id', img.id, 'name', img.name)'''
# above part of code was launched before to get all available images on nectar,
# For assignment, we chose id ami-c163b887 name NeCTAR Ubuntu 16.04 LTS (Xenial) amd64 (pre-installed murano-agent)
#############################################
# create instance
ec2_conn.run_instances('ami-c163b887', min_count=0, max_count=1, key_name='CCC_liam', instance_type='m1.small',
                       security_groups=['ssh', 'default', 'icmp', 'http'], placement='melbourne-np')
# terminate instance
'''ec2_conn.terminate_instances(instance_ids=['instance ID, like 'i-xxxxxxxx'])'''

# show all reservation (instances)
reservations = ec2_conn.get_all_reservations()

# create a list to record (str)instance_id
instance_id = []

# list all reservations(instances) on nectar
for idx, res in enumerate(reservations):
    instance_id.append(str(res.instances)[10:-1])
    print(idx, res.id, res.instances)

# request volume
vol_req = ec2_conn.create_volume(250, "melbourne-np")
# attach volume
ec2_conn.attach_volume(vol_req.id, instance_id[0], "/dev/vdb")

# give instance a name as a tag, can be used to query, but this won't change the name on nectar
# ec2_conn.create_tags(instance_id, {'Name': 'CCC'})
