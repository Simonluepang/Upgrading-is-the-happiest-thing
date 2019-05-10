#!\usr\bin\env python
# -*- coding:utf-8 -*-
# Title: 测试用例
# Description: 合同管理页面
# @author: Xushenwei
# @update: 2018年7月1日
# @editor:

import random, string, pytest
from time import sleep
from Center_Test.test_case.page_obj.Public.PageFunction import  FunctionFactory
from Center_Test.test_case.myunit import CenterTest

class ConfigurationTest(CenterTest):
	'''应用配置流程测试'''

	def test1_datacatalog_flow(self):
		'''资料目录相关流程'''
		FF = FunctionFactory(self.driver, 'Page_configuration_css')
		message = "测试" + ''.join(random.sample(string.ascii_letters + string.digits, 4))
		click_list = ["configuration", "common", "data_catalog", "folder_add", "folder_success_add",
		 "folder_search", "folder_edit", "folder_success_edit", "folder_delete_box", "folder_delete", "success_delete"]
		for Function_Name in click_list:
			FF.Click(Function_Name)
			sleep(1.3)
			if Function_Name == "folder_add":
				"""添加文件夹"""
				FF.SendKeys("folder_add_name", message)
			elif Function_Name == "folder_success_add":
				FF.SendKeys('folder_search_name', message)
			elif Function_Name == "folder_search":
				"""搜索文件夹"""
				# 验证文件夹是否添加成功
				self.assertEqual(FF.Hint('folder_new_name_hint'), message)
			elif Function_Name == "folder_edit":
				"""修改文件夹"""
				ed_message = message + 'edit'
				FF.SendKeys('folder_edit_name', ed_message)
			elif Function_Name == "folder_success_edit":
				# 验证文件夹是否修改成功
				self.assertEqual(FF.Hint('folder_new_name_hint'), message+'edit')
			elif Function_Name == "success_delete":
				'''删除文件夹'''
				# 验证文件夹是否删除成功
				self.assertEqual(FF.Hint('folder_success_delete_hint'), '暂无数据')

	# def test2_labelmanagement_flow(self):
	# 	'''标签管理相关流程'''
	# 	FF = FunctionFactory(self.driver, 'Page_configuration_css')
	# 	click_list = ["configuration", "common", "label_management", "label_add", "label_success_add",
	# 	"label_search", "label_edit", "label_success_edit", "label_delete_box", "label_delete", "success_delete"]
	# 	message = "测试" + ''.join(random.sample(string.ascii_letters + string.digits, 4))
	# 	for Function_Name in click_list:
	# 		FF.Click(Function_Name)
	# 		sleep(1.3)
	# 		if Function_Name == "label_add":
	# 			"""添加标签"""
	# 			FF.SendKeys('label_add_name', message)
	# 		elif Function_Name == "label_success_add":
	# 			"""搜索标签"""
	# 			FF.SendKeys('label_search_name', message)
	# 		elif Function_Name == "label_search":
	# 			# 验证标签是否添加成功
	# 			self.assertEqual(FF.Hint('label_new_name_hint'), message)
	# 		elif Function_Name == "label_edit":
	# 			"""修改标签"""
	# 			ed_message = message + 'edit'
	# 			FF.SendKeys('label_edit_name', ed_message)
	# 		elif Function_Name == "label_success_edit":
	# 			# 验证标签是否修改成功
	# 			self.assertEqual(FF.Hint('label_new_name_hint'), message+'edit')
	# 		elif Function_Name == "success_delete":
	# 			"""删除标签"""
	# 			# 验证标签是否删除成功
	# 			self.assertEqual(FF.Hint('label_success_delete_hint'), '暂无数据')

	# def test3_formmanagement_flow(self):
		# '''表单管理相关流程'''
		# FF = FunctionFactory(self.driver, 'Page_configuration_css')
		# click_list = ["configuration", "common", "form_management", "form_add", "upload_templatefile",
		# "form_success_add", "form_edit", "form_success_edit", "form_delete_box", "form_delete", "success_delete"]
		# message = "测试" + ''.join(random.sample(string.ascii_letters + string.digits, 4))
		# for Function_Name in click_list:
		# 	FF.Click(Function_Name)
		# 	sleep(1.3)
		# 	if Function_Name == "upload_templatefile":
		# 		FF.addfile('打开', 'uploadfile_1.doc')
		# 	elif Function_Name == 'form_success_add':
		# 		# 验证表单模板是否上传成功
		# 		self.assertEqual(FF.Hint('form_hint'), 'uploadfile_1')
		# 	elif Function_Name == "form_edit":
		# 		FF.SendKeys('form_template_name_edit', message)
		# 	elif Function_Name == "form_success_edit":
		# 		# 验证表单模板修改名称是否成功
		# 		self.assertEqual(FF.Hint('form_hint'), message)
		# 	elif Function_Name == "success_delete":
		# 		# 验证表单模板删除是否成功
		# 		self.assertEqual(FF.Hint('form_success_delete_hint'), '暂无数据')

		

if __name__ == '__main__':
	# unittest.main()
	pytest.main()

	# 构造测试集
	'''
	suite = unittest.TestSuite()
	suite.addTest(ConfigurationTest("test1_datacatalog_flow"))
	# suite.addTest(ConfigurationTest("test2_labelmanagement_flow"))
	# suite.addTest(ConfigurationTest("test3_formmanagement_flow"))
	
	suite.addTest(NormalFlowTest(""))
	suite.addTest(NormalFlowTest(""))
	suite.addTest(NormalFlowTest(""))
	suite.addTest(NormalFlowTest(""))
	
	
	# 执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)
	'''