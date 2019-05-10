#! python3
# -*- coding:utf-8 -*-
'''
Title: 数据相关功能
Description:查看报表、对应出量
@author: Xushenwei
@update: 2018年1月26日
'''
import sys, configparser, autoit, pymysql, operator
from time import sleep
sys.path.insert(0, r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from autoit_function import MouseControl, WinControl, ProcessControl
from time import sleep

class DataFunctions():
	"""数据相关功能"""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')
		self.BWWin = conf.get('parameters', 'win_BW')
		self.downloadaddress = conf.get('parameters', 'downloadaddress')
		self.uploadaddress = conf.get('parameters', 'uploadaddress')

	def viewing_reports(self):
		"""查看报表"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.数据[0], screen_point.数据[1])
			m1.click(self.BECivilWin, '', screen_point.查看报表[0], screen_point.查看报表[1])
			sleep(2)
			w1 = WinControl('报表（Civil）')
			if w1.exists():
				w1.wait(3)
				# 条件统计
				m1.click('报表（Civil）', '', 40, 70)
				sleep(1)
				w2 = WinControl('条件统计')
				if w2.exists():
					w2.wait(3)
					# 勾选全部楼层
					m1.click('条件统计', '', 740, 410)
					sleep(1)
					# 勾选全部构件
					m1.click('条件统计', '', 975, 410)
					sleep(1)
					w2.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					raise Exception("未打开条件统计窗口")
				# 选中构件
				m1.click('报表（Civil）', '', 860, 260, clicks=2)
				# 点击反查
				m1.click('报表（Civil）', '', 100, 70)
				sleep(2)
				w3 = WinControl('反查结果')
				if w3.exists():
					w3.wait(3)
					sleep(2)
					w3.controlClick('[CLASS:Button; INSTANCE:3]')
				else:
					raise Exception("未打开反查结果窗口")
				sleep(1)
				# 打印预览
				m1.click('报表（Civil）', '', 290, 70)
				sleep(2)
				w4 = WinControl('打印预览 - 你的报表标题')
				if w4.exists():
					w4.wait(3)
					# 退出打印预览
					m1.click('打印预览 - 你的报表标题', '', 1890, 10)
				else:
					raise Exception('未打开打印预览窗口')
				sleep(2)
				# 导出Excel
				m1.click('报表（Civil）', '', 360, 70)
				sleep(2)
				w5 = WinControl('另存为')
				if w5.exists():
					w5.wait(3)
					w5.setState(3)
					m1.click('另存为', '', 860, 45)
					w5.controlSetText('[CLASS:Edit; INSTANCE:2]', self.downloadaddress)
					autoit.send("{ENTER}")
					sleep(2)
					w5.controlClick('[CLASS:Button; INSTANCE:1]')
					sleep(2)
					w6 = WinControl('确认另存为')
					if w6.exists():
						w6.wait(3)
						w6.controlClick('[CLASS:Button; INSTANCE:1]')
					else:
						pass
				else:
					raise Exception("未打开另存为窗口")
				sleep(15)
				w7 = WinControl('测试脚本用安装工程.YS_清单定额汇总表.xls  [兼容模式] - Excel')
				if w7.exists():
					w7.wait(3)
					w7.setState(3)
					sleep(3)
					# 关闭自动打开的Excel
					m1.click('测试脚本用安装工程.YS_清单定额汇总表.xls  [兼容模式] - Excel', '', 1905, 12)
				else:
					raise Exception("未打开Excel")
				sleep(2)
				# 导出PDF
				m1.click('报表（Civil）', '', 435, 70)
				sleep(2)
				w8 = WinControl('另存为')
				if w8.exists():
					w8.wait(3)
					w8.setState(3)
					m1.click('另存为', '', 860, 45)
					w8.controlSetText('[CLASS:Edit; INSTANCE:2]', self.downloadaddress)
					autoit.send("{ENTER}")
					sleep(2)
					w5.controlClick('[CLASS:Button; INSTANCE:1]')
					sleep(2)
					w9 = WinControl('确认另存为')
					if w9.exists():
						w9.wait(3)
						w9.controlClick('[CLASS:Button; INSTANCE:1]')
					else:
						pass
				else:
					raise Exception("未打开另存为窗口")
				sleep(7)
				w10 = WinControl('你的报表标题 - 测试脚本用安装工程.YS_清单定额汇总表.pdf - Mozilla Firefox')
				if w10.exists():
					w10.wait(3)
					w10.setState(3)
					sleep(3)
					# 关闭自动打开的Excel
					m1.click('你的报表标题 - 测试脚本用安装工程.YS_清单定额汇总表.pdf - Mozilla Firefox', '', 1893, 7)
					sleep(2)
					w11 = WinControl("确认关闭")
					if w11.exists():
						w11.wait(3)
						autoit.send("{ENTER}")
				else:
					raise Exception("未打开PDF")
				sleep(1)
				# 报表管理
				m1.click('报表（Civil）', '', 500, 70)
				sleep(2)
				w12 = WinControl('报表管理')
				if w12.exists():
					w12.wait(3)
					w12.controlClick('[CLASS:Button; INSTANCE:4]')
					sleep(2)
					w13 = WinControl('打开')
					if w13.exists():
						w13.wait(3)
						m1.click('打开', '', 1030, 45)
						w13.controlSetText('[CLASS:Edit; INSTANCE:2]', self.uploadaddress)
						sleep(1)
						autoit.send("{ENTER}")
						w13.controlSetText('[CLASS:Edit; INSTANCE:1]', '测试脚本用上传报表.xlsx')
						sleep(1)
						w13.controlClick("[CLASS:Button; INSTANCE:1]")
						sleep(5)
						w14 = WinControl('上传报表')
						if w14.exists():
							w14.wait(3)
							w14.controlClick('[CLASS:Button; INSTANCE:1]')
						else:
							raise Exception('未打开上传报表窗口')
					else:
						raise Exception("未打开打开窗口")
					# 关闭报表管理
					m1.click('报表管理', '', 1314, 243)
					sleep(2)
				else:
					raise Exception('未打开报表管理窗口')
				# 关闭报表窗口
				m1.click('报表（Civil）', '', 1895, 5)
			else:
				raise Exception('未打开报表（Civil）窗口')
		else:
			raise Exception('未识别BECivil窗口')


	def corresponding_output(self):
		"""对应出量"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', 1090, 570)
			m1.click(self.BECivilWin, '', screen_point.数据[0], screen_point.数据[1])
			m1.click(self.BECivilWin, '', screen_point.对应出量[0], screen_point.对应出量[1])
			sleep(2)
			w1 = WinControl('报表（Civil）')
			if w1.exists():
				w1.wait(3)
				# 选中构件
				m1.click('报表（Civil）', '', 860, 260, clicks=2)
				# 点击反查
				m1.click('报表（Civil）', '', 100, 70)
				sleep(2)
				w3 = WinControl('反查结果')
				if w3.exists():
					w3.wait(3)
					sleep(2)
					w3.controlClick('[CLASS:Button; INSTANCE:3]')
				else:
					raise Exception("未打开反查结果窗口")
				
				sleep(1)
				# 打印预览
				m1.click('报表（Civil）', '', 290, 70)
				sleep(2)
				w4 = WinControl('打印预览 - 你的报表标题')
				if w4.exists():
					w4.wait(3)
					# 退出打印预览
					m1.click('打印预览 - 你的报表标题', '', 1890, 10)
				else:
					raise Exception('未打开打印预览窗口')
				sleep(2)
				# 导出Excel
				m1.click('报表（Civil）', '', 360, 70)
				sleep(2)
				w5 = WinControl('另存为')
				if w5.exists():
					w5.wait(3)
					w5.setState(3)
					m1.click('另存为', '', 860, 45)
					w5.controlSetText('[CLASS:Edit; INSTANCE:2]', self.downloadaddress)
					autoit.send("{ENTER}")
					sleep(2)
					w5.controlClick('[CLASS:Button; INSTANCE:1]')
					sleep(2)
					w6 = WinControl('确认另存为')
					if w6.exists():
						w6.wait(3)
						w6.controlClick('[CLASS:Button; INSTANCE:1]')
					else:
						pass
				else:
					raise Exception("未打开另存为窗口")
				sleep(15)
				w7 = WinControl('测试脚本用安装工程.YS_对应工程量.xls  [兼容模式] - Excel')
				if w7.exists():
					w7.wait(3)
					w7.setState(3)
					sleep(3)
					# 关闭自动打开的Excel
					m1.click('测试脚本用安装工程.YS_对应工程量.xls  [兼容模式] - Excel', '', 1905, 12)
				else:
					raise Exception("未打开Excel")
				sleep(2)
				# 导出PDF
				m1.click('报表（Civil）', '', 435, 70)
				sleep(2)
				w8 = WinControl('另存为')
				if w8.exists():
					w8.wait(3)
					w8.setState(3)
					m1.click('另存为', '', 860, 45)
					w8.controlSetText('[CLASS:Edit; INSTANCE:2]', self.downloadaddress)
					autoit.send("{ENTER}")
					sleep(2)
					w5.controlClick('[CLASS:Button; INSTANCE:1]')
					sleep(2)
					w9 = WinControl('确认另存为')
					if w9.exists():
						w9.wait(3)
						w9.controlClick('[CLASS:Button; INSTANCE:1]')
					else:
						pass
				else:
					raise Exception("未打开另存为窗口")
				sleep(7)
				w10 = WinControl('你的报表标题 - 测试脚本用安装工程.YS_对应工程量.pdf - Mozilla Firefox')
				if w10.exists():
					w10.wait(3)
					w10.setState(3)
					sleep(3)
					# 关闭自动打开的Excel
					m1.click('你的报表标题 - 测试脚本用安装工程.YS_对应工程量.pdf - Mozilla Firefox', '', 1893, 7)
					sleep(2)
					w11 = WinControl("确认关闭")
					if w11.exists():
						w11.wait(3)
						autoit.send("{ENTER}")
				else:
					raise Exception("未打开PDF")
				sleep(1)
				# 报表管理
				m1.click('报表（Civil）', '', 500, 70)
				sleep(2)
				w12 = WinControl('报表管理')
				if w12.exists():
					w12.wait(3)
					m1.click('报表管理', '', 1300, 340)
					sleep(2)
					w12.controlClick('[CLASS:Button; INSTANCE:4]')
					sleep(2)
					w13 = WinControl('打开')
					if w13.exists():
						w13.wait(3)
						m1.click('打开', '', 1030, 45)
						w13.controlSetText('[CLASS:Edit; INSTANCE:2]', self.uploadaddress)
						sleep(1)
						autoit.send("{ENTER}")
						w13.controlSetText('[CLASS:Edit; INSTANCE:1]', '测试脚本用上传报表.xlsx')
						sleep(1)
						w13.controlClick("[CLASS:Button; INSTANCE:1]")
						sleep(5)
						w14 = WinControl('上传报表')
						if w14.exists():
							w14.wait(3)
							w14.controlClick('[CLASS:Button; INSTANCE:1]')
						else:
							raise Exception('未打开上传报表窗口')
					else:
						raise Exception("未打开打开窗口")
					# 关闭报表管理
					m1.click('报表管理', '', 1314, 243)
					sleep(2)
				else:
					raise Exception('未打开报表管理窗口')
				# 关闭报表窗口
				m1.click('报表（Civil）', '', 1895, 5)
			else:
				raise Exception('未打开报表（Civil）窗口')
		else:
			raise Exception('未识别BECivil窗口')


if __name__ == '__main__':
	DF = DataFunctions()
	sleep(2)
	DF.viewing_reports()
	sleep(2)
	DF.corresponding_output()