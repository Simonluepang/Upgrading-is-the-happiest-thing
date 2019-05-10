from time import sleep
import unittest, os
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
import subprocess
#sys.path.append(r'..\Clients\bimim')
#import Page
#print(os.path.relpath(r"F:\pythondemo\Github\Python-script\IM(CEF+selenium)\Clients\bimim\Page.py")) # 绝对路径转换相对路路径
#import Client.bimim.Page

class PythonOrgSearch(unittest.TestCase):

    APPLICATION_PATH = r'F:\pythondemo\Github\Python-script\IM(CEF+selenium)\Clients\bimim\BimIm.exe'
    #APPLICATION_PATH = r'F:\pythondemo\Github\Python-script\IM(CEF+selenium)\apps\cef_client_x86\cefclient.exe'

    #TEST_PAGE_PATH = r'file:///F:\pythondemo\Github\Python-script\IM(CEF+selenium)\bimim\config\WebPag/Login.html'
    #TEST_PAGE_PATH = 'file:///F:/pythondemo/Github/cef-pyhton-selenium/calc_proto/index.html'
    TEST_PAGE_PATH = 'http://192.168.13.215:8082/LBIM'
    #TEST_PAGE_PATH = 'http://172.16.21.242:8082/im/resource/index.html'
    #APPLICATION_PATH = r'BimIm.exe'
    #TEST_PAGE_PATH = r'file:///config/WebPag/index.html'

    def setUp(self):
        options = selenium.webdriver.ChromeOptions()
        options.binary_location = self.APPLICATION_PATH
        self.driver = selenium.webdriver.Chrome(chrome_options=options)
        self.driver.get(self.TEST_PAGE_PATH)
    '''
    def test_IM_Login(self):
        driver = self.driver    
        username = driver.find_element_by_xpath('//*[@id="userName"]')
        password = driver.find_element_by_xpath('//*[@id="password"]')
        server_address = driver.find_element_by_xpath('//*[@id="servaddr"]')
        login_Button = driver.find_element_by_xpath('/html/body/form/input[4]');

        username.send_keys('dlr')
        password.send_keys('12345678')
        server_address.send_keys('192.168.13.215:8082/pds')
        login_Button.click()
        time.sleep(5)
    
    def test_math_operations(self):
        driver = self.driver
        sleep(10)
        operand1 = driver.find_element_by_id('operand1')
        operand2 = driver.find_element_by_id('operand2')
        result = driver.find_element_by_id('result')
        calculateButton = driver.find_element_by_id('calculateButton')

        operand1.send_keys('2')
        operand2.send_keys('3')
        calculateButton.click()
        sleep(5)
        assert result.get_attribute('value') == '5'
    '''
    def wait(self):
        driver = self.driver
        sleep(30)

    def test_baidu(self):
        driver = self.driver
        sleep(5)
    '''
    def tearDown(self):
        self.driver.close()
    '''
    

if __name__ == "__main__":
    unittest.main()

#print(os.path.relpath(r"F:\pythondemo\Github\Python-script\IM(CEF+selenium)\Clients\bimim\Page.py"))