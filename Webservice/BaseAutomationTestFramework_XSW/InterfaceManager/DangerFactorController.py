#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""隐患要素管理"""

class AddDangerFactor(CenterInterface):
    # 新增隐患要素接口
    def req_params(self, name, status):
        params = {
            "name": name,
            "status": status
        }
        return params

    def add_dangerfactor(self,data):
        url = self.builder + "/dictionary/hiddendanger/factor"
        response = self.Webrequests.post_json(url, data, self.headers_builder).json()
        return response

class DeleteDangerFactor(CenterInterface):
    # 删除隐患要素接口
    def delete_dangerfactor(self, *dangerfactorIds):
        url = self.builder + '/dictionary/hiddendanger/factor'
        response = self.Webrequests.delete(url, dangerfactorIds, self.headers_builder).json()
        return response

class UpdateDangerFactor(CenterInterface):
    # 更新隐患要素接口
    def req_params(self, name, status):
        params = {
            "name": name,
            "status": status
        }
        return params

    def update_dangerfactor(self, factorid, data):
        url = self.builder + f'/dictionary/hiddendanger/factor/{factorid}'
        response = self.Webrequests.put(url, data, self.headers_builder).json()
        return response

class ListDangerFactor(CenterInterface):
    # 获取隐患要素列表
    def req_params(self,keyword,page=1,size=10):
        orders = [{"direction": 0, "property": "source"}, {"direction": 1, "property": "updateTime"}]
        params = {
                    "keyword": keyword,
                    "orders": orders,
                    "page": page,
                    "size": size
                }
        return params

    def list_dangerfactor(self, data):
        url = self.builder + '/dictionary/hiddendanger/factors'
        response = self.Webrequests.post_json(url, data,self.headers_builder).json()
        return response

class ListAllowDangerFactor(CenterInterface):
    # 获取隐患要素列表(启用)
    def list_allowdangerfactor(self):
        url = self.builder + '/dictionary/hiddendanger/factors'
        response = self.Webrequests.get(url, '', self.headers_builder).json()
        return response

if __name__ == '__main__':
    pass