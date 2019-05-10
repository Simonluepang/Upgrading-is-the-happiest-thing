#！ python3
# -*- coding:utf-8 -*-
'''
Title: 软件登录相关类
Description: 
@author: Xushenwei
@update: 2018年1月26日
'''
import configparser,autoit,sys
from time import sleep
sys.path.insert(0,r'D:\AutomatedTestScripts\BE_Civil\Functions\basic_functions')
import screen_point
from common_function import verifySystemMetrics, get_base_dir, copy_config
from autoit_function import MouseControl, WinControl, ProcessControl


class Login_BECivil(object):


	def __init__(self):
		# 读取配置文件
		conf = configparser.ConfigParser()
		conf.read(r"D:\AutomatedTestScripts\BE_Civil\ConfigurationFiles\MainConfig.ini")
		# 读取安装路径
		self.path = conf.get('parameters', r'path')
		# 读取登录信息
		self.username = conf.get('parameters', 'username')
		self.password = conf.get('parameters', 'password')
		self.ip = conf.get('parameters', 'ip')
		# 读取进程名称
		self.ShellProcess = conf.get('parameters', 'process_shell')
		self.BECivilProcess = conf.get('parameters', 'process_client')
		self.IMProcess = conf.get('parameters', 'process_IM')
		self.COProcess = conf.get('parameters', 'process_co')
		self.SuspernsionCtrlProcess = conf.get('parameters', 'process_coas')
		self.ZYDLProcess = conf.get('parameters', 'process_ZYDL')
		self.ZYCAProcess = conf.get('parameters', 'process_ZYCA')
		# 读取窗口名称
		self.BECivilWin = conf.get('parameters', 'win_BECivil')

	def start_BECivil(self):
		"""登录BECivil"""

		# 判断屏幕分辨率是否为1920*1080
		if verifySystemMetrics(1920, 1080) == True:
			pass
		else:
			raise Exception("分辨率不为1920*1080，请更改分辨率")
		sleep(5)

		# 初始化登录环境
		processes = [ProcessControl(self.IMProcess), ProcessControl(self.BECivilProcess), ProcessControl(self.ShellProcess)]
		for process in processes:
			if process.exists():
				process.close()
			else:
				pass

		sleep(2)
		# 启动软件以及登录
		try:
			autoit.run(self.path)
		except Exception as e:
			print(e)
			print('软件安装路径有误，或者软件安装路径中有中文，\nstart_APP函数中path变量前需要加r！')
		else:
			sleep(3)
			w1 = WinControl('用户登录')
			if w1.exists():
				w1.wait()
				w1.controlSetText('[CLASS:Edit; INSTANCE:1]', self.username)
				w1.controlSetText('[CLASS:Edit; INSTANCE:2]', self.password)
				w1.controlSetText('[CLASS:Edit; INSTANCE:3]', self.ip)
				w1.controlClick('Button1')
				sleep(20)
				# 如果检测到升级则进行升级过程，若没有则pass
				w2 = WinControl("Luban Explorer（Civil）版本获取")
				if w2.exists():
					w2.wait(60)
					print('>>>>>>>>检测到LubanBECivil正在升级')
					sleep(60)
				else:
					pass
					print('软件未升级')
				sleep(3)
				# 等待BECivil界面
				w3 = WinControl(self.BECivilWin)
				w3.wait(60)
				if w3.exists():
					#w3.wait(60)
					sleep(5)
					w4 = WinControl('启动提示')
					if w4.exists():
						w4.wait(3)
						w4.controlClick('[CLASS:Button; INSTANCE:1]')
						print('软件弹出了启动提示')
					else:
						pass
					w3.wait(60)
					w3.setState(3)
					sleep(15)
				else:
					raise Exception("未识别BECivil打开的窗口")

				# 检测CO进程并退出
				ps = [ProcessControl(self.COProcess), ProcessControl(self.SuspernsionCtrlProcess)]
				for p in ps:
					if p.exists():
						p.wait(6)
						p.close()
					else:
						print("未启动鲁班协作")
			else:
				raise Exception("未打开用户登录窗口")
				
	def quit_BECivil(self):
		"""退出BECivil"""
		w0 = WinControl(self.BECivilWin)
		if w0.exists():
			m1 = MouseControl()
			w0.wait(3)
			m1.click(self.BECivilWin, '', 1900, 13)
			if w0.exists():
				w0.wait(3)
				t = w0.getPos()
				if t == (845, 438, 1075, 602):
					pass
				else:
					raise Exception('Something went wrong.')
				sleep(1)
				w0.controlClick('[CLASS:Button; INSTANCE:1]')
			else:
				raise Exception('未弹出确认关闭软件窗口')
		else:
			raise Exception('未识别BECivil打开的窗口')
		sleep(5)
		if w0.exists():
			raise Exception('关闭软件未成功')
		else:
			pass

if __name__ == '__main__':
	b = Login_BECivil()
	b.start_BECivil()
	sleep(2)
	b.quit_BECivil()