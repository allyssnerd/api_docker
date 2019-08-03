import docker

client = docker.DockerClient(base_url='tcp://127.0.0.1:2376')

container = client.containers.run(
	'mysql:5.7', 
	name='mysql',
	 environment =[
       'MYSQL_ROOT_PASSWORD: 123abc!',
       'MYSQL_DATABASE: mysql',
       'MYSQL_USER: python',
       'MYSQL_PASSWORD: 4linux'],
    detach=True,
	ports = {'3306/tcp' : ('127.0.0.1', '3306')}
)



