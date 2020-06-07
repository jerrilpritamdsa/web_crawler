import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project '+ directory)
        os.makedirs(directory)



# create queue and crawled file

def create_data_files(project_name,base_url):
    queue=project_name+"/queue.txt"
    crawled=project_name+"/crawled.txt"

    if not os.path.isfile(queue):
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, '')

# create new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#add data to existing file
#like the different links in the links present on the
#original page
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')

#delete the contents of a file

def delete_file_content(path):
    with open(path,'w'):
        pass

#read a file and convert each item to set item
def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#iteriate thru a set , each iterm will be a new line in the file_name
def set_to_file(links,file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)
