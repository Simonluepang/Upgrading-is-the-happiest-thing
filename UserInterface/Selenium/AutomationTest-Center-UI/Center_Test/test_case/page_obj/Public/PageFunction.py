#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 页面元素工厂
Description: 继承Base，对页面元素进行二次封装，
读取json格式元素地址，使其能够直接使用element文件中的元素名
直接调用该元素所对应的操作。
@author: Xushenwei
@update: 2018年9月18日
@editor:
'''
import json
from selenium.webdriver.common.by import By
from Center_Test.test_case.page_obj.Public.Base import *

class FunctionFactory(Page):
    '''元素方法工厂'''

    def __init__(self, jsonfilename, driver):
        super().__init__(driver)
        self.jsonfilename = jsonfilename


    def make_function_click_by_css(self, element_location):
        """使用css定位来点击元素"""

        def function_click_by_css():
            self.find_element(By.CSS_SELECTOR, element_location).click()

        return function_click_by_css

    def make_function_sendkeys_by_css(self, element_location):
        """使用css定位来输入信息"""

        def function_sendkeys_by_css(value, clear_first=True, click_first=True, id_name=""):
            try:
                if id_name:
                    js = "document.getElementById('" + id_name + "').removeAttribute('readonly');"
                    self.script(js)
                if click_first:
                    self.find_element(By.CSS_SELECTOR, element_location).click()
                if clear_first:
                    self.find_element(By.CSS_SELECTOR, element_location).clear()
                    self.find_element(By.CSS_SELECTOR, element_location).send_keys(value)
            except AttributeError:
                print("Can't find element as %s" % element_location)

        return function_sendkeys_by_css

    def make_function_hint_by_css(self, element_location):
        """使用css定位来获取验证元素文本"""

        def function_hint_by_css():
            return self.find_element(By.CSS_SELECTOR, element_location)

        return function_hint_by_css().text

    def ReadJsonData(self):
        """从Json文件中读取元素内容"""
        jsonpath = self.basedir + '/page_obj/' + self.jsonfilename + '.json'
        file = open(jsonpath, 'rb')
        fileJsondata = json.loads(file.read())
        file.close()	
        return fileJsondata

    def Click(self, element_name):
        """使用元素名称来操控元素点击动作"""
        element_location = self.ReadJsonData()[element_name]
        function = self.make_function_click_by_css(element_location)
        function()

    def SendKeys(self, element_name, value):
        """使用元素名称来操控输入动作"""
        element_location = self.ReadJsonData()[element_name]
        function = self.make_function_sendkeys_by_css(element_location)
        function(value)

    def Hint(self, element_name):
        """使用元素名称来操控元素点击动作"""
        element_location = self.ReadJsonData()[element_name]
        function = self.make_function_hint_by_css(element_location)
        return function


if __name__ == "__main__":
    pass
