#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2019/1/2 11:19
# @Author  : hubiao
# @File    : PublicLogin.py
from util.Config import ManageConfig
from util import HttpMethod
import json,re

class Center:

    def __init__(self,centerusername,centerpassword):
        self.section = 'pds'
        self.pds = ManageConfig().getConfig(self.section)
        self.wf = ManageConfig()
        self.productId = self.pds['centerProductId']
        self.username = centerusername
        self.password = centerpassword
        self.header = self.pds['headers']
        self.CenterLogin = HttpMethod.sendRequest(self.pds['pds'], self.pds['header'])
        self.epid = ''

    def getServerUrl(self):
        '''
        获取服务器地址信息
        '''
        resource = '/rs/centerLogin/serverurl'
        response = self.CenterLogin.JsonRequest('get',resource)
        serverlist = response.json()
        assert response.status_code == 200
        assert len(serverlist) != 0
        for server in serverlist:
            self.wf.writeConfig(self.section,server["serverName"],server["serverURL"])

    def getDeployType(self):
        '''
        获取部署类型
        :return:
        '''
        resource = '/rs/centerLogin/deployType'
        response = self.CenterLogin.JsonRequest('get', resource)
        assert response.status_code == 200
        deployType = response.text
        self.wf.writeConfig(self.section,'deployType', deployType)

    def getLT(self):
        '''
        获取LT
        :return:
        '''
        resource = '/login'
        response = self.CenterLogin.JsonRequest('get', resource)
        assert response.status_code == 200
        html = response.text
        pattern = 'value="LT(.+?)" />'
        lt = re.findall(pattern, html)[0]
        return lt

    def getTGC(self):
        '''
        获取TGC，依赖getLT接口
        :return:
        '''
        resource = '/login'#?service=+serverlist[6]["serverURL"].replace("://","%3A%2F%2F")
        body = {"_eventId": "submit", "execution": "e1s1", "lt": 'LT' + self.getLT(), "password": self.password, "productId": self.productId,
         "submit": "%E7%99%BB%E5%BD%95", "username": self.username}
        response = self.CenterLogin.JsonRequest('post',resource,body,self.header)
        assert response.status_code == 200

    def getCompanyList(self):
        '''
        获取企业id列表
        :return:
        '''
        resource = "/rs/centerLogin/companyList"
        body = {"password": self.password,"username": self.username}
        response = self.CenterLogin.JsonRequest('post',resource,json.dumps(body))
        self.wf.writeConfig(self.section,'pdsCookie', response.request.headers["cookie"])
        assert response.status_code == 200
        response = response.json()
        if len(response) > 0:
            self.wf.writeConfig(self.section,'epid',response[0]["epid"])
            self.epid = response[0]["epid"]
            return response[0]["epid"]

    def switchCompany(self):
        '''
        切换到指定企业，依赖getCompanyList接口
        :return:
        '''
        resource = "/rs/centerLogin/login"
        body = {"epid":self.epid,"password": self.password,"username": self.username}
        response = self.CenterLogin.JsonRequest('post',resource,json.dumps(body))
        assert response.status_code == 200
        response = response.json()

    def Login(self):
        '''
        Center登录
        :return:
        '''
        self.getServerUrl()
        self.getDeployType()
        self.getTGC()
        self.getCompanyList()
        self.switchCompany()

class BV:

    def __init__(self,username,password):
        self.section = 'pds'
        self.pds = ManageConfig().getConfig(self.section)
        self.wf = ManageConfig()
        self.productId = self.pds['BVproductId']
        self.username = username
        self.password = password
        self.header = self.pds['headers']
        self.casLogin = HttpMethod.sendRequest(self.pds['pds'], self.pds['header'])
        self.epid = ''

    def getServerUrl(self):
        '''
        获取服务器地址信息
        '''
        resource = '/rs/casLogin/serverUrl'
        response = self.casLogin.JsonRequest('get',resource)
        serverlist = response.json()
        assert response.status_code == 200
        assert len(serverlist) != 0
        for server in serverlist:
            self.wf.writeConfig(self.section,server["serverName"],server["serverURL"])

    def getLT(self):
        '''
        获取LT
        :return:
        '''
        resource = '/login'
        response = self.casLogin.JsonRequest('get', resource)
        assert response.status_code == 200
        html = response.text
        pattern = 'value="LT(.+?)" />'
        lt = re.findall(pattern, html)[0]
        return lt

    def getTGC(self):
        '''
        获取TGC，依赖getLT接口
        :return:
        '''
        resource = '/login'#?service=+serverlist[6]["serverURL"].replace("://","%3A%2F%2F")
        body = {"_eventId": "submit", "execution": "e1s1", "lt": 'LT' + self.getLT(), "password": self.password, "productId": self.productId,
         "submit": "%E7%99%BB%E5%BD%95", "username": self.username}
        response = self.casLogin.JsonRequest('post',resource,body,self.header)
        assert response.status_code == 200

    def getCompanyList(self):
        '''
        获取企业id列表
        :return:
        '''
        resource = "/rs/casLogin/companyList"
        body = {"password": self.password,"userName": self.username, "clientVersion": "5.8.0",
         "phoneModel": "国行(A1865)、日行(A1902)iPhone X", "platform": "ios", "innetIp": "192.168.7.184", "productId": self.productId,
         "token": "f54d6c8c13445a723a2863a72d460e5aec48010560ea2351bda6474de5164899", "systemVersion": "12.1.2",
         "hardwareCodes": "3465192946d57f13482640578c77ffa77d1f66a4"}
        response = self.casLogin.JsonRequest('post',resource,json.dumps(body))
        self.wf.writeConfig(self.section,'pdsCookie', response.request.headers["cookie"])
        assert response.status_code == 200
        response = response.json()
        if len(response) > 0:
            self.wf.writeConfig(self.section,'epid',response[0]["enterpriseId"])
            self.epid = response[0]["enterpriseId"]
            return self.epid

    def switchCompany(self):
        '''
        切换到指定企业
        :return:
        '''
        resource = f"/rs/casLogin/changeEnterprise/{self.epid}"
        response = self.casLogin.JsonRequest('get',resource)
        assert response.status_code == 200
        response = response.json()

    def Login(self):
        '''
        Center登录
        :return:
        '''
        self.getServerUrl()
        self.getTGC()
        self.getCompanyList()
        self.switchCompany()