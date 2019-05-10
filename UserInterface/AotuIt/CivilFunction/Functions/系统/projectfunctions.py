#! python3
# -*- coding:utf-8 -*-
'''
Title: 工程相关功能
Description:上传工程、打开工程、下载工程、本地任务、EDS后台删除工程
@author: Xushenwei
@update: 2018年1月26日
'''
import sys, configparser, autoit, pymysql, operator
from time import sleep
sys.path.insert(0, r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from autoit_function import MouseControl, WinControl, ProcessControl
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def choose_direction(num):
	for i in range(num):
		autoit.send("{DOWN}")
	autoit.send("{RIGHT}")

class ProjectFuncions():
	"""工程相关功能"""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')
		self.BWWin = conf.get('parameters', 'win_BW')
		self.downloadaddress = conf.get('parameters', 'downloadaddress')
		self.uploadaddress = conf.get('parameters', 'uploadaddress')

	def upload_project(self, projectname):
		"""上传工程"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.系统[0], screen_point.系统[1])
			m1.click(self.BECivilWin, '', screen_point.上传工程[0], screen_point.上传工程[1])
			w1 = WinControl("打开")
			sleep(4)
			if w1.exists():
				w1.wait(3)
				w1.setState(3)
				# 输入保存上传工程的地址
				m1.click('打开', '', 820, 45)
				w1.controlSetText('[CLASS:Edit; INSTANCE:2]', self.uploadaddress)
				autoit.send("{ENTER}")
				sleep(2)
				w1.controlSetText('[CLASS:Edit; INSTANCE:1]', projectname)
				w1.controlClick('[CLASS:Button; INSTANCE:1]')
				sleep(2)
				w2 = WinControl("上传工程")
				sleep(2)
				if w2.exists():
					w2.wait(3)
					w2.controlClick('[CLASS:Button; INSTANCE:3]')
					sleep(3)
					w3 = WinControl("上传位置")
					if w3.exists():
						w3.wait(3)
						# 选择IM测试
						m1.click(self.BECivilWin, '', 940, 435)
						sleep(1)
						w3.controlClick("[CLASS:Button; INSTANCE:1]")
					else:
						raise Exception('未选中上传位置窗口')
					sleep(1)
					w2.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('未选中上传工程窗口')
			else:
				raise Exception('未选中打开窗口')
			sleep(22)
			w5 = WinControl("Luban Explorer（Civil）提醒您")
			w5.wait(60)
			if w5.exists():
				pass
			else:
				raise Exception("上传成功提示未显示")
		else:
			raise Exception("未识别BECivil窗口")

	def open_project(self, projectname):
		"""打开工程"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.系统[0], screen_point.系统[1])
			m1.click(self.BECivilWin, '', screen_point.打开工程[0], screen_point.打开工程[1])
			sleep(3)
			w1 = WinControl("选择工程")
			if w1.exists():
				w1.wait(3)
				w1.setState(3)
				# 输入名字搜索
				m1.click("选择工程", '', 50, 35)
				autoit.send(projectname)
				sleep(5)
				# 打开测试脚本用土建工程
				m1.click(self.BECivilWin, '', 92, 133, clicks=3)
			else:
				raise Exception("未选中选择工程窗口")
			sleep(10)
			# 使视图视角变为俯视视角
			m1.click(self.BECivilWin, '', 440, 440, button='right')
			m1.click(self.BECivilWin, '', 490, 475)
		else:
			raise Exception("未识别BECivil窗口")

	def download_porject(self):
		"""下载工程"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.系统[0], screen_point.系统[1])
			m1.click(self.BECivilWin, '', screen_point.下载工程[0], screen_point.下载工程[1])
			sleep(2)
			w1 = WinControl('浏览文件夹')
			if w1.exists():
				w1.wait(3)
				# 选择下载的目标地址
				w1.controlTreeView('[CLASS:SysTreeView32; INSTANCE:1]', 'Select', extra='桌面')
				choose_direction(6)
				choose_direction(3)
				choose_direction(1)
				choose_direction(2)
				sleep(2)
				w1.controlClick('Button1')
				if w0.exists():
					w0.wait(3)
					t = w0.getPos()
					# 目标文件夹没有下载过该工程
					if t == (0, 0, 1920, 1040):
						pass
					# 目标文件夹曾经下载过该工程
					elif t == (832, 438, 1088, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					sleep(2)
					w0.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					pass
				sleep(1)
				w2 = WinControl('下载管理器')
				if w2.exists():
					pass
				else:
					raise Exception('未弹出下载管理器窗口')
			else:
				raise Exception("未选中浏览文件夹窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def local_task(self):
		"""本地任务"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.系统[0], screen_point.系统[1])
			m1.click(self.BECivilWin, '', screen_point.本地任务[0], screen_point.本地任务[1])
			w1 = WinControl("  本机处理任务")
			if w1.exists():
				w1.wait(3)
				w1.setState(3)
				# 历史记录
				m1.click("  本机处理任务", '', 85, 30)
				# 删除此次上传的两条记录
				for i in range(2):
					m1.click("  本机处理任务", '', 50, 90)
					w1.controlClick('Button1')
					if w0.exists():
						w0.waitActive(3)
						# 识别确定删除窗口关联的进程ID
						t = w0.getPos()
						if t == (845, 438, 1075, 602):
							pass
						else:
							raise Exception("未成功删除该任务")
						sleep(1)
						w0.controlClick('Button1')
						sleep(1)
					else:
						raise Exception("未成功删除该任务")
				sleep(1)
				# 关闭本机处理任务
				m1.click("  本机处理任务", '', 1905, 5)
			else:
				raise Exception("未选中本机任务窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def delete_project(self):
		"""EDS后台删除上传的工程"""
		'''
		# 这段话是防止使用pyton通过selenium模拟打开chrome窗口报错：您使用的是不受支持的命令行标记: --ignore-certificate-errors
		options = webdriver.ChromeOptions()
		options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
		driver = webdriver.Chrome(chrome_options=options)
		#火狐浏览器有些情况和Chrome不同，有时候Chrome能走通的在火狐上就走不通
		'''
		driver = webdriver.Firefox()
		# 全屏显示浏览器
		driver.maximize_window()
		driver.get("http://192.168.3.70:8080/enterprise/loginPDS.htm")
		# 输入账号密码并点击登录
		driver.find_element_by_css_selector("#enterpriseUsername").send_keys("admin")
		driver.find_element_by_css_selector("#enterprisePassword").send_keys("111111")
		driver.find_element_by_css_selector("#enterpriseLoginButton").click()
		# 点击工程管理
		projectmanage = driver.find_element_by_css_selector("#title_projectmanage")
		projectmanage.click()
		sleep(3)
		# 切入frame控件
		driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
		# 删除测试脚本用安装工程，因为担心会误删，所以使用全名称精确分两次查找并删除
		ds = ('测试脚本用安装工程', '测试脚本用土建工程')
		for d in ds:
			messageinput0 = driver.find_element_by_id('condition_top')
			messageinput0.clear()
			messageinput0.send_keys(d)
			# 点击搜索按钮
			button0 = driver.find_element_by_id('search_top')
			button0.click()
			# 全选搜索到的内容
			selectall0 = driver.find_element_by_id('checkAll')
			pt = driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr/td/span')
			selectall0.click()
			# 删除工程
			deleteproject0 = driver.find_element_by_xpath('/html/body/div[4]/div[1]/button[2]')
			deleteproject0.click()
			# 弹出提示框点击确认,[.dismiss()]相当于取消，[.text]为获取
			driver.switch_to_alert().accept()
			sleep(2)
		# 切出frame控件
		driver.switch_to_default_content()
		sleep(2)
		# 点击回收站
		trash2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul[3]/li/div/span[2]')
		trash2.click()
		# 切入frame控件
		driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
		sleep(3)
		# 输入搜索内容
		messageinput2 = driver.find_element_by_id('condition_top')
		messageinput2.clear()
		messageinput2.send_keys("测试脚本用")
		sleep(2)
		# 点击搜索按钮
		button2 = driver.find_element_by_id('search_top')
		button2.click()
		# 全选搜索到的内容
		selectall2 = driver.find_element_by_id('checkAll')
		selectall2.click()
		# 删除工程
		deleteproject = driver.find_element_by_xpath('/html/body/div[4]/div[1]/button[1]')
		deleteproject.click()
		# 弹出提示框点击确认
		driver.switch_to_alert().accept()
		sleep(3)
		driver.get_screenshot_as_file(self.downloadaddress + "\\成功删除工程.png")
		driver.quit()



if __name__ == '__main__': 
	PF = ProjectFuncions()
	PF.delete_project()
	'''
	ds = ('测试脚本用安装工程', '测试脚本用土建工程')
	sleep(2)
	for d in ds:
		PF.upload_project(d)
		sleep(5)
	
	sleep(2)
	PF.open_project()
	
	sleep(2)
	PF.download_porject()
	
	sleep(2)
	PF.local_task()
	
	sleep(2)
	PF.delete_project()
	
	sleep(2)
	PF.download_porject()
	'''