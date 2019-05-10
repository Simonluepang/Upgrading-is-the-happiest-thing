#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""协作类型管理"""

class AddCooperationType(CenterInterface):
    # 新增协作类型接口
    def req_params(self,name,isShow=0):
        params = {
            "isShow": isShow,
            "name": name
        }
        return params

    def add_cooperationtype(self,data):
        url = self.builder + "/co/type/save"
        response = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return response

class DeleteCooperationType(CenterInterface):
    # 删除协作类型接口
    def delete_cooperationtype(self,*ids):
        url = self.builder + '/co/type/batch_del_co_type'
        resp = self.Webrequests.post_json(url,ids,self.headers_builder).json()
        return resp

class UpdateCooperationType(CenterInterface):
    # 修改协作类型接口
    def req_params(self,id,name,isShow=1):
        params = {
            "id": id,
            "isShow": isShow,
            "name": name
        }
        return params

    def update_cooperationtype(self,data):
        url = self.builder + "/co/type/update"
        response = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return response

class ListAllCooperationType(CenterInterface):
    # 分页查询协作类型接口
    def req_params(self,searchKey,pageIndex=1,pageSize=15):
        params = {
            "pageIndex": pageIndex,
            "pageSize": pageSize,
            "searchKey": searchKey
        }
        return params

    def list_allcooperationtype(self,data):
        url = self.builder + '/co/type/page_co_type'
        response = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return response

class IsRelevanceCO(CenterInterface):
    # 是否关联协作
    def is_relevance_CO(self,coTypeId):
        url = self.builder + f'/co/type/is_rel_co/{coTypeId}'
        response = self.Webrequests.get(url,'',self.headers_builder).json()
        return response

class ListShownCooperationType(CenterInterface):
    # 查询协作类型接口（过滤不显示）
    def list_showncooperationtype(self):
        url = self.builder + '/co/type/list_co_type_show'
        response = self.Webrequests.get(url,'',self.headers_builder).json()
        return response
