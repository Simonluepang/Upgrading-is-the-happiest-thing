#! python3
# -*- coding:utf-8 -*-
'''
Title: 资料相关功能
Description:上传资料、资料管理
@author: Xushenwei
@update: 2018年1月26日
'''
import sys, configparser, autoit, pymysql, operator
from time import sleep
sys.path.insert(0, r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from autoit_function import MouseControl, WinControl, ProcessControl
from time import sleep

class InformationFunctions():
	"""资料相关功能"""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')
		self.BWWin = conf.get('parameters', 'win_BW')
		self.downloadaddress = conf.get('parameters', 'downloadaddress')
		self.uploadaddress = conf.get('parameters', 'uploadaddress')

	def upload_information(self):
		"""上传资料"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.资料[0], screen_point.资料[1])
			m1.click(self.BECivilWin, '', screen_point.上传资料[0], screen_point.上传资料[1])
			w1 = WinControl('上传资料')
			sleep(3)
			if w1.exists():
				w1.wait(3)
				w1.setState(3)
				'''
				# 因删除上传资料的文件夹在BECivil上是有bug的，服务器说要等到下个版本发版的时候再改，所以新增删除文件夹这一块暂时注掉
				m1.click('上传资料', '', 40, 90, button='right')
				sleep(1)
				m1.click('上传资料', '', 100, 105)
				
				m1.click('上传资料', '', 40, 90)# 点击全部
				sleep(1)
				w1.controlClick('[CLASS:Button; INSTANCE:9]')
				sleep(1)
				w2 = WinControl('文件夹新建')
				if w2.exists():
					w2.wait(3)
					w2.controlSetText('[CLASS:Edit; INSTANCE:1]', '测试脚本用上传文件夹')
					sleep(1)
					w2.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception("未打开新建文件夹窗口")
				'''
				# 点击新建文件夹
				m1.click('上传资料', '', 60, 110)
				sleep(1)
				w1.controlClick('[CLASS:Button; INSTANCE:11]')
				sleep(3)
				w3 = WinControl('授权人员')
				if w3.exists():
					w3.wait(3)
					w3.controlSetText('[CLASS:Edit; INSTANCE:1]', 'xushenwei')
					w3.controlClick('[CLASS:Button; INSTANCE:5]')
					sleep(1)
					# 勾选授权人员
					m1.click('授权人员', '', 870, 420)
					w3.controlClick('[CLASS:Button; INSTANCE:2]')
				else:
					raise Exception("未打开授权人员窗口")
				sleep(1)
				# 本地资料
				w1.controlClick('[CLASS:Button; INSTANCE:14]')
				sleep(2)
				w4 = WinControl('打开')
				if w4.exists():
					w4.wait(3)
					w4.setState(3)
					m1.click('打开', '', 970, 50)
					w4.controlSetText('[CLASS:Edit; INSTANCE:2]', self.uploadaddress)
					autoit.send("{ENTER}")
					w4.controlSetText('[CLASS:Edit; INSTANCE:1]', r'上传测试资料.txt')
					sleep(2)
					w4.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception("上传资料未成功")
				sleep(4)
				# 关联
				m1.click('上传资料', '', 1800, 110)
				sleep(2)
				w5 = WinControl(' 设置资料信息')
				if w5.exists():
					w5.wait(3)
					# 点击标签
					m1.click(' 设置资料信息', '', 840, 260)
					w5.controlSetText('[CLASS:ListBox; INSTANCE:1]', '测试脚本用标签')
					w5.controlClick('[CLASS:Button; INSTANCE:14]')
					m1.click(' 设置资料信息', '', 790, 335)
					sleep(1)
					w5.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception("未打开关联资料窗口")
				# 查看
				m1.click('上传资料', '', 1840, 110)
				sleep(2)
				w6 = WinControl('上传测试资料.txt - 记事本')
				if w6.exists():
					w6.wait(3)
					w6.setState(3)
					sleep(1)
					m1.click('上传测试资料.txt - 记事本', '', 1890, 10)
				else:
					raise Exception('未打开上传的资料')
				'''
				m1.click('上传资料', '', 1880, 110)
				sleep(1)
				if w0.exists():
					w0.wait(3)
					w0.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception("未成功删除上传资料")
				'''
				# 关闭上传资料窗口
				m1.click('上传资料', '', 1905, 10)
			else:
				raise Exception("未打开上传资料窗口")
		else:
			raise Exception('未识别BECivil窗口')

	def information_management(self):
		"""资料管理"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.资料[0], screen_point.资料[1])
			m1.click(self.BECivilWin, '', screen_point.资料管理[0], screen_point.资料管理[1])
			w1 = WinControl('资料管理')
			sleep(3)
			if w1.exists():
				w1.wait(3)
				w1.setState(3)
				# 关联
				m1.click('资料管理', '', 1695, 160)
				sleep(1)
				w2 = WinControl(' 设置资料信息')
				if w2.exists():
					w2.wait(3)
					w2.controlClick('[CLASS:Button; INSTANCE:6]')
					m1.click(' 设置资料信息', '', 805, 440)
					sleep(2)
					w2.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('未打开设置资料信息窗口')
				sleep(2)
				w1.setState(3)
				# 反查
				m1.click('资料管理', '', 1785, 160)
				sleep(1)
				if w0.exists():
					w0.wait(3)
					t1 = w0.getPos()
					if t1 == (0, 0, 1920, 1040):
						pass
					else:
						raise Exception('Something went wrong.')
					sleep(2)
					# 退出反查
					m1.click(self.BECivilWin, '', 1100, 490, button='right')
					sleep(0.5)
					m1.click(self.BECivilWin, '', 1170, 505)
					sleep(2)
					if w1.exists():
						w1.wait(3)
						w1.setState(3)
					else:
						raise Exception('退出反查失败')
				else:
					raise Exception('反查失败')
				sleep(2)
				# 下载
				m1.click('资料管理', '', 1835, 160)
				sleep(2)
				w3 = WinControl('另存为')
				if w3.exists():
					w3.wait(3)
					m1.click('另存为', '', 1030, 45)
					w3.controlSetText('[CLASS:Edit; INSTANCE:2]', self.downloadaddress)
					sleep(1)
					w3.controlClick('[CLASS:Button; INSTANCE:1]')
					sleep(1)
					w4 = WinControl('确认另存为')
					if w4.exists():
						w4.wait(3)
						w4.controlClick('[CLASS:Button; INSTANCE:1]')
					else:
						pass
				else:
					raise Exception('未打开另存为窗口')
				# 勾选上传资料
				m1.click('资料管理', '', 425, 160)
				sleep(1)
				# 关联
				w1.controlClick('[CLASS:Button; INSTANCE:6]')
				sleep(1)
				if w2.exists():
					w2.wait(3)
					w2.controlClick('[CLASS:Button; INSTANCE:3]')
					sleep(2)
					w2.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('未打开设置资料信息窗口')
				sleep(3)
				w1.setState(3)
				# 勾选上传资料
				m1.click('资料管理', '', 425, 160)
				# 打印
				w1.controlClick('[CLASS:Button; INSTANCE:7]')
				sleep(1)
				w5 = WinControl('打印')
				if w5.exists():
					w5.wait(3)
					w5.controlClick('[CLASS:Button; INSTANCE:14]')
				else:
					raise Exception('未打开打印窗口')
				sleep(3)
				w1.setState(3)
				# 删除
				w1.controlClick('[CLASS:Button; INSTANCE:8]')
				sleep(2)
				if w0.exists():
					w0.wait(3)
					t2 = w0.getPos()
					if t2 == (844, 438, 1076, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('删除未成功')
				sleep(3)
				w1.setState(3)
				# 关闭资料管理窗口
				m1.click('资料管理', '', 1905, 10)
			else:
				raise Exception('未打开资料管理窗口')
		else:
			raise Exception('未识别BECivil窗口')


if __name__ == '__main__':
	IF = InformationFunctions()
	
	sleep(2)
	IF.upload_information()
	
	sleep(2)
	IF.information_management()
	