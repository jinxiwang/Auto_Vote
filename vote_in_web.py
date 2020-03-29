import re
import requests
from requests import RequestException
import time
import json
import socket
import random


def read_num(html):
	try:
		read_num = int(re.compile('<span>票数.*?(\d+).*?</span>').search(html).group(1))
		print('给兵哥哥怒投5票，当前票数：', read_num)
	except Exception:
		print('解析出错')
		return None

def get_page(url):
	try:
		headers = {
			'Referer': 'http://www.fm169.cn/mvvotes.html',  # 伪装
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'  # 伪装成浏览器
		}
		response = requests.get(url, headers=headers)

		if response.status_code == 200:
			read_num(response.text)
		return None

	except RequestException:
		print('请求出错')
		return None

def vote(url, n):
	ip = [i for i in range(1,256)]
	Fake_Ip = '192.168.{}.{}'.format(random.choice(ip),random.choice(ip))
	print('Fake_Ip: {}'.format(Fake_Ip))
	datas = {'id': 7132}
	header = {
		'Accept': 'text/plain, */*; q=0.01',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Content-Length': '6',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Host': 'www.fm169.cn',
		'Origin': 'http://www.fm169.cn',
		'Proxy-Connection': 'keep-alive',
		'Referer': 'http://www.fm169.cn/mvvotes.html',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
		'X-Real-Ip':Fake_Ip,
		'X-Forwarded-For':Fake_Ip
	}
	try:
		for i in range(n):
			response = requests.post(url, headers=header, data = datas)
			votes_num = int(re.compile('.*?(\d+).*?').search(response.text).group(1))
		print('给兵哥哥怒投5票，当前票数：',votes_num)

	except Exception:
		print('传参出错')
 
def main():

	try:
		url = 'http://www.fm169.cn/musicvotelist_s7132.html'  # 网页浏览的url
		url2 = 'http://www.fm169.cn/zanmusics.html'  # 待刷票数的url
		for i in range(300):
			vote(url2,5)
			# get_page(url) #浏览网页

	except Exception:
		print('出错啦！')

if __name__ == '__main__':
	main()