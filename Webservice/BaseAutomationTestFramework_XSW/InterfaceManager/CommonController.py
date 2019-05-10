#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""Common Controller"""

class GetUserRealName(CenterInterface):
    # 根据企业id和用户名获取用户真实名称
    def req_params(self,epId,*usernames):
        params = {
          "epId": epId,
          "usernames": usernames
        }
        return params

    def get_user_realname(self,data):
        url = self.builder + '/common/remiz/realName'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class GetApplyUploadUrl(CenterInterface):
    # 获取文件上传地址
    def req_params(self,fileMd5,fileSize):
        params = {
          "fileMd5": fileMd5,
          "fileSize": fileSize
        }
        return params

    def get_apply_upload_url(self,data):
        url = self.builder + '/common/applyUploadUrl'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class RemizGetAccessCode(CenterInterface):
    # remiz客户端验证,返回权限码
    def req_params(self,enterpriseId,password,username):
        params = {
          "enterpriseId": enterpriseId,
          "password": password,
          "username": username
        }
        return params

    def get_access_code(self,data):
        url = self.builder + '/common/remiz/client/validate'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class UploadHead(CenterInterface):
    # 本地上传头像图片并返回上传后的文件uuid
    def req_params(self,base64Str,fileName):
        params = {
              "base64Str": base64Str,
              "fileName": fileName
            }
        return params

    def upload_head(self,data):
        url = self.builder + '/common/uploadHead'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class UploadAttachFile(CenterInterface):
    # 上传附件
    def upload_attach_file(self,filename):
        url = self.builder + '/common/attach'
        filepath = root + os.sep + 'Data'+ os.sep + f'UploadData/{filename}'
        with open(filepath, 'rb') as fp:
            files = {'file': (filename, fp,
                              'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
            del self.headers_builder['Content-type']
            self.headers_builder['Cookie'] = self.headers_builder.get('Cookie').split()[
                                         0] + ' pwLength=6; username=xushenwei; pw=; rzpw=96e79218965eb72c92a549dd5a330112'
            response = requests.post(url, '', self.headers_builder, files=files).json()
        return response

class GetFeedBackType(CenterInterface):
    # 获取问题列表类型
    def get_feed_bacd_type(self,productId):
        url = self.builder + f'/common/feedback/type/{productId}'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class RemizCenterVerification(CenterInterface):
    # remiz管理员center验证
    def req_params(self,enterprisePassword,enterpriseUsername,epid):
        params = {
              "enterprisePassword": enterprisePassword,
              "enterpriseUsername": enterpriseUsername,
              "epid": epid,
              "isSubAdmin": False
            }
        return params

    def center_verification(self,data):
        url = self.builder + '/common/remiz/center/validate'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class AddFeedBack(CenterInterface):
    # 提交问题反馈
    def req_params(self):
        attachs = []
        attachsInfo = {
                  "fileId": "string",
                  "fileName": "string",
                  "fileType": 0
                    }
        attachs.append(attachsInfo)
        params = {
              "attachs": attachs,
              "contact": "string",
              "contactinfo": "string",
              "content": "string",
              "deployment": "string",
              "deviceinfo": "string",
              "enterprise": "string",
              "epid": 0,
              "productId": 0,
              "type": 0,
              "version": "string"
            }
        return params
    def certain_params(self):
        params = {
                "attachs": [{
                    "fileId": "",
                    "fileName": "",
                    "fileType": 0
                }],
                "contact": '',
                "contactinfo": '',
                "content": "",
                "deployment": "enterprise",
                "deviceinfo": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
                "enterprise": "上海鲁班软件内网测试企业2",
                "epid": LoginConfig['epid'],
                "productId": 888,
                "type": "",
                "version": "8.7.0"
            }
        return params

    def add_feed_back(self,data):
        url = self.builder + '/common/feedback/problem'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp
