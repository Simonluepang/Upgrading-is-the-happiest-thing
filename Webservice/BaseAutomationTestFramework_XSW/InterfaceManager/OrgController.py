#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""组织机构、项目部"""

class DeleteOrg(CenterInterface):
    # 删除组织机构
    def delete_org(self,orgId):
        url = self.builder + f'/org/{orgId}'
        resp = self.Webrequests.delete(url,'',self.headers_builder).json()
        return resp

class GetOrg(CenterInterface):
    # 查询有组织机构信息，携带管理员信息
    def get_org(self,orgId):
        url = self.builder + f'/org/{orgId}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class UpdateOrg(CenterInterface):
    # 编辑组织机构
    def req_params(self,name):
        params = {
          "name": name
        }
        return params

    def update_org(self,orgId,data):
        url = self.builder + f'/org/{orgId}'
        resp = self.Webrequests.put(url,data,self.headers_builder).json()
        return resp

class UpdateDepts(CenterInterface):
    # 编辑项目部信息
    def req_params(self, name, managerName='ManagerName', mobile='13111111111', location=440923, contractType=1,
                   status=0, area=100):
        params = {
          "area": area,
          "bimConsultation": "string",
          "buildOrg": "string",
          "constructionOrg": "string",
          "contractType": contractType,
          "costConsultation": "string",
          "deptProperties": 1,
          "deptType": "1",
          "designOrg": "string",
          "endDate": "2018-11-26T07:27:52.182Z",
          "location": location,
          "managerName": managerName ,
          "mileage": "string",
          "mobile": mobile,
          "name": name,
          "proxyOrg": "string",
          "remarks": "string",
          "startDate": "2018-11-10T07:27:52.183Z",
          "status": status,
          "supervisorOrg": "string",
          "surveyOrg": "string"
        }
        return params

    def update_depts(self,deptId,data):
        url = self.builder + f'/org/depts/{deptId}'
        resp = self.Webrequests.put(url,data,self.headers_builder).json()
        return resp

class GetNodes(CenterInterface):
    # 查询组织机构树（包括项目部）
    def get_nodes(self):
        url = self.builder + '/org/nodes'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class CheckNodesName(CenterInterface):
    # 检查机构名称是否存在，编辑情况下需要传递orgId查询参数
    def req_params(self,excludeId,name,orgType):
        params = {
          "excludeId": excludeId,
          "name": name,
          "orgType": orgType
        }
        return params

    def check_nodes_name(self,data):
        url = self.builder + '/org/nodes/names/'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class AddDept(CenterInterface):
    # 创建新的项目部
    def req_params(self, name, managerName='ManagerName', mobile='13111111111', location=440923, contractType=1,
                   status=0, area=100):
        params = {
          "area": area,
          "bimConsultation": "string",
          "buildOrg": "string",
          "constructionOrg": "string",
          "contractType": contractType,
          "costConsultation": "string",
          "deptProperties": 1,
          "deptType": "1",
          "designOrg": "string",
          "endDate": "2018-11-26T07:27:52.182Z",
          "location": location,
          "managerName": managerName ,
          "mileage": "string",
          "mobile": mobile,
          "name": name,
          "proxyOrg": "string",
          "remarks": "string",
          "startDate": "2018-11-10T07:27:52.183Z",
          "status": status,
          "supervisorOrg": "string",
          "surveyOrg": "string"
        }
        return params

    def add_dept(self,parentId,data):
        url = self.builder + f'/org/{parentId}/depts'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class AddOrg(CenterInterface):
    # 创建新的组织机构
    def req_params(self,name):
        params = {
          "name": name
        }
        return params

    def add_org(self,orgId,data):
        url = self.builder + f'/org/{orgId}/subs'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp
