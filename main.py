import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME='rediff'
HOMEPAGE='https://www.rediff.com/'
DOMAIN_NAME=get_domain_name(HOMEPAGE)
QUEUE_FILE=PROJECT_NAME+'/queue.txt'
CRAWLED_FILE=PROJECT_NAME+'/crawled.txt'
NUMBER_OF_THREADS=8
#thread Queue
queue = Queue()
#main spider
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


#create worker threads (will die when main exists)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()


#  do next job in the queue
def work():
    while True:
        url=queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

#each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#create other spiders
#check if there are items in the que if so clawl them
def crawl():
    queued_links=file_to_set(QUEUE_FILE)
    if len(queued_links) >0:
        print(str(len(queued_links))+' links in the queue')
        create_jobs()


create_workers()
crawl()