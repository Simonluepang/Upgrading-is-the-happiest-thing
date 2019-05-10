#!/usr/bin/env python
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""工程隐患库"""

class AddDangerLib(CenterInterface):
    # 新增隐患内容接口
    def req_params(self,content,description,factorId,typeId):
        params = {
          "content": content,
          "description": description,
          "factorId": factorId,
          "typeId": typeId
        }
        return params

    def add_dangerlib(self, data):
        url = self.builder + "/project/dangerlib/lib"
        response = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return response

class DeleteDangerLib(CenterInterface):
    # 删除隐患内容
    def delete_all_dangerlib(self,data):
        url = self.builder + "/project/dangerlib/libs"
        response = self.Webrequests.delete(url, data, self.headers_builder).json()
        return response

    def delete_dangerlib(self,*dangerInfos):
        url = self.builder + "/project/dangerlib/libs"
        response = self.Webrequests.delete(url, dangerInfos, self.headers_builder).json()
        return response

class UpdateDangerLib(CenterInterface):
    # 修改隐患内容
    def req_params(self,content,description,factorId,typeId):
        params = {
          "content": content,
          "description": description,
          "factorId": factorId,
          "typeId": typeId
        }
        return params

    def update_dangerlib(self,dangerid,data):
        url = self.builder + f'/project/dangerlib/lib/{dangerid}'
        response = self.Webrequests.put(url,data,self.headers_builder).json()
        return response

class ListDangerLib(CenterInterface):
    # 查询隐患库列表
    def rep_params(self,factorId,typeId,page=1,size=10):
        orders =[{
            "direction": 0,
            "property": "updateTime"
        }]
        params = {
          "factorId": factorId,
          "keyword": '',
          "orders": orders,
          "page": page,
          "size": size,
          "typeId": typeId
        }
        return params

    def list_dangerlib(self,data):
        url = self.builder + "/project/dangerlib/libs"
        response = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return response

class TemplateDangerLib(CenterInterface):
    # 查询隐患库模板列表
    def req_params(self,factorId='',typeId=''):
        orders =[{
            "direction": 1,
            "property": "updateTime"
        }]
        params = {
            "factorId": factorId,
            "keyword": "",
            "orders": orders,
            "page": 1,
            "size": 10,
            "typeId": typeId
        }
        return params

    def template_dangerlib(self, data):
        url = self.builder + '/project/dangerlib/templates'
        response = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return response

class QuoteDangerTemplate(CenterInterface):
    # 引用模板内容
    def quote_dangertemplate(self,*dangerInfos,quotetype='false'):
        url = self.builder + f"/project/dangerlib/templates/type/{quotetype}"
        response = self.Webrequests.put(url,dangerInfos,self.headers_builder).json()
        return response

class TemplateReadStatus(CenterInterface):
    # 隐患模板更新提示阅读状态设置
    def template_read_status(self):
        url = self.builder + "/project/dangerlib/templates/readstatus"
        response = self.Webrequests.put(url,'',self.headers_builder).json()
        return response

class RedTipDangerLibTeplate(CenterInterface):
    # 隐患库模板红点接口
    def red_tip(self):
        url = self.builder + '/project/dangerlib/templates/redtip'
        response = self.Webrequests.get(url,'',self.headers_builder).json()
        return response

class ListDangerFactor(CenterInterface):
    # 查询隐患要素接口
    def list_dangerfactor(self,dangertype,status):
        url = self.builder + f'/project/dangerlib/condition/dangerfactors/type/{dangertype}/status/{status}'
        response = self.Webrequests.get(url,'',self.headers_builder).json()
        return response

class ListDangerType(CenterInterface):
    # 查询隐患类型接口
    def list_dangertype(self,factorId,dangertype,status):
        url = self.builder + f'/project/dangerlib/condition/dangertypes/factorId/{factorId}/type/{dangertype}/status/{status}'
        response = self.Webrequests.get(url,'',self.headers_builder).json()
        return response

class ExportDangerLib(CenterInterface):
    # 导出隐患库接口
    def export_dangerlib(self):
        url = self.builder + '/project/dangerlib/lib/export'
        response = self.Webrequests.get(url,'',self.headers_builder).status_code
        return response

class ImportDangerLib(CenterInterface):
    # 导入隐患库Excel
    def import_dangerlib(self):
        url = self.builder + '/project/dangerlib/lib/import'
        filepath = root + os.sep + 'Data' + os.sep + 'UploadData/TestUploadLib.xlsx'
        with open(filepath, 'rb') as fp:
            files = {'file': ('TestUploadLib.xlsx', fp,
                              'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
            del self.headers_builder['Content-type']
            self.headers_builder['Cookie'] = self.headers_builder.get('Cookie').split()[
                                         0] + ' pwLength=6; username=xushenwei; pw=; rzpw=96e79218965eb72c92a549dd5a330112'
            response = requests.post(url=url, data='', headers=self.headers_builder, files=files).json()
        return response

if __name__ == '__main__':
    ImportDangerLib().import_dangerlib()