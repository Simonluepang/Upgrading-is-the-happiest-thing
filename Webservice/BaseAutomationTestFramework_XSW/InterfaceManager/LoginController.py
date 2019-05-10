#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""登录信息"""

class GetMenuMessage(CenterInterface):
    # 获取center菜单信息
    def get_menu_message(self,parMenuId):
        url = self.builder + f'/subs/menu/{parMenuId}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class UnbindPassport(CenterInterface):
    # 解绑通行证
    def unbind_passport(self):
        url = self.builder + '/subs/unbindPassport'
        resp = self.Webrequests.post_json(url,'',self.headers_builder).json()
        return resp

class UpdatePassword(CenterInterface):
    # 修改管理员的密码
    def req_params(self,currentPw,newPw):
        params = {
          "currentPw": currentPw,
          "newPw": newPw
        }
        return params

    def update_password(self,data):
        url = self.builder + '/subs/updatePassword'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class SetUserHead(CenterInterface):
    # 设置用户头像(超级管理员可以修改头像,子管理员不能修改)
    def set_user_head(self,fileUuid,*fileUuids):
        url = self.builder + f'/subs/userHead/{fileUuid}'
        resp = self.Webrequests.post_json(url,fileUuids,self.headers_builder).json()
        return resp

class GetHeadSettingMenu(CenterInterface):
    # 获取用户设置相关菜单对象
    def get_head_setting_menu(self):
        url = self.builder + '/subs/headSettingMenu'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class BindPassport(CenterInterface):
    # 超级管理员绑定通行证
    def req_params(self,adminPassword,passportName,passportPassword):
        params = {
              "adminPassword": adminPassword,
              "passportName": passportName,
              "passportPassword": passportPassword
            }
        return params

    def bind_passport(self,data):
        url = self.builder + '/subs/bindPassport'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class GetUserHead(CenterInterface):
    # 获取用户头像
    def get_user_head(self):
        url = self.builder + '/subs/userHead'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class CheckPassportIsBind(CenterInterface):
    # 判断通行证账号是否已被绑定
    def check_passport_is_bind(self,passportName):
        url = self.builder + f'/subs/isBindPassport/{passportName}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp
