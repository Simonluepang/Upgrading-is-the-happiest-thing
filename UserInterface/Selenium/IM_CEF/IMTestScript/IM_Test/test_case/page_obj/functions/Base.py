#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 页面功能继承类
Description: open、find_element、find_elements、quit、script
@author: Xushenwei
@update: 2018年6月11日
'''
import os
import sys
from selenium import webdriver

def insert_img(driver, file_name):
	base_dir = os.path.dirname(os.path.dirname(__file__))
	base_dir = str(base_dir)
	base_dir = base_dir.replace('\\', '/')
	base = base_dir.split('/test_case')[0]
	file_path = base + "/report/image/" + file_name
	driver.get_screenshot_as_file(file_path)

def common_path(path, npos):
	n1 = path.find(npos)
	BASE_DIR = path[0:n1]
	return BASE_DIR
	
def browser():
	path = os.path.dirname(__file__)
	npos = 'IMTestScript'
	APPLICATION_PATH = common_path(path=path, npos=npos) + r'IMTestScript\Client\x64_vc11_unicode_release\BimIM.exe'
	options = webdriver.ChromeOptions()
	options.binary_location = APPLICATION_PATH
	driver = webdriver.Chrome (chrome_options=options)
	handles = driver.window_handles
	driver.switch_to.window(handles[-1])
	os.popen('TASKKILL/F /IM ZY.Downloader.exe')
	return driver

class Page(object):

	center_url = "/"

	def __init__(self, selenium_driver, base_url=center_url, parent=None):
		self.base_url = base_url
		self.driver = selenium_driver
		self.timeout = 30
		self.parent = parent

	def on_page(self):
		return self.driver.current_url == (self.base_url + self.url)

	def _open(self, url):
		url = self.base_url + url 
		self.driver.get(url)
		assert self.on_page(), 'Did not land on %s' % url

	def open(self):
		self._open(self.url)

	def find_element(self, *loc):
		return self.driver.find_element(*loc)

	def find_elements(self, *loc):
		return self.driver.find_elements(*loc)

	def script(self, src):
		return self.driver.execute_script(src)

	def quit(self):
		return self.driver.quit()

if __name__ == '__main__':

	# print(common_path(os.path.dirname(__file__), 'IMTestScript'))
	# driver = browser()
	# driver.quit()
	# driver = webdriver.Chrome()
	# driver.get('https://www.baidu.com')
	# insert_img(driver, 'baidu.png')
	# driver.quit()

	# print(common_path('aaa', 'IMTestScript'))