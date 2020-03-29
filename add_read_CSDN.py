import re
import requests
from requests import RequestException
import time
 
 
def get_page(url):
	try:
		headers = {
			'Referer': 'https://blog.csdn.net',  # 伪装成从CSDN博客搜索到的文章
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'  # 伪装成浏览器
		}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('请求出错')
		return None
 
 
def parse_page(html):
	try:
		read_num = int(re.compile('<span.*?read-count.*?(\d+).*?</span>').search(html).group(1))
		return read_num
	except Exception:
		print('解析出错')
		return None
 
 
def main():
	try:
		url = 'https://blog.csdn.net/wangjinxile/article/details/104798510'  # 待刷浏览量博客的url
		url2 = 'https://blog.csdn.net/wangjinxile/article/details/80729304'  # 待刷浏览量博客的url

		while 1:
			html = get_page(url)
			time.sleep(0.5)
			html2 = get_page(url2)
			if html:
				read_num = parse_page(html)
				if read_num:
					print('第一篇当前阅读量：', read_num)
			if html2:
				read_num = parse_page(html2)
				if read_num:
					print('第二篇当前阅读量：', read_num)
			time.sleep(5)  # 设置访问频率，过于频繁的访问会触发反爬虫
	except Exception:
		print('出错啦！')
 
 
if __name__ == '__main__':
	main()