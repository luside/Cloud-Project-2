import boto
from boto.ec2.regioninfo import RegionInfo
import boto.ec2
from boto.s3.key import Key

region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')

access_key = "24ae81c8cef743b5a12f6e64bcba6c2d"
secret_key = "103b7b1e74d84131b48aa22787249316"

ec2_conn = boto.connect_ec2(aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                            is_secure=True, region=region, port=8773,
                            path='/services/Cloud', validate_certs=False)

'''images = ec2_conn.get_all_images()
for img in images:
    print('id', img.id, 'name', img.name)'''

'''ec2_conn.run_instances('ami-c163b887', key_name='CCC_liam', instance_type='m1.small',
                       security_groups=['ssh', 'default'])'''


'''ec2_conn.terminate_instances(instance_ids=['i-954a7582'])'''

reservations = ec2_conn.get_all_reservations()
print(type(reservations))
for idx, res in enumerate(reservations):
    print(idx, res.id, res.instances)

#print(reservations[0].instances[0].ip_address)
#print(reservations[0].instances[0].placement)


# connect to object store
'''s3_conn = boto.connect_s3(aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                          is_secure=True, host='swift.rc.nectar.org.au', port=8888, path='/')

buckets = s3_conn.get_all_buckets()'''

'''for bucket in buckets:
    print(bucket.name)
    k = Key(bucket)
    k.key = 'my_key'
    k.set_contents_from_string('hello world')
    k.get_contents_as_string()'''




