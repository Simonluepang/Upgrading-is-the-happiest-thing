#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""BIM回收站相关接口"""

class ReductionProj(CenterInterface):
    # 还原回收站中的工程
    def reduction_project(self,packageType,*projIds):
        url = self.builder + f'/rs/bimRecycleRest/reductionProjs/{packageType}'
        resp = self.Webrequests.post_json(url,projIds,self.headers_builder).json()
        return resp

class DeleteProject(CenterInterface):
    # 删除回收站中的工程
    def req_params(self,*projIds,deleteAll=False,packageType=1):
        params = {
          "deleteAll": deleteAll,
          "packageType": packageType,
          "projIds": projIds
        }
        return params

    def delete_project(self,data):
        url = self.builder + '/rs/bimRecycleRest/deleteProject'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp