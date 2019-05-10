#! python3
# -*- coding:utf-8 -*-
'''
Title: 沙盘状态
Description:定义状态、格式刷、状态管理、统计面板、状态统计、刷新数据
@author: Xushenwei
@update: 2018年1月26日
'''
import sys, configparser, autoit, pymysql, operator
from time import sleep
sys.path.insert(0, r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from autoit_function import MouseControl, WinControl, ProcessControl
from time import sleep

class StatusFunctions():
	"""沙盘相关功能"""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')
		self.BWWin = conf.get('parameters', 'win_BW')
		self.downloadaddress = conf.get('parameters', 'downloadaddress')
		self.uploadaddress = conf.get('parameters', 'uploadaddress')

	def define_status(self):
		"""定义状态"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.定义状态[0], screen_point.定义状态[1])
			sleep(2)
			# 框选构件墙
			m1.drag(self.BECivilWin, '', 880, 470, 1220, 550)
			m1.click(self.BECivilWin, '', 1220, 550, button="right")
			m1.click(self.BECivilWin, '', 1280, 570)
			sleep(3)
			w1 = WinControl('编辑历史状态 [4个构件]')
			if w1.exists():
				w1.wait(3)
				# 添加
				w1.controlClick('[CLASS:Button; INSTANCE:4]')
				sleep(2)
				w2 = WinControl('添加新状态记录')
				if w2.exists():
					w2.wait(3)
					w2.controlClick('[CLASS:Button; INSTANCE:4]')
					sleep(1)
					# 选择状态
					m1.click('添加新状态记录', '', 970, 590, clicks=2)
					sleep(1)
					w2.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception("未打开添加新状态记录窗口")
				sleep(2)
				# 完成
				w1.controlClick('[CLASS:Button; INSTANCE:5]')
				sleep(2)
				w3 = WinControl('完成')
				if w3.exists():
					w3.wait(3)
					w3.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception("未打开完成窗口")
				sleep(2)
				# 编辑					
				w1.controlClick('[CLASS:Button; INSTANCE:6]')
				sleep(2)
				w4 = WinControl('编辑历史状态')
				if w4.exists():
					w4.wait(3)
					w4.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('未打开编辑历史状态窗口')
				sleep(1)
				# 使已灰显的状态栏亮显
				m1.click('编辑历史状态 [4个构件]', '', 840, 340)
				sleep(2)
				'''
				# 删除
				w1.controlClick('[CLASS:Button; INSTANCE:7]')
				sleep(2)
				w5 = WinControl('删除状态记录')
				if w5.exists():
					w5.wait(3)
					w5.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('未打开删除状态记录窗口')
				sleep(1)
				'''
				# 完工状态
				w1.controlClick('[CLASS:Button; INSTANCE:8]')
				sleep(1)
				w1.controlClick('[CLASS:Button; INSTANCE:1]')
			else:
				raise Exception("未打开编辑历史状态[4个构件]窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def format_painter(self):
		"""格式刷"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.格式刷[0], screen_point.格式刷[1])
			sleep(2)
			# 勾选“未定义状态”构件
			w0.controlClick("[CLASS:Button; INSTANCE:14]")
			sleep(2)
			# 选择需要使用格式刷的构件
			m1.click(self.BECivilWin, '', 1060, 505)
			sleep(1)
			m1.click(self.BECivilWin, '', 980, 640)
			sleep(1)
			m1.click(self.BECivilWin, '', 980, 640, button='right')
			sleep(2)
			if w0.exists():
				w0.wait(3)
				t = w0.getPos()
				if t == (832, 437, 1088, 603):
					pass
				else:
					raise Exception('Something went wrong.')
				w0.controlClick('[CLASS:Button; INSTANCE:1]')
			else:
				raise Exception("未弹出刷新状态确认框")
		else:
			raise Exception("未识别BECivil窗口")

	def status_manage(self):
		"""状态管理"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.状态管理[0], screen_point.状态管理[1])
			sleep(3)
			w1 = WinControl('状态管理')
			if w1.exists():
				w1.wait(3)
				# 添加新节点
				m1.click('状态管理', '', 750, 300)
				sleep(1)
				# 添加三个新状态
				m1.click('状态管理', '', 810, 300, clicks=3)
				# 使最后一个状态更名为重命名状态1
				autoit.send("重命名状态1")
				autoit.send("{ENTER}")
				sleep(1)
				# 选中新状态
				m1.click('状态管理', '', 830, 730)
				sleep(1)
				# 复制状态
				m1.click('状态管理', '', 830, 730, button='right')
				m1.click('状态管理', '', 890, 785)
				m1.click('状态管理', '', 830, 730, button='right')
				m1.click('状态管理', '', 890, 810)
				sleep(1)
				# 重命名
				m1.click('状态管理', '', 910, 300)
				autoit.send("重命名状态2")
				autoit.send("{ENTER}")
				sleep(1)
				# 上移
				m1.click('状态管理', '', 960, 300)
				sleep(1)
				# 下移
				m1.click('状态管理', '', 1000, 300)
				sleep(1)
				# 升级
				m1.click('状态管理', '', 1045, 300)
				sleep(1)
				# 降级
				m1.click('状态管理', '', 1090, 300)
				sleep(1)
				# 删除
				m1.click('状态管理', '', 860, 300)
				sleep(1)
				if w0.exists():
					w0.wait(3)
					t1 = w0.getPos()
					if t1 == (791, 411, 1127, 628):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					raise Exception("未弹出确认删除窗口")
				# 上传
				m1.click('状态管理', '', 1180, 300)
				sleep(2)
				w2 = WinControl('另存为EDS模板')
				if w2.exists():
					w2.wait()
					w2.controlSetText('[CLASS:Edit; INSTANCE:1]', '测试脚本用新增模板')
					w2.controlClick('[CLASS:Button; INSTANCE:2]')
					sleep(2)
					if w0.exists():
						w0.wait(3)
						t2 = w0.getPos()
						if t2 == (835, 436, 1084, 602):
							pass
						else:
							raise Exception('Something went wrong.')
						w0.controlClick("[CLASS:Button; INSTANCE:1]")
					else:
						pass
				else:
					raise Exception("未打开另存模板窗口")
				sleep(2)
				# 下载
				m1.click('状态管理', '', 1135, 300)
				sleep(5)
				w3 = WinControl('选择EDS模板')
				if w3.exists():
					w3.wait(3)
					w3.controlClick("[CLASS:Button; INSTANCE:2]")
				else:
					raise Exception("未打开选择EDS模板窗口")
				sleep(2)
				w1.controlClick("[CLASS:Button; INSTANCE:1]")
			else:
				raise Exception("未打开状态管理窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def statistics_panel(self):
		"""统计面板"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.统计面板[0], screen_point.统计面板[1])
			sleep(2)
			w0.controlClick("[CLASS:Button; INSTANCE:29]")
			sleep(2)
			w0.controlClick("[CLASS:Button; INSTANCE:29]")
		else:
			raise Exception("未识别BECivil窗口")

	def state_statistics(self):
		"""状态统计"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.状态统计[0], screen_point.状态统计[1])
			sleep(2)
			w0.controlClick("[CLASS:Button; INSTANCE:24]")
			sleep(2)
			w0.controlClick("[CLASS:Button; INSTANCE:25]")
			sleep(3)
			w1 = WinControl("另存为")
			if w1.exists():
				w1.wait(3)
				w1.setState(3)
				m1.click('另存为', '', 1060, 50)
				autoit.send(self.downloadaddress)
				autoit.send("{ENTER}")
				sleep(2)
				w1.controlClick("[CLASS:Button; INSTANCE:1]")
				sleep(1)
				w2 = WinControl("确认另存为")
				if w2.exists():
					w2.wait(3)
					w2.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					pass
				sleep(35)
				if w0.exists():
					w0.wait(3)
					t = w0.getPos()
					if t == (832, 438, 1088, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick("[CLASS:Button; INSTANCE:2]")
			else:
				raise Exception("未能打开另存为窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def refresh_data(self):
		"""刷新数据""" 
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.刷新数据[0], screen_point.刷新数据[1])
			sleep(4)
			if w0.exists():
				w0.wait(3)
				t = w0.getPos()
				if t == (838, 438, 1082, 602):
					pass
				else:
					raise Exception('Something went wrong.')
				w0.controlClick("[CLASS:Button; INSTANCE:1]")
			else:
				raise Exception("数据刷新未完成")
		else:
			raise Exception("未识别BECivil窗口")				





if __name__ == '__main__':
	SF = StatusFunctions()
	
	sleep(2)
	SF.status_manage()
	
	sleep(5)
	SF.define_status()
	
	sleep(5)
	SF.format_painter()
	
	sleep(5)
	SF.statistics_panel()

	sleep(2)
	SF.state_statistics()

	sleep(2)
	SF.refresh_data()
	
	
