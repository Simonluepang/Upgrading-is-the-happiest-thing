#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""监控平台"""

class ListMonitor(CenterInterface):
    # 获取监控列表
    def list_monitor(self):
        url = self.builder + '/monitors/'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class GetPlatformMessage(CenterInterface):
    # 获取设备平台soap信息
    def get_message(self, platformCode):
        url = self.builder + f'/monitors/{platformCode}'
        resp = self.Webrequests.get(url,'',self.headers_builder).status_code
        return resp
