#! python3
# -*- coding:utf-8 -*-
'''
Title: 监控
Description:插入监控、监控管理、服务设置、监控面板
@author: Xushenwei
@update: 2018年1月26日
'''
import sys, configparser, autoit, pymysql, operator
from time import sleep
sys.path.insert(0, r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from autoit_function import MouseControl, WinControl, ProcessControl
from time import sleep

class MonitoringFunctions():
	"""监控相关功能"""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')
		self.BWWin = conf.get('parameters', 'win_BW')

	def add_monitor(self):
		""" """
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.沙盘模式[0], screen_point.沙盘模式[1])
			sleep(2)
			# 使视图视角变为俯视视角
			m1.click(self.BECivilWin, '', 440, 440, button='right')
			m1.click(self.BECivilWin, '', 490, 475)
			sleep(2)
			m1.click(self.BECivilWin, '', screen_point.插入监控[0], screen_point.插入监控[1])
			w1 = WinControl('插入监控')
			sleep(2)
			if w1.exists():
				w1.wait(3)
				# 关联监控
				w1.controlClick('[CLASS:Button; INSTANCE:3]')
				sleep(8)
				w2 = WinControl('关联监控')
				if w2.exists():
					w2.wait(3)
					m1.click('关联监控', '', 623, 375)
					sleep(2)
					w2.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					raise Exception("未打开关联监控窗口")
				sleep(1)
				# 详细位置
				w1.controlClick("[CLASS:Button; INSTANCE:4]")
				sleep(1)
				m1.click(self.BECivilWin, '', 1050, 520)
				sleep(1)
				m1.click(self.BECivilWin, '', 1050, 520, button='right')
				sleep(2)
				m1.click(self.BECivilWin, '', 1100, 535)
				sleep(1)
				if w1.exists():
					w1.wait(3)
					w1.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					raise Exception("未打开插入监控窗口")
			else:
				raise Exception("未打开插入监控窗口")
			sleep(2)
			if w0.exists():
				w0.wait(3)
				t = w0.getPos()
				if t == (862, 438, 1058, 602):
					pass
				else:
					raise Exception('Something went wrong.')
				w0.controlClick("[CLASS:Button; INSTANCE:1]")
			else:
				raise Exception("未显示插入监控成功窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def monitor_management(self):
		"""监控管理"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.监控管理[0], screen_point.监控管理[1])
			sleep(1)
			w1 = WinControl("监控管理")
			if w1.exists():
				w1.wait(3)
				# 监控查看
				m1.click('监控管理', '', 1140, 300)
				sleep(7)
				w2 = WinControl("监控查看")
				if w2.exists():
					w2.wait(3)
					w2.controlClick("[CLASS:Button; INSTANCE:3]")
					sleep(2)
					w2.controlClick("[CLASS:Button; INSTANCE:4]")
				else:
					raise Exception("未打开监控查看窗口")
				sleep(2)
				# 编辑监控
				m1.click('监控管理', '', 1180, 300)
				sleep(2)
				w3 = WinControl("编辑监控")
				if w3.exists():
					w3.wait(3)
					w3.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					raise Exception("未打开编辑监控窗口")
				sleep(2)
				# 删除
				m1.click('监控管理', '', 1260, 300)
				sleep(1)
				if w0.exists():
					w0.wait(3)
					t = w0.getPos()
					if t == (845, 438, 1075, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					raise Exception("未识别确认删除窗口")
				# 关闭监控管理窗口
				m1.click('监控管理', '', 1360, 210)
			else:
				raise Exception('未识别监控管理窗口')
		else:
			raise Exception("未识别BECivil窗口")

	def service_setting(self):
		""" 、服务设置"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.服务设置[0], screen_point.服务设置[1])
			sleep(1)
			w1 = WinControl("第三方监控服务设置")
			if w1.exists():
				w1.wait(3)
				# 检测
				w1.controlClick("[CLASS:Button; INSTANCE:1]")
				sleep(7)
				if w0.exists():
					w0.wait(3)
					t1 = w0.getPos()
					if t1 == (880, 438, 1040, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					raise Exception("未弹出检测成功窗口")
				sleep(2)
				# 确定
				w1.controlClick("[CLASS:Button; INSTANCE:2]")
				sleep(7)
				if w0.exists():
					w0.wait(3)
					t2 = w0.getPos()
					if t2 == (868, 438, 1052, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					raise Exception("未弹出保存设置成功窗口")
			else:
				raise Exception("未弹出第三方监控服务设置")
		else:
			raise Exception("未识别BECivil窗口")

	def monitoring_panel(self):
		"""监控面板"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.监控面板[0], screen_point.监控面板[1])
			sleep(1)
			# 启用沙盘模式
			if w0.exists():
				w0.wait(3)
				t = w0.getPos()
				if t == (830, 438, 1090, 602):
					pass
				else:
					raise Exception('Something went wrong.')
				w0.controlClick('[CLASS:Button; INSTANCE:1]')
			else:
				raise Exception('未打开开启沙盘模式窗口')
			sleep(13)
			# 点击添加监控
			m1.click(self.BECivilWin, '', 1800, 320)
			sleep(7)
			w1 = WinControl('添加监控')
			if w1.exists():
				w1.wait(3)
				w1.controlClick("[CLASS:Button; INSTANCE:1]")
			else:
				raise Exception("未弹出添加监控窗口")
			sleep(4)
			m1.click(self.BECivilWin, '', screen_point.沙盘模式[0], screen_point.沙盘模式[1])
		else:
			raise Exception("未识别BECivil窗口")





if __name__ == '__main__':
	MF = MonitoringFunctions()
	'''
	sleep(2)
	MF.add_monitor()
	
	sleep(2)
	MF.monitor_management()
	
	sleep(2)
	MF.service_setting()
	'''
	sleep(2)
	MF.monitoring_panel()
	