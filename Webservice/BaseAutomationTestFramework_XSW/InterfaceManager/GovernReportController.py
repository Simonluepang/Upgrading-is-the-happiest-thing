#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""原Govern报表订阅相关接口"""

class GetDataType(CenterInterface):
    # 数据类型列表下拉框数据
    def get_datatype(self):
        url = self.builder + '/rs/oldgovern/report/getDataType'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class GetOrgNodes(CenterInterface):
    # 组织节点列表下拉框数据
    def get_orgnodes(self):
        url = self.builder + '/rs/oldgovern/report/getOrgNodes'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class GetReportRoleList(CenterInterface):
    # 查询对应角色的报表模板权限,返回有权限的报表id列表
    def get_reportrolelist(self,roleId):
        url = self.builder + f'/rs/oldgovern/report/getReportList/{roleId}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class DeleteReportPermissions(CenterInterface):
    # 删除角色对应的报表权限
    def req_params(self,epid,reportid,roleid):
        params = [
          {
            "enterpriseId": epid,
            "reportId": reportid,
            "roleId": roleid
          }
        ]
        return params

    def del_reportpermissions(self,data):
        url = self.builder + '/rs/oldgovern/report/delReportPermissions'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class AddReportPermissions(CenterInterface):
    # 添加角色对应的报表权限
    def req_params(self,enterpriseId,reportId,roleId):
        params = [
          {
            "enterpriseId": enterpriseId,
            "reportId": reportId,
            "roleId": roleId
          }
        ]
        return params

    def add_reportpermissions(self,data):
        url = self.builder + '/rs/oldgovern/report/addReportPermissions'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class GetReportList(CenterInterface):
    # 获取报表列表数据
    def req_params(self,dataType,orgCode):
        params = {
          "dataType": dataType,
          "orgCode": orgCode
        }
        return params

    def get_reportlist(self,data):
        url = self.builder + '/rs/oldgovern/report/getReportList'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp
