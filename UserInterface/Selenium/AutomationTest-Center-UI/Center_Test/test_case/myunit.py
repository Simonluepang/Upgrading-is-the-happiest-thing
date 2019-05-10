#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 继承unittest
Description: 初始化测试框架
@author: Xushenwei
@update: 2018年6月11日
@editor:
'''
import unittest
from selenium import webdriver
from Center_Test.test_case.page_obj.Public.PageFunction import *

class CenterTest(unittest.TestCase):
    """初始化测试框架"""

    def Center_login(self, driver):
        login = FunctionFactory(driver, 'Page_login_css')
        login.open('http://192.168.13.195:8989/dist/#/login')
        messagelist = [('login_username', 'xushenwei'), ('login_password', '111111')]
        for element_name, value in messagelist:
            login.SendKeys(element_name, value)
        login.Click('submit_login')
        sleep(1)
        try:
            if login.Hint('choose_company') == "选择企业：":
                login.Click('submit_login')
            else:
                pass
        except:
            pass
        if login.Hint('login_success_hint') == '徐莘伟的企业':
            pass
        else:
            raise Exception('login failed!')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Center_login(self.driver)

        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    MLT = CenterTest()
    MLT.setUp()
    MLT.tearDown()
    # unittest.main()