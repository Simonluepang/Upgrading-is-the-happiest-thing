#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 测试用例
Description: 合同管理页面
@author: Xushenwei
@update: 2018年7月1日
'''
from time import sleep
import unittest, random, sys, autoit, threading, os
from	 page_obj.functions import Base
from page_obj.functions import myunit
from page_obj.functions import PageFunction_XML

def addfile():
	'''上传附件流程'''
	autoit.mouse_click(x=630, y=255)
	sleep(3)
	if autoit.win_exists('打开文件'):
		autoit.win_active('打开文件')
		autoit.mouse_click(x=780, y=50)
		path = os.path.dirname(__file__)
		npos = 'IMTestScript'
		APPLICATION_PATH = Base.common_path(path=path, npos=npos) + r'IMTestScript\IM_Test\data\uploadfile'
		autoit.send(APPLICATION_PATH)
		autoit.send('{ENTER}')
		autoit.mouse_click(x=780, y=970)
		autoit.send('uploadfile_1.txt')
		autoit.send('!o')
		sleep(2)
	else:
		raise Exception('没有打开文件窗口')	

class NormalFlowTest(myunit.IMTest):
	'''正常流程相关测试'''
	def test1_creatnormal_flow(self):
		'''添加合同正常流程'''
		FF  = PageFunction_XML.FunctionFactory(self.driver,'IM_Test/test_case/page_obj/Element.xml')
		
		click_list = ['Maximize_Window', 'ProjectManage', 'ContractManage','switch_ContractType', 'ConstructionContract', 'create_ConstructModal']
		send_key_list = [('ContractNum', '1111'), ('ContractAmount', '2222'), ('ProvisionalSum', '3333'), ('ConstructionUnit', '测试建设单位'), ('ExecutionUnit', '测试施工单位'), 
		('ConstructionManager', '测试施工负责人'), ('StartStakeMark', '4444'), ('SectionLength', '5555'), ('Duration', '6666'), ('SectionNum', '7777'), ('ProjectName', '测试项目名称'),
		('SupervisionUnit', '测试监理单位'), ('EndStakeMark', '8888'),]
		time_widget_list = [('PlanStartDate', 'planStartDate', '2018-06-20'), ('ActualStartDate', 'actualStartDate', '2018-06-20'), 
		('PlanEndDate', 'planEndDate', '2018-06-22'), ('ActualEndDate', 'actualEndDate', '2018-06-22'), ('SignedDate', 'signedDate', '2018-06-23'), ]

		for Function_Name in click_list:
			FF.RunClick(Function_Name)
			sleep(0.5)
		addfile()
		for Function_Name, message in send_key_list:
			FF.RunSendKeys(Function_Name, message)
			sleep(0.5)
		for Function_Name, id_name, message in time_widget_list:
			FF.RunTimeWidget(Function_Name, id_name, message)
			sleep(0.5)

		FF.RunClick('save_Contract')
		sleep(5)
		self.assertEqual(FF.RunHint('ContractName_hint'), '7777')

	def test2_deletenormal_flow(self):
		'''删除合同正常流程'''
		FF = PageFunction_XML.FunctionFactory(self.driver, 'IM_Test/test_case/page_obj/Element.xml')

		click_list = ['Maximize_Window', 'delete_Contract', 'Enter_DeleteContract']
		for Function_Name in click_list:
			FF.RunClick(Function_Name)
			sleep(0.5)
		sleep(3)
		self.assertEqual(FF.RunHint('ContractName_hint'), '合同段')

if __name__ == '__main__':
	
	myunit.unittest.main()
	'''
	# 构造测试集
	suite = unittest.TestSuite()
	suite.addTest(NormalFlowTest("test1_creatnormal_flow"))
	suite.addTest(NormalFlowTest("test2_deletenormal_flow"))
	suite.addTest(NormalFlowTest(""))
	suite.addTest(NormalFlowTest(""))
	suite.addTest(NormalFlowTest(""))
	suite.addTest(NormalFlowTest(""))
	
	# 执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)
	'''
