#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2018/8/1 16:03
# @Author  : hubiao
# @File    : test_BimAdamin.py

import time,json,re
import pytest
from util.Config import ManageConfig

class Test_Center:
    '''
    登录演示企业，查询添加的用户是否自动添加到了演示企业、是否分配了所有PDS应用、项目部、工程、工作集、Grover工程、资料目录授权
    '''
    def setup_class(self):
        sysadmin = ManageConfig().getConfig('sysadmin')
        self.wf = ManageConfig()
        self.username = sysadmin["newUserName"]
        self.packageInfoNumber = 0
        self.orgId = ''

    @pytest.mark.parametrize('resource,method',[('/org/nodes','get')])
    def test_nodes(self,CenterBuilder,resource,method):
        # 获取组织节点
        response = CenterBuilder.JsonRequest(method,resource)
        assert response.status_code == 200
        response = response.json()
        if response["code"] == 200 and len(response["result"]) != 0:
            for result in response['result']:
                if result["root"] is True:
                    Test_Center.orgId = result["id"]
        else:
            assert False

    @pytest.mark.parametrize('resource,method',[('/userRest/findUsers','post')])
    def test_findUsers(self,CenterBuilder,resource,method):
        # 搜索指定用户
        body = {"direction":1,"ignoreCase":True,"orgId":self.orgId,"roleId":"","searchStr":self.username,"property":"updateDate","pageNum":1,"pageSize":10}
        response = CenterBuilder.JsonRequest(method,resource,json.dumps(body))
        assert response.status_code == 200
        response = response.json()
        if response["code"] == 200 and len(response["result"]["result"]) != 0:
            assert len(response['result']["result"]) == 1
        else:
            assert False

    @pytest.mark.parametrize('resource,method',[('/appallocation/getAppAllocationPackageInfo','get')])
    def test_getAppAllocationPackageInfo(self,CenterBuilder,resource,method):
        # 获取应用授权信息
        response = CenterBuilder.JsonRequest(method,resource)
        assert response.status_code == 200
        response = response.json()
        if response["code"] == 200 and len(response["result"]) != 0:
            for package in response['result']:
                if package["packageType"] == 3:
                    Test_Center.packageInfoNumber = len(package["packageInfos"])
        else:
            assert False

    @pytest.mark.parametrize('method',[('get')])
    def test_getUserAuthPDSPackage(self,CenterBuilder,method):
        # 获取指定用户的PDS授权信息
        resource = f'/appallocation/getUserAuthPDSPackage/{self.username}'
        response = CenterBuilder.JsonRequest(method,resource)
        assert response.status_code == 200
        response = response.json()
        if response["code"] == 200 and len(response["result"]) != 0:
            #验证是否分配了全部PDS套餐
            assert self.packageInfoNumber != 0
            assert len(response['result']) > self.packageInfoNumber
        else:
            assert False

    @pytest.mark.parametrize('method',[('get')])
    def test_findUserDeptInfo(self,CenterBuilder,method):
        # 获取指定用户的项目部授权信息
        resource = f'/authRest/findUserDeptInfo/{self.username}'
        response = CenterBuilder.JsonRequest(method,resource)
        assert response.status_code == 200
        response = response.json()
        if response["code"] == 200 and len(response["result"]) != 0:
            #判断是否授权了顶级公司节点
            assert self.orgId in response['result']["orgIds"]
        else:
            assert False

    @pytest.mark.parametrize('method',[('get')])
    def test_findUserProjectInfo(self,CenterBuilder,method):
        # 获取指定用户的工程授权信息
        resource = f'/authRest/findUserProjectInfo/{self.username}'
        response = CenterBuilder.JsonRequest(method,resource)
        assert response.status_code == 200
        response = response.json()
        if response["code"] == 200 and len(response["result"]) != 0:
            assert response['result']["isAll"] == True
        else:
            assert False

    @pytest.mark.parametrize('method',[('get')])
    def test_findUserWorkSetInfo(self,CenterBuilder,method):
        # 获取指定用户的Works分配信息
        resource = f'/authRest/findUserWorkSetInfo/{self.username}'
        response = CenterBuilder.JsonRequest(method,resource)
        assert response.status_code == 200
        response = response.json()
        if response["code"] == 200 and len(response["result"]) != 0:
            assert response['result']["isAll"] == True
        else:
            assert False

    @pytest.mark.parametrize('method',[('get')])
    def test_findUserGovernProjectInfo(self,CenterBuilder,method):
        # 获取指定用户的Govern工程分配信息
        resource = f'/authRest/findUserGovernProjectInfo/{self.username}'
        response = CenterBuilder.JsonRequest(method,resource)
        assert response.status_code == 200
        response = response.json()
        if response["code"] == 200 and len(response["result"]) != 0:
            assert response['result']["isAll"] == True
        else:
            assert False

    @pytest.mark.parametrize('method',[('get')])
    def test_findUserDataDirectoryIds(self,CenterBuilder,method):
        # 获取指定用户的目录分配信息
        resource = f'/authRest/findUserDataDirectoryIds/{self.username}/-1'
        response = CenterBuilder.JsonRequest(method,resource)
        assert response.status_code == 200
        response = response.json()
        if response["code"] == 200 and len(response["result"]) != 0:
            assert response['result']["chooseAll"] == True
        else:
            assert False

if __name__ == "__main__":
    pytest.main(["-s", "test_domeCenter.py"])
