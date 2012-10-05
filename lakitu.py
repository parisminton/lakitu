import cloudfiles

# authentication
username = 'account_name:the_username'
api_key = 'the_api_key'

# make a connection
conn = cloudfiles.get_connection(
        username=username,
        api_key=api_key,
        authurl='https://objects.dreamhost.com/auth',
        )

# list Containers in my instance
for container in conn.get_all_containers():
  print container.name

# create a Container
container = conn.create_container('my-new-container');

# list contents of a Container
for obj in container.get_objects():
  print "{0}\t{1}\t{2}".format(obj.name, obj.size, obj.last_modified)

# delete an empty Container
conn.delete_container(container_name)

# create an Object
obj = container.create_object('hello.txt')
obj.content_type = 'text/plain'
obj.load_from_filename('./my_hello.txt')

# download an Object
obj = container.get_object('hello.txt')
obj.save_to_filename('./my_hello.txt')

# delete an Object
container.delete_object('goodbye.txt')
