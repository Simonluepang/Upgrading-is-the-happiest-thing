#! python3
# -*- coding:utf-8 -*-
'''
Title: 功能操作类
Description: 
@author: Xushenwei
@update: 2017年12月13日
'''
import configparser, screen_point,autoit
from time import sleep
from common_function import verifySystemMetrics, get_base_dir, copy_config
from autoit_function import MouseControl, WinControl, ProcessControl


class Base(object):


	def __init__(self):
		# 读取配置文件
		conf = configparser.ConfigParser()
		conf.read(r"F:\pythondemo\自动化测试脚本\质检计量\IMconfig.ini")
		# 读取安装路径
		self.path = conf.get('install', 'path')
		# 读取登录信息
		self.username = conf.get('login', 'username')
		self.password = conf.get('login', 'password')
		self.ip = conf.get('login', 'ip')
		# 读取进程名称
		self.ShellProcess = conf.get('process', 'Shell')
		self.BECivilProcess = conf.get('process', 'BECivil')
		self.IMProcess = conf.get('process', 'IM')
		self.COProcess = conf.get('process', 'CO')
		self.SuspernsionCtrlProcess = conf.get('process', 'SuspernsionCtrl')
		# 读取窗口名称
		self.BECivilWin = conf.get('window', 'BECivil')
		self.IMWin = conf.get('window', 'IM')

	def start_BECivli(self):
		"""登录BECivil"""

		# 判断屏幕分辨率是否为1920*1080
		if verifySystemMetrics(1920, 1080) == True:
			pass
		else:
			raise Exception("分辨率不为1920*1080，请更改分辨率")

		# 判断Shell、BECivil和IM是否存在，若存在则退出
		processes = [ProcessControl(self.IMProcess), ProcessControl(self.BECivilProcess), ProcessControl(self.ShellProcess)]
		for process in processes:
			if process.exists():
				process.close()

		# 启动软件以及登录
		try:
			autoit.run(self.path)
		except Exception as e:
			print(e)
			print('软件安装路径有误，或者软件安装路径中有中文，\nstart_APP函数中path变量前需要加r！')
		else:
			w1 = WinControl('用户登录')
			w1.wait()
			if w1.exists():
				w1.controlSetText('[CLASS:Edit; INSTANCE:1]', self.username)
				w1.controlSetText('[CLASS:Edit; INSTANCE:2]', self.password)
				w1.controlSetText('[CLASS:Edit; INSTANCE:3]', self.ip)
				w1.controlClick('Button1')
				# 等待BECivil界面
				w2 = WinControl(self.BECivilWin)
				w2.wait(25)
				w2.setState(3)
				sleep(1)
				"""
				# 退出CO进程
				ps = [ProcessControl(self.COProcess), ProcessControl(self.SuspernsionCtrlProcess)]
				for p in ps:
					p.wait(6)
					p.close()
				"""

	def start_IM(self):
		"""启动IM"""

		if WinControl(self.BECivilWin).exists():
			m1 = MouseControl()
			m1.click(self.BECivilWin, '', screen_point.资料[0], screen_point.资料[1])
			sleep(1)
			m1.click(self.BECivilWin, '', screen_point.质检计量[0], screen_point.质检计量[1])
			# 等待IM界面
			w1 = WinControl(self.IMWin)
			w1.wait(30)
			# 关闭筑业升级进程
			if autoit.process_exists("ZY.Downloader.exe"):
				autoit.process_close("ZY.Downloader.exe")
			else:
				pass
			w1.setState(3)
		else:
			print('BECivil未启动，无法启动IM。')

	def quit_BECivil(self):
		"""退出BECivil"""

		p = ProcessControl(self.BECivilProcess)
		if p.exists():
			p.close()

	def quit_IM(self):
		"""退出IM"""

		p = ProcessControl(self.IMProcess)
		if p.exists():
			p.close()


