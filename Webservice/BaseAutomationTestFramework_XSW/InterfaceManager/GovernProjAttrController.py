#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""原Govern工程属性相关接口"""

class GetProjAttrs(CenterInterface):
    # 获取工程性质列表数据
    def get_projattrs(self):
        url = self.builder + '/rs/oldgovern/projattr/getProjAttrs'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class UpdateProjAttrs(CenterInterface):
    # 更新工程性质列表数据
    def req_params(self,id,projAttr,projAttrName,projAttrNickName,attrConfig=1,timeType=1):
        params = [
          {
            "attrConfig": attrConfig,
            "epid": self.epid,
            "id": id,
            "projAttr": projAttr,
            "projAttrName": projAttrName,
            "projAttrNickName": projAttrNickName,
            "timeType": timeType
          }
        ]
        return params
    def update_projattrs(self,data):
        url = self.builder + '/rs/oldgovern/projattr/updateProjAttrs'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp
