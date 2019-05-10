#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.MonitorController import *

class SingleInterfaceTest(object):
    def get_list(self):
        # 获取监控列表
        list_resp = ListMonitor().list_monitor()
        assert_pass(list_resp)
        return list_resp.get('result')[0].get('platformcode')

    def get_info(self,platformCode):
        # 获取监控平台信息
        message_resp = GetPlatformMessage().get_message(platformCode)
        assert message_resp == 200

class TestIntergratedInterface(SingleInterfaceTest):

    def test_monitor_controller(self):
        '''监控平台集成接口'''
        platformCode =self.get_list()
        self.get_info(platformCode)



if __name__ == '__main__':
    pytest.main(['test_MonitorController.py'])
