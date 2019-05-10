#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 页面元素:动作+验证
Description: 合同管理页面
@author: Xushenwei
@update: 2018年6月11日
'''
import os
from selenium.webdriver.common.by import By 
from selenium import webdriver
from time import sleep
import xml.dom.minidom as xmlParser
# from Base import *
from	 page_obj.models import Base

class ElementClass:
	'''获取配置文件中的信息'''
	def __init__(self, function_name, element_location):
		
		self.function_name = function_name
		self.element_location = element_location

	def get_function_name(self):
		return self.function_name

	def get_element_location(self):
		return self.element_location

def ReadXMlData(xmlPath, parent):
	'''读取配置文件中的信息，并返回每个项为一个(name,element_location)的列表'''
	dom = xmlParser.parse(xmlPath)
	db = dom.documentElement
	data_list = []
	itemlist = db.getElementsByTagName(parent)
	for item in itemlist:
		it = ElementClass(item.getAttribute('Function_name'), item.getAttribute('Element_location'))
		data_list.append(it)
	return data_list

class MakeFunction(Base.Page):
	'''创建元素操作方法'''
	def make_function_click_by_xpath(self, element_location):
		def function_click_by_xpath():
			self.find_element(By.XPATH, element_location).click()
		return function_click_by_xpath

	def make_function_click_by_class_name(self, element_location):
		def function_click_by_class_name():
			self.find_element(By.CLASS_NAME, element_location).click()
		return function_click_by_class_name

	def make_function_send_keys(self,element_location):
		def function_send_keys(message):
			self.find_element(By.XPATH, element_location).send_keys(message)
		return function_send_keys

	def make_function_time_widget1(self,element_location):
		def function_time_widget(id_name, message):
			js = "document.getElementById('" + id_name + "').removeAttribute('readonly');"
			self.driver.execute_script(js)
			self.find_element(By.XPATH, element_location).send_keys(message)
			self.find_element(By.XPATH, element_location).click()
		return function_time_widget

	def make_function_time_widget2(self,element_location):
		def function_time_widget(id_name, message):
			js = "document.getElementById('" + id_name + "').removeAttribute('readonly');"
			self.driver.execute_script(js)
			self.find_element(By.XPATH, element_location).send_keys(message)
		return function_time_widget

	def make_function_hint(self, element_location):
		def function_hint():
			return self.find_element(By.XPATH, element_location).text 
		return function_hint

class FunctionFactory():
	'''功能工厂'''
	def __init__(self, driver, xmlpath):

		self.FunctionMap = {}
		self.driver =  driver

		self.InitClickByXpath(xmlpath,"FUNCTION_CLICK_BY_XPATH")
		self.InitClickByClassName(xmlpath, "FUNCTION_CLICK_BY_CLASS_NAME")
		self.InitSendMessage(xmlpath, "FUNCTION_SEND")
		self.InitTimeWidget1(xmlpath, "FUNCTION_TIME_WDIGET1")
		self.InitTimeWidget2(xmlpath, "FUNCTION_TIME_WDIGET2")
		self.InitHint(xmlpath, "FUNCTION_HINT")

	def InitClickByXpath(self, xmlpath, Parent):
		#初始化点击事件，并保存在FuncMap中
		listclickbyxpath = ReadXMlData(xmlpath, Parent)
		for list1 in listclickbyxpath:
			self.FunctionMap[list1.get_function_name()] = MakeFunction(self.driver).make_function_click_by_xpath(list1.get_element_location())

	def InitClickByClassName(self, xmlpath, Parent):
		#初始化点击事件，并保存在FuncMap中
		listclickbyclassname = ReadXMlData(xmlpath, Parent)
		for list1 in listclickbyclassname:
			self.FunctionMap[list1.get_function_name()] = MakeFunction(self.driver).make_function_click_by_class_name(list1.get_element_location())

	def InitSendMessage(self, xmlpath, Parent):
		#初始化信息输入事件，并保存在FuncMap中
		listsSend = ReadXMlData(xmlpath, Parent)
		for list1 in listsSend:
			self.FunctionMap[list1.get_function_name()] = MakeFunction(self.driver).make_function_send_keys(list1.get_element_location())

	def InitTimeWidget1(self, xmlpath, Parent):
		#初始化时间控件事件，并保存在FuncMap中
		listTimeWidget1 = ReadXMlData(xmlpath, Parent)
		for list1 in listTimeWidget1:
			self.FunctionMap[list1.get_function_name()] = MakeFunction(self.driver).make_function_time_widget1(list1.get_element_location())

	def InitTimeWidget2(self, xmlpath, Parent):
		#初始化时间控件事件，并保存在FuncMap中
		listTimeWidget2 = ReadXMlData(xmlpath, Parent)
		for list1 in listTimeWidget2:
			self.FunctionMap[list1.get_function_name()] = MakeFunction(self.driver).make_function_time_widget2(list1.get_element_location())

	def InitHint(self, xmlpath, Parent):
		#初始化元素验证事件，并保存在FuncMap中
		listhint = ReadXMlData(xmlpath, Parent)
		for list1 in listhint:
			self.FunctionMap[list1.get_function_name()] = MakeFunction(self.driver).make_function_hint(list1.get_element_location())

	def RunClick(self, funcname):
		'''运行点击事件'''
		element = self.FunctionMap.get(funcname)
		element()

	def RunSendKeys(self, funcname, message):
		'''运行信息输入事件'''
		element = self.FunctionMap.get(funcname)
		element(message)

	def RunTimeWidget(self, funcname, id_name, message):
		'''运行时间控件事件'''
		element = self.FunctionMap.get(funcname)
		element(id_name, message)

	def RunHint(self, funcname):
		'''运行元素验证事件'''
		element = self.FunctionMap.get(funcname)
		return element()

if __name__ == "__main__":
	driver =browser()
	FunctionFactory  = FunctionFactory(driver,'../Element.xml')
	FunctionFactory.RunClick('Maximize_Window')
	sleep(3)
	driver.quit()
