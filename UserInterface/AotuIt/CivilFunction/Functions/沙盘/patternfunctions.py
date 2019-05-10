#! python3
# -*- coding:utf-8 -*-
'''
Title: 沙盘模式
Description:沙盘模式、工程时间
@author:Xushenwei
@update:
'''
import sys, configparser, autoit, pymysql, operator
from time import sleep
sys.path.insert(0, r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from autoit_function import MouseControl, WinControl, ProcessControl
from time import sleep

class PattrenFuncitons():
	"""沙盘相关功能"""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')
		self.BWWin = conf.get('parameters', 'win_BW')
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MessagesConfig.ini")
		self.messgae1 = conf.get('监控设置Messages', 'username')
		self.messgae2 = conf.get('监控设置Messages', 'password')
		self.messgae3 = conf.get('监控设置Messages', 'address')
		self.messgae4 = conf.get('监控设置Messages', 'port')

	def sand_table_pattern(self):
		"""沙盘模式"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.沙盘模式[0], screen_point.沙盘模式[1])
			sleep(2)
			w1 = WinControl('欢迎使用沙盘功能')
			if w1.exists():
				w1.wait(3)
				w1.controlClick('[CLASS:Button; INSTANCE:3]')
				sleep(1)
				# 设置开工和竣工时间
				m1.click('欢迎使用沙盘功能', '', 890, 640)
				sleep(3)
				w2 = WinControl('工程时间')
				if w2.exists():
					w2.wait(3)
					w2.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('未能打开工程时间窗口')
				sleep(1)
				w1.controlClick('[CLASS:Button; INSTANCE:3]')
				sleep(2)
				# 设置监控服务
				m1.click('欢迎使用沙盘功能', '', 830, 640)
				sleep(3)
				w3 = WinControl('第三方监控服务设置')
				if w3.exists():
					w3.wait(3)
					# 选择对接平台
					m1.click('第三方监控服务设置', '', 950, 460)
					m1.click('第三方监控服务设置', '', 950, 480)
					w3.controlSetText('[CLASS:Edit; INSTANCE:1]', self.messgae1)
					w3.controlSetText('[CLASS:Edit; INSTANCE:2]', self.messgae2)
					w3.controlSetText('[CLASS:Edit; INSTANCE:3]', self.messgae3)
					w3.controlSetText('[CLASS:Edit; INSTANCE:4]', self.messgae4)
					sleep(1)
					w3.controlClick('[CLASS:Button; INSTANCE:2]')
					sleep(12)
					if w0.exists():
						w0.wait(3)
						t = w0.getPos()
						if t == (868, 438, 1052, 602):
							pass
						else:
							raise Exception('Something went wrong.')
						w0.controlClick('[CLASS:Button; INSTANCE:1]')
					else:
						raise Exception('未能成功设置监控服务')
					w1.controlClick('[CLASS:Button; INSTANCE:3]')
					sleep(1)
					w1.controlClick('[CLASS:Button; INSTANCE:3]')
					sleep(1)
					w1.controlClick('[CLASS:Button; INSTANCE:3]')
					sleep(1)
					w1.controlClick('[CLASS:Button; INSTANCE:3]')
				else:
					raise Exception('未能打开第三方监控服务设置')
			else:
				raise Exception('未能打开欢迎使用沙盘功能')
		else:
			raise Exception("未识别BECivil窗口")

	def project_time(self):
		"""工程时间"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.工程时间[0], screen_point.工程时间[1])
			sleep(2)
			w1 = WinControl("工程时间")
			if w1.exists():
				w1.wait(3)
				w1.controlClick("[CLASS:Button; INSTANCE:1]")
			else:
				raise Exception("未打开工程时间窗口")
		else:
			raise Exception("未识别BECivil窗口")


if __name__ == '__main__':
	PF = PattrenFuncitons()

	sleep(2)
	PF.sand_table_pattern()

	sleep(2)
	PF.project_time()