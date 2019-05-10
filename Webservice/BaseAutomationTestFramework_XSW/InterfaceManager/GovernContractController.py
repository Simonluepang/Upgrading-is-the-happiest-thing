#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""Govern合同清单管理"""

class BuilderJump(CenterInterface):
    # Builder 302跳转
    def jump(self):
        url = self.builder + '/rs/govern/contract/jump'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class GetProject(CenterInterface):
    # 获取与合同清单相关联的项目
    def get_project(self,formatId):
        url = self.builder + f'/rs/govern/contract/organIds/{formatId}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class FindList(CenterInterface):
    # 分页查询合同清单
    def req_params(self,keyword):
        params = {
            'keyword': keyword
        }
        return params

    def find_list(self,data):
        url = self.builder + '/rs/govern/contract/find'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class UpdateProject(CenterInterface):
    # 更新与合同清单相关联的项目
    def update_project(self,formatId,*deptIds):
        url = self.builder + f'/rs/govern/contract/update/{formatId}'
        resp = self.Webrequests.post_json(url,deptIds,self.headers_builder).json()
        return resp
