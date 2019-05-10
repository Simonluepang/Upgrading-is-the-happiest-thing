#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""BIM工程条件相关接口"""

class GetProjAuthUserInfos(CenterInterface):
    # 创建/修改工程时获取授权用户信息列表
    def req_params(self,deptId,packageType,ppid):
        params = {
          "deptId": deptId,
          "packageType": packageType,
          "ppid": ppid
        }
        return params

    def get_projectauthuserinfos(self,data):
        url = self.builder + '/rs/bimParamRest/getProjAuthUserInfos'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class GetProjType(CenterInterface):
    # 获取某企业下的所有专业类型列表
    def GetProjTypeget_projtype(self,isDelete,packageType):
        url = self.builder + f'/rs/bimParamRest/getProjType/{isDelete}/{packageType}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class GetMajorsByCreate(CenterInterface):
    # 创建工程时获取该企业能创建的专业类型
    def get_majorsbycreate(self):
        url = self.builder + '/rs/bimParamRest/getMajorsByCreate'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class GetProjGenre(CenterInterface):
    # 获取某企业下的所有BIM属性列表
    def get_projgenre(self,isDelete,packageType):
        url = self.builder + f'/rs/bimParamRest/getProjGenre/{isDelete}/{packageType}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp
