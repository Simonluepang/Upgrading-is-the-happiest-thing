#! python3
# -*- coding:utf-8 -*-
'''
Title: 操作相关功能
Description:构建搜索、导出二维码、添加节点、节点管理
@author: Xushenwei
@update: 2018年1月26日
'''
import sys, configparser, autoit, pymysql, operator
from time import sleep
sys.path.insert(0, r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from autoit_function import MouseControl, WinControl, ProcessControl
from time import sleep

class OperationFunctions():
	"""操作相关功能"""
	def __init__(self):
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		self.BECivilWin = conf.get('parameters', 'win_BECivil')
		self.BWWin = conf.get('parameters', 'win_BW')
		self.downloadaddress = conf.get('parameters', 'downloadaddress')
		self.uploadaddress = conf.get('parameters', 'uploadaddress')

	def component_search(self):
		"""构建搜索"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.操作[0], screen_point.操作[1])
			m1.click(self.BECivilWin, '', screen_point.构件搜索[0], screen_point.构件搜索[1])
			w1 = WinControl('构件搜索')
			sleep(2)
			if w1.exists():
				w1.wait(2)
				w1.controlSetText('[CLASS:Edit; INSTANCE:1]', 'TWQ2')
				w1.controlClick('[CLASS:Button; INSTANCE:5]')
				sleep(2)
				w1.controlClick('[CLASS:Button; INSTANCE:1]')
				sleep(2)
				w2 = WinControl('搜索结果')
				if w2.exists():
					w2.wait(3)
					w2.controlClick('[CLASS:Button; INSTANCE:3]')
				else:
					raise Exception("未打开搜索结果窗口")
			else:
				raise Exception("未打开构件搜索窗口")
			sleep(2)
			m1.click(self.BECivilWin, '', screen_point.构件搜索[0], screen_point.构件搜索[1])
		else:
			raise Exception("未识别BECivil窗口")

	def export_the_qr_code(self):
		"""导出二维码"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.操作[0], screen_point.操作[1])
			m1.click(self.BECivilWin, '', screen_point.导出二维码[0], screen_point.导出二维码[1])
			# 选中需要导出二维码的构件
			m1.click(self.BECivilWin, '', 810, 500)
			# 右键导出
			m1.click(self.BECivilWin, '', 810, 500, button='right')
			m1.click(self.BECivilWin, '', 730, 510)
			sleep(2)
			w1 = WinControl('选择文件夹')
			if w1.exists():
				w1.wait(3)
				w1.controlSetText('[CLASS:Edit; INSTANCE:1]', self.downloadaddress + '\二维码下载')
				sleep(1)
				w1.controlClick('[CLASS:Button; INSTANCE:1]')
			else:
				raise Exception("未打开选择文件夹窗口")
			sleep(3)
			if w0.exists():
				w0.wait(3)
				t = w0.getPos()
				if t == (862, 438, 1058, 602):
					pass
				else:
					raise Exception('Something went wrong.')
				sleep(1)
				w0.controlClick('[CLASS:Button; INSTANCE:1]')
			else:
				raise Exception("未弹出导出二维码成功窗口")
		else:
			raise Exception("未识别BECivil窗口")

	def add_node(self):
		"""添加钢筋节点"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			sleep(2)
			# 使视图视角变为俯视视角
			m1.click(self.BECivilWin, '', 440, 440, button='right')
			m1.click(self.BECivilWin, '', 490, 475)
			m1.click(self.BECivilWin, '', screen_point.操作[0], screen_point.操作[1])
			m1.click(self.BECivilWin, '', screen_point.插入节点[0], screen_point.插入节点[1])
			w1 = WinControl('插入节点')
			sleep(1)
			if w1.exists():
				w1.wait(3)
				# 上传文件
				m1.click('插入节点', '', 970, 360)
				sleep(1)
				w2 = WinControl('打开')
				if w2.exists():
					w2.wait(3)
					m1.click('打开', '', 1000, 50)
					w2.controlSetText('[CLASS:Edit; INSTANCE:2]', self.uploadaddress)
					autoit.send("{ENTER}")
					sleep(1)
					w2.controlSetText('[CLASS:Edit; INSTANCE:1]', '钢筋节点 (2).lbg')
					w2.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('未打开上传节点文件窗口')
				sleep(2)
				# 详细位置
				m1.click('插入节点', '', 970, 450)
				sleep(1)
				# 选择要插入节点的位置
				m1.click(self.BECivilWin, '', 1050, 504)
				m1.click(self.BECivilWin, '', 1050, 504, button='right')
				sleep(1)
				m1.click(self.BECivilWin, '', 1100, 514)
				sleep(2)
				w1.controlClick('[CLASS:Button; INSTANCE:1]')
				sleep(5)
				if w0.exists():
					w0.wait(3)
					t = w0.getPos()
					if t == (862, 438, 1058, 602):
						pass
					else:
						raise Exception('Something went wrong.')
					w0.controlClick('[CLASS:Button; INSTANCE:1]')
				else:
					raise Exception('节点插入未成功')
			else:
				raise Exception('未打开插入节点窗口')
		else:
			raise Exception('未识别BECivil窗口')


	def node_management(self):
		"""节点管理"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.操作[0], screen_point.操作[1])
			m1.click(self.BECivilWin, '', screen_point.节点管理[0], screen_point.节点管理[1])
			w1 = WinControl('节点管理')
			sleep(1)
			if w1.exists():
				w1.wait(3)
				w1.setState(3)
				# 点击预览
				m1.click('节点管理', '', 1510, 100)
				sleep(2)
				w2 = WinControl('预览窗口 ')
				if w2.exists():
					w2.wait(3)
					w2.setState(3)
					# 关闭预览窗口
					m1.click('预览窗口 ', '', 1910, 10)
				else:
					raise Exception('未打开预览窗口')
				sleep(2)
				# 点击编辑
				m1.click('节点管理', '', 1550, 100)
				sleep(2)
				w3 = WinControl('编辑节点')
				if w3.exists():
					w3.wait(3)
					# 点击节点名称
					m1.click('编辑节点', '', 970, 390, clicks=2)
					autoit.send('新建1')
					# 更改图钉颜色
					m1.click('编辑节点', '', 970, 425)
					sleep(0.5)
					m1.click('编辑节点', '', 970, 490)
					sleep(1)
					# 添加节点备注
					m1.click('编辑节点', '', 970, 520)
					autoit.send('备注123')
					sleep(1)
					w3.controlClick("[CLASS:Button; INSTANCE:1]")
					sleep(2)
					if w0.exists():
						w0.wait(3)
						t1 = w0.getPos()
						if t1 == (862, 438, 1058, 602):
							pass
						else:
							raise Exception('Something went wrong.')
						w0.controlClick('[CLASS:Button; INSTANCE:1]')
					else:
						raise Exception("未成功编辑节点")
				else:
					raise Exception('未打开编辑节点窗口')
				# 点击删除
				m1.click('节点管理', '', 1630, 100)
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
					raise Exception('未成功删除节点')
				sleep(1)
				# 关闭节点管理窗口
				m1.click('节点管理', '', 1910, 10)
			else:
				raise Exception('未打开节点管理窗口')
		else:
			raise Exception('未识别BECivil窗口')







if __name__ == '__main__':
	OF = OperationFunctions()
	'''
	sleep(2)
	OF.component_search()
	
	sleep(2)
	OF.export_the_qr_code()
	
	sleep(2)
	OF.add_node()
	'''
	sleep(2)
	OF.node_management()
	