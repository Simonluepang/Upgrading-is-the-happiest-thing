#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""应用配置-原BW"""

class CheckProjectsFile(CenterInterface):
    # 分页查询项目的hsf文件
    def check_projects_file(self,projectId):
        url = self.builder + f'/appconfig/bw/projects/{projectId}/files'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class CheckRecyclesFile(CenterInterface):
    # 分页查询回收站的hsf文件
    def check_recycles_file(self,projectId):
        url = self.builder + f'/appconfig/bw/recycles/{projectId}/files'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class ListProjectLib(CenterInterface):
    # 分页查询项目库列表
    def list_project_lib(self):
        url = self.builder + '/appconfig/bw/projects'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class ListProjectMajor(CenterInterface):
    # 查询所有项目专业列表
    def list_project_major(self,projectId):
        url = self.builder + f'/appconfig/bw/projects/{projectId}/majors'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class ListRecycles(CenterInterface):
    # 分页查询回收站列表
    def list_recycles(self):
        url = self.builder + '/appconfig/bw/recycles'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class ListCompletesMajors(CenterInterface):
    # 查询所有已完成专业列表
    def list_complete_majors(self,projectId):
        url = self.builder + f'/appconfig/bw/completes/{projectId}/majors'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class ListComplete(CenterInterface):
    # 分页查询已完成列表
    def list_complete(self):
        url = self.builder + '/appconfig/bw/completes'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class ListRecyclesMajors(CenterInterface):
    # 查询所有回收站专业列表
    def list_recycles_majors(self,projectId):
        url = self.builder + f'/appconfig/bw/recycles/{projectId}/majors'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class CheckCompletesFile(CenterInterface):
    # 分页查询已完成的hsf文件
    def check_completes_file(self,projectId):
        url = self.builder + f'/appconfig/bw/completes/{projectId}/files'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class CheckPermissions(CenterInterface):
    # 账号分配获取权限信息
    def check_permissions(self,projectId):
        url = self.builder + f'/appconfig/bw/permissions/{projectId}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class UpdatePermissions(CenterInterface):
    # 更新账号权限信息
    def update_permission(self,projectId,*username):
        url = self.builder + f'/appconfig/bw/permissions/{projectId}'
        resp = self.Webrequests.put(url,username,self.headers_builder).json()
        return resp
