#! python3
# -*- coding:utf-8 -*-
'''
Title: 协作相关功能
Description:协作管理
@author: Xushenwei
@update: 2018年1月26日
'''
import sys, configparser, autoit, pymysql, operator
from time import sleep
sys.path.insert(0, r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from autoit_function import MouseControl, WinControl, ProcessControl
from time import sleep

class CooperationFunctions():
	"""协作相关功能"""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')
		self.BWWin = conf.get('parameters', 'win_BW')
		self.COProcess = conf.get('parameters', 'process_co')
		self.SuspernsionCtrlProcess = conf.get('parameters', 'process_coas')

	def cooperation_management(self):
		"""协作管理"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.协作[0], screen_point.协作[1])
			m1.click(self.BECivilWin, '', screen_point.协作管理[0], screen_point.协作管理[1])
			sleep(15)
			w1 = WinControl('Luban Cooperation')
			if w1.exists():
				w1.wait(3)
				w1.setState(3)
				sleep(2)
				# 确认协作已删除
				m1.click('Luban Cooperation', '', 960, 575)
				sleep(1)
				# 关闭CO
				m1.click('Luban Cooperation', '', 1882, 29)
			else:
				raise Exception("未能打开鲁班协作窗口")
			# 从后台关闭CO
			sleep(3)
			ps = [ProcessControl(self.COProcess), ProcessControl(self.SuspernsionCtrlProcess)]
			for p in ps:
				if p.exists():
					p.wait(6)
					p.close()
				else:
					print('未找到运行的鲁班协作程序')
		else:
			raise Exception("未识别BECivil窗口")

	



if __name__ == '__main__':
	CF = CooperationFunctions()
	sleep(2)
	CF.cooperation_management()