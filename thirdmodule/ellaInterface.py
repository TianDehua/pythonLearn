#!/usr/bin/env python3

# -*- coding:utf-8 -*-

import requests
import json

paramContent = {
    'versionNum':'1.0.6'
}
paramDict = {
    'snCode' : 'X91600N191016000000050',
    'method' : 'ella.boeuser.updateAppVersion', #指定method
    'equipmentCode' : 'X91600N191016000000050',
    'format' : 'json',
    'sign' : '57482800eaf55a577000dd65',
    'deviceNo' : 'X91600N191016000000050',
    'content' : json.dumps(paramContent),
    'platform' : 'BOE',
    'system_v' : 'FUNBOOK OSV1.1.1',
    'token' : '123456',
    'uid' : 'U201908021820021699882', #用户uid
    'app_key' : '2017506650',
    'v' : '1.0.6',
    'countryCode' : '+86',
    'sign_method' : 'md5',
    'channelCode' : 'boe',
    'timestamp' : '2020-04-14 17:07:30',
    'cid' : 'C202003311405169927101'
}

j = json.dumps(paramDict)
print(type(j))
p = json.loads(json.dumps(paramDict))
print(type(p))

r = requests.post('http://devboeapi.ellabook.cn/rest/api/service', 
headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'},
data=paramDict)
print(r.status_code)
print(r.text)
print('-----json=',r.json)