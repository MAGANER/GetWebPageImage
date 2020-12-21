import requests
import random
from bs4 import BeautifulSoup


class ImageGetter:
	def __init__(self, url):
		self.data = {}
		self.data["link"] = url
	
	def get_html_page(self, headers=None, params=None):
		return requests.get(self.data["link"],headers=headers,params=params)
	
	def parse_html_page(self,page):
		return BeautifulSoup(page.text,"html.parser")
	
	def get_images(self,html):
		# data can be contained with link/a tag
		data1 = html.find_all("link")
		data2 = html.find_all("a")
		
		#combine them and convert to strings
		data = data1 + data2
		data = list(map(lambda n: str(n),data))
		paths= list(filter(lambda string: "href" in string, data))
		
		def get_href_data(href):
			href_pos = href.find('href="')
			
			find_value_len = 6
			_href = href[href_pos+find_value_len:]
			
			end_pos = _href.find('"')
			return _href[:end_pos]
		href_data = list(map(get_href_data,paths))	
		
		is_png    = lambda data:".png" in data
		image_data =list(filter(is_png,href_data))
		 
		return image_data