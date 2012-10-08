#!/usr/local/bin/env python

import sys
import boto
import boto.s3.connection

access_key = 'your_access_key'
secret_key = 'your_secret_key'
upload_file = sys.argv[2]

print upload_file

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = 'your_access_key'
        host = 'objects.dreamhost.com',
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

newbucket = conn.create_bucket(sys.argv[1])
newkey = newbucket.new_key('sv')
newkey.set_contents_from_filename(upload_file)

for bucket in conn.get_all_buckets():
  print "{name}\t{created}".format(
          name = bucket.name,
          created = bucket.creation_date,
          )

for key in newbucket.list():
  print "{name}\t{size}\t{modified}".format(
          name = key.name,
          size = key.size,
          modified = key.last_modified,
          )
