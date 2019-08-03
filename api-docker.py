import docker

print('{0:<20}{1:<20}'.format ('Nome', 'Imagem'))

client = docker.DockerClient(base_url='tcp://127.0.0.1:2376')


for container in client.containers.list(all=True):
	print('{0:<20}{1:<20}'.format (container.name, container.image.tags[0]))
	if 'nginx' in container.image.tags[0]:
		container.stop()

