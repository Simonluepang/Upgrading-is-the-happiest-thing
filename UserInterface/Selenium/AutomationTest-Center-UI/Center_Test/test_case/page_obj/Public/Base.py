#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 页面功能基类
Description: 基础类Page，封装所有页面都公用的方法，
定义open函数，重定义find_element，switch_frame，send_keys等函数
再初始化方法中定义驱动driver，基本url，title
使用WebDriverWait提供了显式等待方式。
@author: Xushenwei
@update: 2018年9月18日
@editor:
'''
import os, autoit, selenium,time
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from time import sleep



class Page(object):
	"""封装所有页面都公用的方法，例如driver、url、findelement等"""

	def __init__(self, driver):
		# 有默认值的参数一定放在没有默认值的参数后面，
		# 否则会报non-default parameter follows default parameter
		self.driver = driver
		self.timeout = 10
		self.basedir = self.Base_dir()


	def on_page(self, pagetitle):
		# 通过title断言进入的页面是否正确
		# 获取当前页面title，检查输入的title是否在当前title中。
		# return self.driver.current_url == (self.base_url + self.url)
		return pagetitle in self.driver.title

	def open(self, url):
		# 打开页面，并校验页面链接是否加载正确
		# 以单下划线_开头的方法，使用import * 的时候，该方法不会被导入，保证该方法为类私有的
		self.driver.get(url)
		self.driver.maximize_window()
		# assert self.on_page(pagetitle), 'Did not land on %s' % url

	# def open(self,base_url):
	# 	# 定义open方法，调用_open()进行打开链接
	# 	self._open(base_url)

	def find_element(self, *loc):
		# 重定义元素定位方法
		# 加*表示接受一个tuple（元组）
		# return self.driver.find_element(*loc)
		try:
			WebDriverWait(self.driver, self.timeout, 0.5).until(EC.visibility_of_element_located(loc))
			return self.driver.find_element(*loc)
		except:
			print("Can't find element as %s " % loc)

	def find_elements(self, *loc):
		# return self.driver.find_elements(*loc)
		try:
			WebDriverWait(self.driver, self.timeout, 0.5).until(EC.visibility_of_element_located(loc))
			return self.driver.find_elements(*loc)
		except:
			print("Can't find elements as %s " % loc)


	def script(self, src):
		# 定义script方法，用于执行js脚本，范围执行结果
		return self.driver.execute_script(src)

	def switch_frame(self, loc):
		# 重定义switch_frame方法
		return self.driver.switch_to_frame(loc)

	def quit(self):
		# 重定义quit方法
		return self.driver.quit()

	def insert_img(self, file_name):
		"""截图保存"""
		file_path = self.basedir + "/report/image/" + file_name
		self.driver.get_screenshot_as_file(file_path)

	def Base_dir(self):
		"""寻找指定文件夹的系统路径"""
		base_dir = str(os.path.dirname(os.path.dirname(__file__))).replace('\\', '/')
		base = base_dir.split('/page_obj')[0]
		return base
			

	def addfile(self, windowname, filename):
		'''pyautoit实现上传附件'''
		# autoit.mouse_click(x=630, y=255)
		sleep(1.5)
		if autoit.win_exists(windowname):
			autoit.win_active(windowname)
			autoit.mouse_click(x=1580, y=46)
			APPLICATION_PATH = self.Base_dir() + r'/data/uploadfile'
			autoit.send(APPLICATION_PATH)
			autoit.send('{ENTER}')
			autoit.mouse_click(x=780, y=970)
			autoit.send(filename)
			autoit.send('!o')
			sleep(1)
		else:
			raise Exception('没有打开文件窗口')	



if __name__ == '__main__':

	# driver = selenium.webdriver.Chrome()
	# PA = Page(driver)
	# PA.open('https://www.baidu.com')
	# time.sleep(3)
	# PA.insert_img('baidu.png')
	# driver.quit()

	pass