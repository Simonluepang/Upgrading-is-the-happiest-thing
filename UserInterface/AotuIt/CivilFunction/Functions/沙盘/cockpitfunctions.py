#! python3
# -*- coding:utf-8 -*-
'''
Title: 驾驶舱以及总进度图
Description:沙盘驾驶舱、上传图片
@author: Xushenwei
@update: 2018年1月26日
'''
import sys, configparser, autoit, pymysql, operator
from time import sleep
sys.path.insert(0, r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from autoit_function import MouseControl, WinControl, ProcessControl
from time import sleep

class CockpitFunctions():
	""""""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')
		self.BWWin = conf.get('parameters', 'win_BW')
		self.downloadaddress = conf.get('parameters', 'downloadaddress')
		self.uploadaddress = conf.get('parameters', 'uploadaddress')

	def sand_table_cockpit(self):
		"""沙盘驾驶舱"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.沙盘模式[0], screen_point.沙盘模式[1])
			m1.click(self.BECivilWin, '', screen_point.沙盘驾驶舱[0], screen_point.沙盘驾驶舱[1])
			sleep(3)
			w1 = WinControl(" 沙盘驾驶舱")
			if w1.exists():
				w1.wait(3)
				# 播放
				m1.click(' 沙盘驾驶舱', '', 190, 970)
				sleep(3)
				# 刷新
				m1.click(' 沙盘驾驶舱', '', 450, 40)
				sleep(3)
				if w0.exists():
					w0.wait(3)
					t = w0.getPos()
					if t == (838, 438, 1082, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					sleep(1)
					w0.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					raise Exception("未弹出刷新完成窗口")
				# 关闭沙盘驾驶舱窗口
				m1.click(' 沙盘驾驶舱', '', 1905, 10)
			else:
				raise Exception("未打开沙盘驾驶舱窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def upload_picture(self):
		""" """
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.沙盘[0], screen_point.沙盘[1])
			m1.click(self.BECivilWin, '', screen_point.上传图片[0], screen_point.上传图片[1])
			sleep(1)
			w1 = WinControl('打开')
			if w1.exists():
				w1.wait(3)
				m1.click('打开', '', 1110, 45)
				sleep(1)
				w1.controlSetText('[CLASS:Edit; INSTANCE:2]', self.uploadaddress)
				autoit.send("{ENTER}")
				sleep(1)
				w1.controlSetText('[CLASS:Edit; INSTANCE:1]', r'picture1.jpg')
				sleep(1)
				w1.controlClick("[CLASS:Button; INSTANCE:1]")
				sleep(3)
				if w0.exists():
					w0.wait(3)
					t = w0.getPos()
					if t == (874, 438, 1046, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					raise Exception("未弹出上传成功窗口")
			else:
				raise Exception("未弹出打开窗口")
		else:
			raise Exception("未识别BECivil窗口")


if __name__ == '__main__':
	CF = CockpitFunctions()
	'''
	sleep(2)
	CF.sand_table_cockpit()
	'''
	sleep(2)
	CF.upload_picture()
	