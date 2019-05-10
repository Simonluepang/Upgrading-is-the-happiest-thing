#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""BIM工程相关接口"""

class GetProjExtractInfo(CenterInterface):
    # 工程抽取失败时，获取失败详情信息
    def get_projextractinfo(self,packageType,*ppids):
        url = self.builder + f'/rs/bimRest/getProjExtractInfo/{packageType}'
        resp = self.Webrequests.post_json(url,ppids,self.headers_builder).json()
        return resp

class GetProjUsedName(CenterInterface):
    # 获取工程曾用名
    def get_projusedname(self,projId,packageType=1):
        url = self.builder + f'/rs/bimRest/getProjUsedName/{projId}/{packageType}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class ExtractProject(CenterInterface):
    # 抽取工程接口
    def extract_project(self,projId,packageType):
        url = self.builder + f'/rs/bimRest/extractProj/{projId}/{packageType}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class DeleteProjectToRecycle(CenterInterface):
    # 批量标记删除工程
    def delete_projecttorecycle(self,*projIds,packageType=1):
        url = self.builder + f'/rs/bimRest/deleteProjects/{packageType}'
        resp = self.Webrequests.post_json(url,projIds,self.headers_builder).json()
        return resp

class CreateProject(CenterInterface):
    # 创建工程
    def req_params(self,deptId,projName,projType=1,packageType=1,projMemo='',*userNames):
        params = {
          "deptId": deptId,
          "packageType": packageType,
          "projMemo": projMemo,
          "projName": projName,
          "projType": projType,
          "userNames": userNames
        }
        return params

    def create_project(self,data):
        url = self.builder + '/rs/bimRest/createProject'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class GetProject(CenterInterface):
    # 获取工程列表
    def req_params(self,searchKey):
        params = {
          "delete": False,
          "deptIds": [],
          "latest": True,
          "packageType": 1,
          "pageParam": {
            "orders": [
              {
                "direction": 1,
                "property": "t1.updateDate"
              }
            ],
            "page": 1,
            "size": 10
          },
          "projGenre": '',
          "projType": 0,
          "searchKey": searchKey,
          "skOnlyProjName": False
        }
        return params

    def find_all_params(self):
        params = {
            "delete": False,
            "deptIds": [],
            "latest": True,
            "packageType": 1,
            "pageParam": {
                "orders": [{
                    "direction": 1,
                    "ignoreCase": True,
                    "property": "t1.updateDate"
                }],
                "page": 1,
                "size": 10000
            },
            "projGenre": '',
            "projType": 0,
            "searchKey": "",
            "skOnlyProjName": False
        }
        return params

    def get_project(self,data):
        url = self.builder + '/rs/bimRest/getProjects'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class UpdateProjName(CenterInterface):
    # 修改工程名称
    def req_params(self,projId,projName,packageType=1):
        params = {
          "packageType": packageType,
          "projId": projId,
          "projName": projName
        }
        return params

    def update_projectname(self,data):
        url = self.builder + '/rs/bimRest/updateProjName'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class UpdateProjShortInfo(CenterInterface):
    # 更新工程简要信息
    def req_params(self,projId,projName,*userNames):
        params = {
          "packageType": 1,
          "projId": projId,
          "projName": projName,
          "projType": 1,
          "userNames": userNames,
          "projMemo": ""
        }
        return params

    def update_projectshortinfo(self,data):
        url = self.builder + '/rs/bimRest/updateProjShortInfo'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp
