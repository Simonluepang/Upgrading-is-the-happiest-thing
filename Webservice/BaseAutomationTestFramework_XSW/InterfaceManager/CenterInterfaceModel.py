#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append('..')
from Public.WebRequestManage import *
from Public.FileOperate import read_dynamic_generation_txt
from Public.HeaderManage import *
from Setting import *

pdsUrl = LoginConfig['pdsUrl']
userName = LoginConfig['user']
userPwd = LoginConfig['pwd']
enterpriseId = LoginConfig['epid']
productId = LoginConfig['productId']
CookieFilePath = Path['CookiePath']
UrlFilePath = Path['UrlPath']

class CenterInterface(object):
    """接口通用"""
    def __init__(self):
        self.builder = read_dynamic_generation_txt(UrlFilePath, 'builder', SpliteSymbol)
        self.LBprocess = read_dynamic_generation_txt(UrlFilePath, 'LBprocess', SpliteSymbol)
        self.headers_builder = headers_json(read_dynamic_generation_txt(CookieFilePath,'builder',SpliteSymbol))
        self.headers_process = headers_json(read_dynamic_generation_txt(CookieFilePath,'process',SpliteSymbol))
        self.headers_BE = headers_json(read_dynamic_generation_txt(CookieFilePath, 'LBSP', SpliteSymbol))
        self.Webrequests = Webrequests()
        self.epid = LoginConfig['epid']

if __name__ == '__main__':
    print('builder:' + CenterInterface().builder)
    # print('process:' + CenterInterface().LBprocess,CenterInterface().headers_process)
    pass