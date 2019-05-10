#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os,time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Setting import *

class Base:

    def __init__(self):
        self.driver = webdriver.Remote(serverAddress,desired_caps)
        self.timeout = 10
        self.basedir = os.path.dirname(os.path.abspath(__file__))

    def __find_element(self,method,loc):
        if method == 'CSS':
            return self.driver.find_element_by_css_selector(loc)
        elif method == 'ID':
            return self.driver.find_element_by_id(loc)
        elif method == 'NAME':
            return self.driver.find_element_by_name(loc)
        elif method == 'CLASS':
            return self.driver.find_element_by_class_name(loc)
        elif method == 'TAG':
            return self.driver.find_element_by_tag_name(loc)
        elif method == 'LINK':
            return self.driver.find_element_by_link_text(loc)
        elif method == 'PARTIAL_LINK':
            return self.driver.find_element_by_partial_link_text(loc)
        elif method == 'XPATH':
            return self.driver.find_element_by_xpath(loc)
        else:
            raise Exception(f"没有找到{method}此种定位方式！")

    def find_element(self,method,loc):
        # try:
        #     WebDriverWait(self.driver,self.timeout,0.5).until(EC.presence_of_element_located(loc))
        #     return self.__find_element(method,loc)
        # except:
        #     raise Exception(f"未能根据‘{loc}’找到正确的元素定位")
        return self.__find_element(method, loc)

    def __find_elements(self,method,loc):
        if method == 'CSS':
            return self.driver.find_element_by_css_selector(loc)
        elif method == 'ID':
            return self.driver.find_element_by_id(loc)
        elif method == 'NAME':
            return self.driver.find_element_by_name(loc)
        elif method == 'CLASS':
            return self.driver.find_element_by_class_name(loc)
        elif method == 'TAG':
            return self.driver.find_element_by_tag_name(loc)
        elif method == 'LINK':
            return self.driver.find_element_by_link_text(loc)
        elif method == 'PARTIAL_LINK':
            return self.driver.find_element_by_partial_link_text(loc)
        elif method == 'XPATH':
            return self.driver.find_element_by_xpath(loc)
        else:
            raise Exception(f"没有找到{method}此种定位方式！")

    def find_elements(self,method, loc):
        try:
            WebDriverWait(self.driver,self.timeout,0.5).until(EC.presence_of_element_located(loc))
            return self.__find_elements(method,loc)
        except:
            raise Exception(f"未能根据‘{loc}’找到正确的元素定位")

    def location(self,method,act,loc,clickFirst=False,message=''):
        if act == 'CLICK':
            self.find_element(method,loc).click()
            time.sleep(0.7)
        elif act == 'SENDKEYS':
            # if clickFirst == True:
            #     self.find_element(method,loc).click()
            # self.find_element(method,loc).clear()
            self.find_element(method,loc).send_keys(message)
            time.sleep(0.7)
        elif act == 'HINT':
            return self.find_element(method,loc).text
        else:
            raise Exception(f"没有收录{act}此种动作！")

    def tap(self,*positions,duration=None):
        self.driver.tap(positions,duration)
        time.sleep(1)

    def swipeUp(self,duration=None,n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.75
        y2 = l['height'] * 0.25
        for i in range(n):
            self.driver.swipe(x1,y1,x1,y2,duration)
            time.sleep(0.5)

    def swipeDown(self,duration=None,n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.25
        y2 = l['height'] * 0.75
        for i in range(n):
            self.driver.swipe(x1,y1,x1,y2,duration)
            time.sleep(0.5)

    def swipeLeft(self,duration=None,n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1,y1,x2,y1,duration)
            time.sleep(0.5)

    def swipeRight(self,duration=None,n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1,y1,x2,y1,duration)
            time.sleep(0.5)

    def quit(self):
        self.driver.quit()