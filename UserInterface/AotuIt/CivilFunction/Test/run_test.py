#! python3
# -*- coding:utf-8 -*-
'''
Title: BECivil功能测试
Description: 系统相关、沙盘、操作、数据、协作、任务、资料
@author: Xushenwei
@update: 2018年1月26日
'''
import unittest, os, sys, time
from time import sleep
sys.path.insert(0,r'D:\AutomatedTestScripts\BE_Civil\Functions')
from Login_BECivil import Login_BECivil as LB 
sys.path.insert(0,r'D:\AutomatedTestScripts\BE_Civil\Functions\系统')
from projectfunctions import ProjectFuncions as PF 
from workingsetfunctions import WorkingSetFunctions as WSF   
sys.path.insert(0,r'D:\AutomatedTestScripts\BE_Civil\Functions\沙盘')
from runsandplate import run_sand_plate as RSP
sys.path.insert(0,r'D:\AutomatedTestScripts\BE_Civil\Functions\操作')
from runtheoperation import run_the_operation as RTO
sys.path.insert(0,r'D:\AutomatedTestScripts\BE_Civil\Functions\数据')
from runthedata import run_the_data as RTA
sys.path.insert(0,r'D:\AutomatedTestScripts\BE_Civil\Functions\协作')
from cooperationfunctions import CooperationFunctions as CF
sys.path.insert(0,r'D:\AutomatedTestScripts\BE_Civil\Functions\任务')
from runthemission import run_the_mission as RTM
sys.path.insert(0,r'D:\AutomatedTestScripts\BE_Civil\Functions\资料')
from runtheinformation import run_the_information as RTI


def now():
	"""返回当前时间"""
	return time.strftime("%Y-%m-%d %H:%M:%S")

def setUp():
		print("test module start >>>>>>>>>>>" + now())




class TestCaseBECivil(unittest.TestCase):

	def setUp(self):
		print("test module start >>>>>>>>>>>" + now())
		LB().start_BECivil()
		print("\n>>>>>>>>成功登陆BECivil")

	def testBECivil(self):
		"""市政相关功能"""
		sleep(2)
		ds = ('测试脚本用土建工程', '测试脚本用安装工程')
		for d in ds:
			PF().upload_project(d)
			sleep(6)
		print("\n>>>>>>>>成功上传两个测试工程")
		sleep(2)
		WSF().manage_working_set()
		sleep(2)
		WSF().creat_working_set()
		sleep(2)	 
		WSF().open_working_set()
		sleep(20)
		PF().open_project('测试脚本用土建工程')
		sleep(20)
		PF().download_porject()
		# 沙盘相关功能
		RSP()
		# 操作相关功能
		RTO()
		PF().open_project('测试脚本用安装工程')
		# 资料相关功能
		RTI()
		# 数据相关功能
		RTA()
		sleep(2)
		#CF().cooperation_management()
		#print("\n>>>>>>>>协作已完成")
		# 任务相关功能
		RTM()
		WSF().clear_cache()
		WSF().quit_BECivil()
		print("\n>>>>>>>>成功关闭软件")

	def tearDown(self):
		PF().delete_project()
		print("\n成功删除工程")
		print("test module end >>>>>>>>>>>" + now())

unittest.main()