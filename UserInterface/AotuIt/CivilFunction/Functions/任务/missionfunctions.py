#! python3
# -*- coding:utf-8 -*-
'''
Title: 任务相关功能
Description:测点管理、监测报告、设置点位图管理
@author:
@update:
'''
import sys, configparser, autoit, pymysql, operator
from time import sleep
sys.path.insert(0, r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from autoit_function import MouseControl, WinControl, ProcessControl
from time import sleep


class MissionFunctions():
	"""任务相关功能"""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')
		self.BWWin = conf.get('parameters', 'win_BW')
		self.downloadaddress = conf.get('parameters', 'downloadaddress')
		self.uploadaddress = conf.get('parameters', 'uploadaddress')

	def measure_point_management(self):
		"""测点管理"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.任务[0], screen_point.任务[1])
			m1.click(self.BECivilWin, '', screen_point.测点管理[0], screen_point.测点管理[1])
			sleep(1)
			# 无法识别测点列表窗口
			# 添加
			m1.click(self.BECivilWin, '', 1185, 270)
			sleep(1)
			w1 = WinControl('新建测点')
			if w1.exists():
				w1.wait(3)
				# 选择深层位移
				m1.click('新建测点', '', 980, 445)
				sleep(1)
				m1.click('新建测点', '', 980, 515)
				sleep(1)
				# 测点名称
				m1.click('新建测点', '', 980, 480)
				autoit.send('测点名称123')
				sleep(1)
				# 选择位置
				m1.click('新建测点', '', 850, 520)
				sleep(1)
				m1.click(self.BECivilWin, '', 750, 620)
				m1.click(self.BECivilWin, '', 750, 620, button='right')
				m1.click(self.BECivilWin, '', 710, 635)
				sleep(1)
				w1.controlClick("[CLASS:Button; INSTANCE:1]")
			else:
				raise Exception('未打开新建测点窗口')
			sleep(2)
			# 数据读取
			m1.click(self.BECivilWin, '', 1380, 270)
			sleep(1)
			w2 = WinControl("打开")
			if w2.exists():
				w2.wait(3)
				m1.click('打开', '', 940, 45)
				w2.controlSetText('[CLASS:Edit; INSTANCE:2]', self.uploadaddress)
				autoit.send("{ENTER}")
				sleep(1)
				w2.controlSetText('[CLASS:Edit; INSTANCE:1]', '测点数据读取模板.xlsx')
				w2.controlClick('[CLASS:Button; INSTANCE:1]')
				sleep(2)
				w3 = WinControl('数据读取设置')
				if w3.exists():
					w3.wait(3)
					# 数据表名
					m1.click('数据读取设置', '', 980, 435)
					sleep(1)
					# 深层位移
					m1.click('数据读取设置', '', 980, 455)
					sleep(1)
					# 数据类型
					m1.click('数据读取设置', '', 980, 470)
					sleep(1)
					# 深层位移
					m1.click('数据读取设置', '', 980, 597)
					sleep(1)
					w3.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('未打开数据读取设置窗口')
			else:
				raise Exception('未识别打开窗口')
			sleep(1)
			# 关闭测点管理
			m1.click(self.BECivilWin, '', screen_point.测点管理[0], screen_point.测点管理[1])
		else:
			raise Exception("未识别市政窗口")

	def setting(self):
		"""设置"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.任务[0], screen_point.任务[1])
			m1.click(self.BECivilWin, '', screen_point.设置[0], screen_point.设置[1])
			'''
			m1.click(self.BECivilWin, '', screen_point.设置[0], 140)# 仪器信息
			sleep(1)
			w1 = WinControl('仪器信息')
			if w1.exists():
				w1.wait(3)
				w1.controlClick('[CLASS:Button; INSTANCE:1]')
				sleep(1)
				m1.click('仪器信息', '', 910, 650)
				autoit.send('测试脚本用添加仪器')
				m1.click('仪器信息', '', 1080, 650)
				autoit.send('134652')
				autoit.send("{ENTER}")
				m1.click('仪器信息', '', 1180, 370)# 关闭仪器信息
			else:
				raise Exception('未打开仪器信息窗口')
			sleep(1)
			m1.click(self.BECivilWin, '', screen_point.设置[0], screen_point.设置[1])
			'''
			# 点位图管理
			m1.click(self.BECivilWin, '', screen_point.设置[0], 160)
			sleep(2)
			w2 = WinControl('点位图管理')
			if w2.exists():
				w2.wait(3)
				w2.controlClick("[CLASS:Button; INSTANCE:1]")
				sleep(1)
				# 截图点位图
				m1.click(self.BECivilWin, '', 710, 390, button='right')
				m1.click(self.BECivilWin, '', 660, 405)
				sleep(2)
				w3 = WinControl('点位图命名')
				if w3.exists():
					w3.wait(3)
					w3.controlSetText('[CLASS:Edit; INSTANCE:1]', '测试脚本用点位图')
					sleep(1)
					w3.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('未打开点位图命名窗口')
				sleep(1)
				# 关闭点位图管理
				m1.click('点位图管理', '', 1336, 183)
			else:
				raise Exception('未打开点位图管理窗口')
		else:
			raise Exception('未识别市政窗口')

	def add_form(self, y1=515, message='封面'):
		"""添加表单用"""
		w0 = WinControl("添加表单")
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click('添加表单', '', 990, 495)
			sleep(1)
			m1.click('添加表单', '', 990, y1)
			sleep(0.5)
			m1.click('添加表单', '', 990, 530)
			autoit.send(message)
			sleep(0.5)
			w0.controlClick("[CLASS:Button; INSTANCE:1]")
		else:
			raise Exception('添加表单未成功')


	def measure_report(self):
		"""监测报告"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.任务[0], screen_point.任务[1])
			m1.click(self.BECivilWin, '', screen_point.监测报告[0], screen_point.监测报告[1])
			sleep(1)
			# 创建报告
			m1.click(self.BECivilWin, '', 1190, 270)
			sleep(1)
			w1 = WinControl("新建报告")
			if w1.exists():
				w1.wait(3)
				# 报告名称
				m1.click('新建报告', '', 980, 400)
				autoit.send('测试脚本用报告')
				# 期号
				m1.click('新建报告', '', 980, 440)
				autoit.send('1')
				# 编号
				m1.click('新建报告', '', 980, 480)
				autoit.send('123456')
				# 承包单位
				m1.click('新建报告', '', 980, 570)
				autoit.send('测试脚本用承包单位')
				# 监理单位
				m1.click('新建报告', '', 980, 615)
				autoit.send('测试脚本用监理单位')
				sleep(1)
				w1.controlClick('[CLASS:Button; INSTANCE:1]')
			else:
				raise Exception('未打开新建报告窗口')
			# 点击名称
			m1.click(self.BECivilWin, '', 1320, 340)
			sleep(2)
			w2 = WinControl("表单列表")
			if w2.exists():
				w2.wait(3)
				w2.controlClick("[CLASS:Button; INSTANCE:1]")
				sleep(1)
				MissionFunctions().add_form()
				sleep(1)
				w2.controlClick("[CLASS:Button; INSTANCE:1]")
				sleep(1)
				MissionFunctions().add_form(565, '脚本测试用监测成果分析报告')
				m1.click('表单列表', '', 1260, 235)
			else:
				raise Exception('未打开表单列表窗口')
			# 点击编辑
			m1.click(self.BECivilWin, '', 1800, 340)
			sleep(1)
			w3 = WinControl("编辑报告")
			if w3.exists():
				w3.wait(3)
				m1.click('编辑报告', '', 960, 400)
				autoit.send('测试脚本用报告更改')
				sleep(1)
				w3.controlClick("[CLASS:Button; INSTANCE:1]")
			else:
				raise Exception("未打开编辑报告窗口")
			# 点击导出
			m1.click(self.BECivilWin, '', 1860, 340)
			sleep(1)
			w4 = WinControl('另存为')
			if w4.exists():
				w4.wait(3)
				m1.click('另存为', '', 1030, 45)
				w4.controlSetText("[CLASS:Edit; INSTANCE:2]", self.downloadaddress)
				sleep(1)
				w4.controlClick('[CLASS:Button; INSTANCE:1]')
				sleep(1)
				w5 = WinControl('确认另存为')
				if w5.exists():
					w5.wait(3)
					w5.controlClick("[CLASS:Button; INSTANCE:1]")
				else:
					pass
				sleep(2)
				if w0.exists():
					w0.wait(3)
					t1 = w0.getPos()
					if t1 == (845, 438, 1075, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick("[CLASS:Button; INSTANCE:2]")
				else:
					pass
			else:
				raise Exception('未成功导出报告')
			sleep(2)
			# 全部勾选报告
			m1.click(self.BECivilWin, '', 1172, 340)
			sleep(1)
			# 删除
			m1.click(self.BECivilWin, '', 1290, 270)
			sleep(1)
			if w0.exists():
				w0.wait(3)
				t2 = w0.getPos()
				if t2 == (845, 438, 1075, 602):
					pass
				else:
					raise Exception('Something went wrong.')
				w0.controlClick("[CLASS:Button; INSTANCE:1]")
			else:
				raise Exception('删除报告失败')
				sleep(1)
			m1.click(self.BECivilWin, '', screen_point.监测报告[0], screen_point.监测报告[1])
		else:
			raise Exception('未识别市政窗口')


if __name__ == '__main__':
	MF = MissionFunctions()
	'''
	sleep(2)
	MF.measure_point_management()
	
	sleep(2)
	MF.setting()
	'''
	sleep(2)
	MF.measure_report()
