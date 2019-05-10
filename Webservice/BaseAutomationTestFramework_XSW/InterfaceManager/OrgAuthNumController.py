#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""组织授权数管理"""

class GetUserOrgAuthNum(CenterInterface):
    # 获取当前用户可授权的组织数据
    def get_user_org_auth_num(self,userName,packageType,functionId,heldId):
        url = self.builder + f'/org/authNum/getUserOrgAuthNum/username/{userName}/packageType/{packageType}/functionId/{functionId}/heldId/{heldId}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class RecycleAuthNum(CenterInterface):
    # 回收组织授权
    def recycle_auth_num(self,orgId,*orgIds):
        url = self.builder + f'/org/authNum/{orgId}'
        resp = self.Webrequests.delete(url,orgIds,self.headers_builder).json()
        return resp

class GetAuthNum(CenterInterface):
    # 获取组织授权数详情
    def get_auth_num(self,orgId):
        url = self.builder + f'/org/authNum/{orgId}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class SaveAuthNum(CenterInterface):
    # 保存组织授权
    def req_params(self,availableAuth,functionId,heldId,packageType):
        params = [
          {
            "availableAuth": availableAuth,
            "functionId": functionId,
            "heldId": heldId,
            "packageType": packageType
          }
        ]
        return params

    def save_auth_num(self,orgId,data):
        url = self.builder + f'/org/authNum/{orgId}'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp
