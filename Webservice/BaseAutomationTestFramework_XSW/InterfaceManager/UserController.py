#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""用户Controller"""

class AddUser(CenterInterface):
    # 添加单个用户并返回userId
    def req_params(self,userName,realName,roleId,passWord='96e79218965eb72c92a549dd5a330112',mobile='',email='',userId='',remarks=''):
        params = {
            "email": email,
            "mobile": mobile,
            "passWord": passWord,
            "realName": realName,
            "remarks": remarks,
            "roleId": roleId,
            "userId": userId,
            "userName": userName
        }
        return params

    def add_user(self,data):
        url = self.builder + '/userRest/addUser'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class DeleteUsers(CenterInterface):
    # 批量删除用户
    def delete_users(self,*username):
        url = self.builder + '/userRest/deleteUsers'
        resp = self.Webrequests.post_json(url,username,self.headers_builder).json()
        return resp

if __name__ == '__main__':
    pass