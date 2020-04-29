import asyncio
import aiohttp
import requests
import time
import concurrent.futures
import threading

#-----------------使用单线程下载---------------------------------
def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))
    
def download_all(sites):
    for site in sites:
        download_one(site)

#----------------使用多线程----------------------------------------------
def download_one_thread(url): 
    resp = requests.get(url) 
    print('Read {} from {}'.format(len(resp.content), url))
def download_all_thread(sites): 
    # 线程池的使用
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: 
        executor.map(download_one_thread, sites)

#----------------future的使用-------------------------------------------------
def download_one_future(url): 
    resp = requests.get(url) 
    print('Read {} from {}'.format(len(resp.content), url))

def download_all_future(sites): 
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: 
        to_do = [] 
        for site in sites: 
            future = executor.submit(download_one, site) 
            to_do.append(future) 
        #等任务结束
        for future in concurrent.futures.as_completed(to_do): 
            print('result=', future.result())

#------------------asyncio的使用---------------------------------------
async def download_one_async(url): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url) as resp: 
            print('Read {} from {}'.format(resp.content_length, url))

async def download_all_async(sites): 
    tasks = [asyncio.create_task(download_one(site)) for site in sites] 
    await asyncio.gather(*tasks)

#----------------test----------------------------------------------
sites = [
        'https://baike.baidu.com/item/%E5%8C%BA%E5%9D%97%E9%93%BE/13465666?fr=aladdin',
        'https://baike.baidu.com/item/%E6%AF%94%E7%89%B9%E5%B8%81%E6%8C%96%E7%9F%BF%E6%9C%BA/12536531?fr=aladdin',
        'https://baike.baidu.com/item/%E5%BA%9E%E6%B0%8F%E9%AA%97%E5%B1%80',
        'https://baike.baidu.com/item/%E6%8A%97%E7%94%9F%E7%B4%A0'
    ]

def main():
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

def main_thread():
    start_time = time.perf_counter()
    download_all_thread(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

def main_future():
    start_time = time.perf_counter()
    download_all_future(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

def main_async():
    start_time = time.perf_counter()
    download_all_async(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

    
if __name__ == '__main__':
    #main()
    #main_thread()
    #main_future()
    main_async()
