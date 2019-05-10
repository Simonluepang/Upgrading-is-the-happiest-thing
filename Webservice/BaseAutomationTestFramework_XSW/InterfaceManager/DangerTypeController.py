#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""隐患类别管理"""

class AddDangerType(CenterInterface):
    # 新增隐患类别接口
    def req_params(self, factorId, name, status):
        params = {
            "factorId": factorId,
            "name": name,
            "status": status
        }
        return params

    def add_dangertype(self, data):
        url = self.builder + "/datadictionary/hiddendanger/type"
        response = self.Webrequests.post_json(url, data, self.headers_builder).json()
        return response

class DeleteDangerType(CenterInterface):
    # 删除隐患类别接口
    def delete_dangertype(self,*dangerTypes):
        url = self.builder + "/datadictionary/hiddendanger/type"
        response = self.Webrequests.delete(url,dangerTypes,self.headers_builder).json()
        return response

class UpdateDangerType(CenterInterface):
    # 更新隐患类别接口
    def req_params(self,factorId,name,status):
        params = {
            "factorId": factorId,
            "name": name,
            "status": status
        }
        return params

    def update_dangertype(self,typeid,data):
        url = self.builder + f"/datadictionary/hiddendanger/type/{typeid}"
        response = self.Webrequests.put(url,data,self.headers_builder).json()
        return response

class ListDangerType(CenterInterface):
    # 获取隐患类别列表
    def req_params(self,factorId,keyword,page=4,size=10):
        orders =[{
                "direction": 0,
                "property": "source"
            },
            {
                "direction": 1,
                "property": "updateTime"
            }
        ]
        params = {
                    "factorId": factorId,
                    "keyword": keyword,
                    "orders": orders,
                    "page": page,
                    "size": size
                }
        return params

    def list_dangertype(self,data):
        url = self.builder + "/datadictionary/hiddendanger/types"
        response = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return  response

class ListAllowDangerType(CenterInterface):
    # 获取已启用隐患类别列表
    def list_allowdangertype(self, factorId):
        url = self.builder + f"/datadictionary/hiddendanger/types/{factorId}"
        response = self.Webrequests.get(url,'',self.headers_builder).json()
        return response
