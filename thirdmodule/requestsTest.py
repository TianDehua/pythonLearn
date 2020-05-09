#!/usr/bin/env python3

# -*- coding:utf-8 -*-

import requests
import chardet

# get请求
r = requests.get('https://www.baidu.com/', verify=False) #百度首页
print(r.status_code) #状态码
print(r.text) #返回文本
print("----------content=")
print(r.content) #文本或二进制内容的bytes对象

# 特定类型的响应，可以直接获取

# # 需要传入 Http Headers时， 我们传入一个dict作为headers参数
# r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}, verify=False) 
# print(r.status_code)
# print(r.text)


# # post请求
r = requests.post('https://accounts.douban.com/login', 
headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'},
data={'form_email': 'abc@example.com', 'form_password': '123456'},
verify=False)
print(r.status_code)
print(r.text)
print(chardet.detect(r.text))



