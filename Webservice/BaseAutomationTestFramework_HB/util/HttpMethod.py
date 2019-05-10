#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2018/7/31 17:18
# @Author  : hubiao
# @File    : HttpMethod.py
from util.Config import ManageConfig
import requests
import json

class sendRequest:
    '''
    发送请求类
    '''
    def __init__(self,host,header):
        '''
        请求数据初始化
        @host：请求的地址前缀
        @header：请求头信息
        '''
        self.host = host
        self.header = header
        self.postSite = requests.session()
        self.rf = ManageConfig().getConfig('pds')

    def hooks(self,r,*args, **kwargs):
        '''
        为解决302跨域跳转到pds时，不传cookie实现的钩子方法，人为指定cookie并去请求302跳转连接
        :param r: 原始请求的响应信息
        :param args:
        :param kwargs:
        :return: and "Set-Cookie" in r.headers.keys()
        '''
        try:
            # 如果响应码是302，且location是PDS地址的跳转时，要加上PDS的cookie并请求这个location
            if r.status_code == 302 and self.rf["pds"] in r.headers['location']:
                header = json.loads(self.header)
                header["cookie"] = self.rf["pdscookie"]
                self.postSite.request(method=r.request.method, url=r.headers['location'],headers=header,timeout=60)
        except BaseException as e:
            print("PDS跳转异常请求失败！", str(e))

    def JsonRequest(self,method,address,payload=None,header=None):
        '''
        封装request方法，要求传三个参数
        @method：请求的方式post，get
        @address：请求的地址
        @payload：请求的body数据，可以不传，默认为空
        '''
        try:
            #组装请求地址
            self.postUrl = ''.join([self.host,address])
            #是否使用默认请求头
            if header is None:
                header = self.header
            #发送POST请求
            self.Response = self.postSite.request(method=method,url=self.postUrl,data=payload,headers=json.loads(header),hooks=dict(response=self.hooks),timeout=60)
            # 解决跨域302跳转后响应成cas登录页面的处理，当出现cas登录界面时自动重试相关接口
            if self.Response.status_code == 200 and self.rf["pds"]+"/login?service" in self.Response.url:
                self.Response = self.postSite.request(method=method, url=self.postUrl, data=payload,
                                                      headers=json.loads(header),timeout=60)
            return self.Response
        except BaseException as e:
            print("请求失败！", str(e))

if __name__ == '__main__':
    zentao = ManageConfig().getConfig('zentao')
    print(type(zentao['headerss']))
    print(json.dumps(type(zentao['headers'])))
    print(zentao['host'])
    print(zentao['headers'])
