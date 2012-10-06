# how to capture variables passed from the command line in Python?

import boto
import boto.s3.connection

access_key = 'your_access_key'
secret_key = 'your_secret_key'

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = 'your_access_key'
        host = 'objects.dreamhost.com',
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

newbucket = conn.create_bucket('the-ipanemas')

for bucket in conn.get_all_buckets():
  print "{name}\t{created}".format(
          name = bucket.name,
          created = bucket.creation_date,
          )
