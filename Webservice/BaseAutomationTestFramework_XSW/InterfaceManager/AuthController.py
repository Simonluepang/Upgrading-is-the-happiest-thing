#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""用户权限"""

class SaveUserProjectInfo(CenterInterface):
    # 保存工程授权信息
    def req_params(self):
        params = {"isAll":False,"ppIds":{"4539e96d9c794dad9315ee8d0e3fa6b5":[131878]},"userName":"15800968817"}
        return params

    def save_user_project_info(self,data):
        url = self.builder + '/authRest/saveUserProjectInfo'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp
