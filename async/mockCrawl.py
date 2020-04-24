import time
import sys
import os
sys.path.append("..")
sys.path.extend([os.path.join(root, name) for root, dirs, _ in os.walk("../") for name in dirs])
import execTimeUse
import asyncio

#-------------不使用协程----------
def crawl_page(url):
    print("crawling {}".format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))

@execTimeUse.log_execution_time
def main(urls):
    for url in urls:
        crawl_page(url)

#----------------------------------

async def crawl_page_1(url):
    print("crawling {}".format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

@execTimeUse.log_execution_time
async def main_1(urls):
    tasks = [asyncio.create_task(crawl_page_1(url)) for url in urls]
    for task in tasks:
        await task

#---------------test-----------------

if __name__ == '__main__':
    #main(['url_1', 'url_2', 'url_3', 'url_4'])
    asyncio.run(main_1(['url_1', 'url_2', 'url_3', 'url_4']))