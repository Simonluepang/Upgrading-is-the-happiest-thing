#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 继承unittest
Description: 设置setup和teardown
@author: Xushenwei
@update: 2018年6月11日
'''
import os, unittest
from selenium import webdriver
# from Base import *
from page_obj.models import Base

class IMTest(unittest.TestCase):
    """质检计量初始化与清理程序"""

    def setUp(self):
        self.driver = Base.browser()
        self.driver.implicitly_wait(10)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":

    IMT = IMTest()
    IMT.setUp()
    IMT.tearDown()
    #unittest.main()