class ContractManagement():


	def __init__(self):
		# 读取配置文件
		conf = configparser.ConfigParser()
		conf.read(r"F:\pythondemo\自动化测试脚本\质检计量\IMconfig.ini")
		# 读取窗口名称
		self.BECivilWin = conf.get('window', 'BECivil')
		self.IMWin = conf.get('window', 'IM')
		# 读取需要输入文字
		self.message1 = conf.get('messages', '合同编号')
		self.message2 = conf.get('messages', '合同金额')
		self.message3 = conf.get('messages', '建设单位')
		self.message4 = conf.get('messages', '施工单位')
		self.message5 = conf.get('messages', '起止桩号')
		self.message6 = conf.get('messages', '合同段长度')
		self.message7 = conf.get('messages', '标段号')
		self.message8 = conf.get('messages', '项目名称')
		self.message9 = conf.get('messages', '监理名称')
		self.message10 = conf.get('messages', '结束桩号')
		self.message11 = conf.get('messages', '工期')
		self.message12 = conf.get('messages', '施工负责人')
		self.message13 = conf.get('messages', '总监理工程师')
		self.message14 = conf.get('messages', '项目总工')

	def creat_contract_management(self):
		# 新增合同

		if WinControl(self.IMWin).exists():
			m1 = MouseControl()
			m1.click(self.IMWin, '', screen_point.选择项目部[0], screen_point.选择项目部[1])
			sleep(1)
			m1.click(self.IMWin, '', screen_point.工程管理[0], screen_point.工程管理[1])
			m1.click(self.IMWin, '', screen_point.合同管理[0], screen_point.合同管理[1])
			m1.click(self.IMWin, '', screen_point.新增施工合同[0], screen_point.新增施工合同[1])
			sleep(5)
			m1.click(self.IMWin, '', screen_point.合同编号[0], screen_point.合同编号[1])
			autoit.send(self.message1)
			m1.click(self.IMWin, '', screen_point.合同金额[0], screen_point.合同金额[1])
			autoit.send(self.message2)
			m1.click(self.IMWin, '', screen_point.合同签订日期[0], screen_point.合同签订日期[1])
			m1.click(self.IMWin, '', screen_point.今天签订[0], screen_point.今天签订[1])
			m1.click(self.IMWin, '', screen_point.建设单位[0], screen_point.建设单位[1])
			autoit.send(self.message3)
			m1.click(self.IMWin, '', screen_point.施工单位[0], screen_point.施工单位[1])
			autoit.send(self.message4)
			m1.click(self.IMWin, '', screen_point.起止桩号[0], screen_point.起止桩号[1])
			autoit.send(self.message5)
			m1.click(self.IMWin, '', screen_point.合同段长度[0], screen_point.合同段长度[1])
			autoit.send(self.message6)
			m1.click(self.IMWin, '', screen_point.计划开工日期[0], screen_point.计划开工日期[1])
			m1.click(self.IMWin, '', screen_point.今天开工[0], screen_point.今天开工[1])
			m1.click(self.IMWin, '', screen_point.标段号[0], screen_point.标段号[1])
			autoit.send(self.message7)
			m1.click(self.IMWin, '', screen_point.项目名称[0], screen_point.项目名称[1])
			autoit.send(self.message8)
			m1.click(self.IMWin, '', screen_point.监理名称[0], screen_point.监理名称[1])
			autoit.send(self.message9)
			m1.click(self.IMWin, '', screen_point.结束桩号[0], screen_point.结束桩号[1])
			autoit.send(self.message10)
			m1.click(self.IMWin, '', screen_point.计划完工日期[0], screen_point.计划完工日期[1])
			m1.click(self.IMWin, '', screen_point.今天完工[0], screen_point.今天完工[1])
			m1.move(self.IMWin, '', 960, 590)
			autoit.mouse_wheel('down', 2)
			m1.click(self.IMWin, '', screen_point.工期[0], screen_point.工期[1])
			autoit.send(self.message11)
			m1.click(self.IMWin, '', screen_point.保存[0], screen_point.保存[1])
		else:
			raise Exception('没有检测到IM窗口！')

	def edit_contract_management(self):
		"""编辑合同"""

		if WinControl(self.IMWin).exists():
			m1 = MouseControl()
			m1.click(self.IMWin, '', screen_point.编辑施工合同[0], screen_point.编辑施工合同[1])
			sleep(3)
			m1.click(self.IMWin, '', screen_point.施工负责人[0], screen_point.施工负责人[1])
			autoit.send(self.message12)
			m1.click(self.IMWin, '', screen_point.总监理工程师[0], screen_point.总监理工程师[1])
			autoit.send(self.message13)
			m1.click(self.IMWin, '', screen_point.项目总工[0], screen_point.项目总工[1])
			autoit.send(self.message14)
			m1.click(self.IMWin, '', screen_point.保存[0], screen_point.保存[1])
		else:
			raise Exception('没有检测到IM窗口！')

	def delete_contract_managemeng(self):
		"""删除合同"""

		if WinControl(self.IMWin).exists():
			m1 = MouseControl()
			m1.click(self.IMWin, '', screen_point.工程管理[0], screen_point.工程管理[1])
			m1.click(self.IMWin, '', screen_point.合同管理[0], screen_point.合同管理[1])
			m1.click(self.IMWin, '', screen_point.删除施工合同[0], screen_point.删除施工合同[1])
			m1.click(self.IMWin, '', screen_point.确认删除合同[0], screen_point.确认删除合同[1])
		else:
			raise Exception('没有检测到IM窗口！')


# 检查各对象是否出错
if __name__ == '__main__':
	b = Base()
	cm = ContractManagement()
	b.start_BECivli()
	b.start_IM()
	sleep(30)
	cm.creat_contract_management()
	sleep(25)
	cm.edit_contract_management()
	#cm.delete_contract_managemeng()
	#b.quit_IM()
	#b.quit_BECivil()
