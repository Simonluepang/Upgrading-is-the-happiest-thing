#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""应用权限"""

class GetAPPAllocationPackageInfo(CenterInterface):
    # 获取各个分配类型各个套餐/产品信息
    def get_APPallocation_package_info(self):
        url = self.builder + '/appallocation/getAppAllocationPackageInfo'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class UpdateUserPackageAuth(CenterInterface):
    # 更新用户套餐授权
    def req_params(self,functionId,heldId,operType,orgId,packageType,*userNames):
        params = {
          "functionId": functionId,
          "heldId": heldId,
          "operType": operType,
          "orgId": orgId,
          "packageType": packageType,
          "userNames": userNames
        }
        return params

    def update_user_package_auth(self,data):
        url = self.builder + '/appallocation/updateUserPackageAuth'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class GetAdminManageUserList(CenterInterface):
    # 根据组织获取管理员能够管理的可授权用户列表
    def get_admin_manage_user_list(self, packageId, orgId):
        url = self.builder + f'/appallocation/getAdminManageUserList/{packageId}/{orgId}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class GetUserAuthBimAppPackage(CenterInterface):
    # 获取用户授权的BimApp套餐
    def get_admin_auth_bim_APP_package(self, userName):
        url = self.builder + f'/appallocation/getUserAuthBimAppPackage/{userName}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class GetPackageAllocatedUserList(CenterInterface):
    # 查询云部署套餐用户授权列表
    def req_params(self,heldId,packageId,packageType,userName):
        pageParam = {
            "beginNumber": 0,
            "page": 1,
            "pageSize": 10,
            "sortField": "",
            "sortType": ""
          }
        params = {
          "heldId": heldId,
          "packageId": packageId,
          "packageType": packageType,
          "pageParam": pageParam,
          "searchKey": userName
        }
        return params

    def get_package_allocated_user_list(self,data):
        url = self.builder + '/appallocation/getPackageAllocatedUserList'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class GetOrderAndAllocationInfoByPackage(CenterInterface):
    # 查询套餐/产品对应的订单列表以及该套餐分配情况,获取pds套餐订单分配情况时单独调用接口
    def req_params(self,packageId,packageType):
        packageInfo = {
            "packageId": packageId,
            "packageType": packageType
        }
        params = []
        params.append(packageInfo)
        return params

    def get_order_and_allocation_info(self,data):
        url = self.builder + '/appallocation/getOrderAndAllocationInfoByPackage'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class GetUserAuthQuotaLibraryPackage(CenterInterface):
    # 获取用户授权的定额库套餐
    def get_user_auth_quota_library_package(self,userName):
        url = self.builder + f'/appallocation/getUserAuthQuotaLibraryPackage/{userName}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class GetUserAuthBasicPackage(CenterInterface):
    # 获取用户授权的基础客户端套餐
    def get_user_auth_basic_package(self,userName):
        url = self.builder + f'/appallocation/getUserAuthBasicPackage/{userName}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class GetUserAuthPDSPackage(CenterInterface):
    # 获取用户授权的PDS套餐
    def get_user_auth_PDSpackage(self,userName):
        url = self.builder + f'/appallocation/getUserAuthPDSPackage/{userName}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp