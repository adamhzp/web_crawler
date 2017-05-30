import os

# Create the project directory
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('[INFO] Creating project: '+directory)
		os.makedirs(directory)

# Create two essential files for the crawler
def create_data_files(project_name, base_url):

	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'

	if not os.path.exists(queue):
		print('[INFO] Creating queue file for project: '+project_name+'('+queue+')')
		write_file(queue, base_url)
	if not os.path.exists(crawled):
		print('[INFO] Creating crawled file for project: '+project_name+'('+crawled+')')
		write_file(crawled, '')

# Write data to a file(overwrite)
def write_file(path, data):
	with open(path, 'w') as f:
		f.write(data)

# Add data to a existing file
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data+'\n')

# Delete all content in file
def delete_file_contents(path):
	with open(path, 'w'):
		pass

def file_to_set(file_name):
	result = set()
	with open(file_name, 'rt') as f:
		for line in f:
			result.add(line.replace('\n', ''))

	return result

def set_to_file(links, file):
	delete_file_contents(file)
	for link in sorted(links):
		append_to_file(file, link)
