#! python3
# -*- coding:utf-8 -*-
'''
Title: 工作集相关功能
Description:创建工作集、打开工作集、管理工作集、清理缓存、退出
@author:Xushenwei
@update:2018年1月26日
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

class WorkingSetFunctions():
	"""工作集相关功能"""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')


	def creat_working_set(self):
		"""创建工作集""" 
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.系统[0], screen_point.系统[1])
			m1.click(self.BECivilWin, '', screen_point.创建工作集[0], screen_point.创建工作集[1])
			w1 = WinControl('创建工作集')
			sleep(2)
			if w1.exists():
				w1.wait(3)
				w1.controlSetText('[CLASS:Edit; INSTANCE:1]', '测试脚本用创建工作集')
				w1.controlClick('[CLASS:Button; INSTANCE:1]')
				w2 = WinControl('选择所属项目部')
				sleep(2)
				if w2.exists():
					# 选择IM测试
					m1.click('选择所属项目部', '', 850, 385)
					w2.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception("未选中选择所属项目部窗口")
				sleep(2)
				# 选中需要创建工作集的两个工程
				m1.click('创建工作集', '', 780, 390)
				m1.click('创建工作集', '', 780, 420)
				w1.controlClick('[CLASS:Button; INSTANCE:3]')
				sleep(2)
				if w0.exists():
					w0.wait(3)
					t = w0.getPos()
					if t == (826, 438, 1094, 602):
						pass
					else:
						raise Exception('未弹出打开工作集选择框')
					sleep(1)
					w0.controlClick('[CLASS:Button; INSTANCE:2]')
				else:
					raise Exception('未弹出打开工作集选择框')
			else:
				raise Exception("未选中创建工作集窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def open_working_set(self):
		"""打开工作集"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.系统[0], screen_point.系统[1])
			m1.click(self.BECivilWin, '', screen_point.打开工作集[0], screen_point.打开工作集[1])
			sleep(3)
			w1 = WinControl('打开工作集')
			if w1.exists():
				w1.setState(3)
				w1.controlSetText('[CLASS:Edit; INSTANCE:1]', '测试脚本用创建工作集')
				sleep(3)
				# 打开工作集，因为有时候双击会出现打不开的情况，故设置点击数为3
				m1.click('打开工作集', '', 92, 134, clicks=3)
			else:
				raise Exception("未选中打开工作集窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def manage_working_set(self):
		"""管理工作集"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.系统[0], screen_point.系统[1])
			m1.click(self.BECivilWin, '', screen_point.管理工作集[0], screen_point.管理工作集[1])
			sleep(2)
			w1 = WinControl('管理工作集')
			if w1.exists():
				w1.wait(3)
				#w1.setState(3)
				w1.controlSetText('[CLASS:Edit; INSTANCE:1]', '测试脚本用创建工作集')
				sleep(3)
				# 选中要删除的工作集
				m1.click('管理工作集', '', 880, 390)
				sleep(2)
				# 点击删除
				m1.click('管理工作集', '', 870, 760)
				sleep(2)
				if w0.exists():
					sleep(2)
					t1 = w0.getPos()
					if t1 == (844, 438, 1076, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick('[CLASS:Button; INSTANCE:1]')
					sleep(3)
					if w0.exists():
						t2 = w0.getPos()
						if t2 == (880, 438, 1040, 602):
							pass
						else:
							raise Exception('Something went wrong.')
						sleep(2)
						if w0.exists():
							t3 = w0.getPos()
							if t3 == (880, 438, 1040, 602):
								pass
							else:
								raise Exception('Something went wrong.')
							w0.controlClick('[CLASS:Button; INSTANCE:1]')
						else:
							raise Exception('未弹出删除确认框')
					else:
						raise Exception('未弹出删除成功选择框')
				else:
					raise Exception('未弹出删除工作集选择框')
				sleep(2)
				# 关闭管理工作集窗口
				m1.click('管理工作集', '', 1114,263)
			else:
				raise Exception("未弹出管理工作集窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def clear_cache(self):
		"""清理缓存"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.系统[0], screen_point.系统[1])
			m1.click(self.BECivilWin, '', screen_point.清除[0], screen_point.清除[1])
			sleep(2)
			if w0.exists():
				w0.wait(3)
				t1 = w0.getPos()
				if t1 == (832, 437, 1088, 603):
					pass
				else:
					raise Exception('Something went wrong.')
				w0.controlClick('[CLASS:Button; INSTANCE:1]')
				sleep(3)
				if w0.exists():
					w0.wait(3)
					t2 = w0.getPos()
					if t2 == (845, 438, 1075, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick('[CLASS:Button; INSTANCE:2]')
				else:
					raise Exception("没有弹出退出确认窗口")
			else:
				raise Exception("没有弹出清理缓存窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def quit_BECivil(self):
		"""退出"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.系统[0], screen_point.系统[1])
			m1.click(self.BECivilWin, '', screen_point.退出[0], screen_point.退出[1])
			sleep(2)
			if w0.exists():
				w0.wait(3)
				t = w0.getPos()
				if t == (845, 438, 1075, 602):
					pass
				else:
					raise Exception('Something went wrong.')
				w0.controlClick('[CLASS:Button; INSTANCE:1]')
			else:
				raise Exception("没有弹出退出确认窗口")
		else:
			raise Exception("未识别BECivil窗口")


if __name__ == '__main__':
	WSF = WorkingSetFunctions()
	'''
	sleep(2)
	WSF.creat_working_set()
	sleep(2)
	WSF.manage_working_set()



	sleep(2)	 
	WSF.open_working_set()
	'''
	'''
	sleep(2)
	WSF.clear_cache()
	'''
	sleep(2)
	WSF.quit_BECivil()
	