#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""流程后台相关接口"""

class PublishTemplate(CenterInterface):
    # 发布流程类型模板
    def list_made(self,*args):
        # 创建列表
        params = []
        for i in args:
            params.append(i)
        return params

    def node_info(self,approvalType,roleId,roleName,userName,realName,approverType,nodeName):
        # 返回节点信息
        params ={
                "approvalType": approvalType,       # 1或签 2会签
                "approverRoleList": [{
                    "roleId": roleId,
                    "roleName": roleName
                }],
                "approverType": approverType,       # 0指定角色 1指定人
                "approverUserList": [{
                    "userName": userName,
                    "realName": realName
                }],
                "nodeName": nodeName
            }

        return params

    def node_info_list(self,*args):
        # 创建节点信息列表
        params = [
            {
                "nodeName": "发起人",
                "approverType": 0,
                "approverRoleList": [],
                "approverUserList": [],
                "approvalType": 1,
                "isCanDelete": False
            }
        ]
        for i in args:
            params.append(i)
        return params

    def req_params(self, processNodeList, remark, typeName,sponsorType, sponsorRoleList, sponsorUserList,
                   templateid=''):
        params = {
              "id": templateid,                     # 流程模板id，新建时为空
              "processNodeList": processNodeList,   # 流程节点信息列表
              "remark": remark,                     # 流程模板备注信息
              "sponsorType": int(sponsorType),      # 发起人类型，0：全员可发起 1:指定角色或指定人
              "sponsorRoleList": sponsorRoleList,   # 发起人角色列表
              "sponsorUserList": sponsorUserList,   # 发起人成员列表
              "typeName": typeName                  # 流程模板名称
            }
        return params

    def range_process_node_list(self,approvalType,approverList,approverType,num):
        # 自动创建列表信息
        params = [
            {
                "approvalType": 1,
                "approverList": [],
                "approverType": 1,
                "nodeName": "发起人"
            }
        ]
        for i in range(num):
            node_params = {
                "approvalType": int(approvalType),
                "approverList": approverList,
                "approverType": int(approverType),
                "nodeName": "节点名称"+str(i)
            }
            params.append(node_params)
        return params

    def publish_template(self,data):
        url = self.LBprocess + '/process/deploy'
        resp = self.Webrequests.post_json(url,data,self.headers_process).json()
        return resp

class DeleteInstance(CenterInterface):
    # 批量删除流程实例
    def delete_instance(self,*instanceids):
        url = self.LBprocess + '/process/instance'
        resp = self.Webrequests.delete(url,instanceids,self.headers_process).json()
        return resp

class ListInstace(CenterInterface):
    # 流程实例列表
    def req_params(self, keyword, processType, status, endDateOfEnd='', endDateOfStart='', startDateOfEnd='',
                   startDateOfStart='', page=1, size=1000, property='keyword', direction=0):
        params = {
          "endDateOfEnd": endDateOfEnd,                 # 结束时间
          "endDateOfStart": endDateOfStart,
          "keyword": keyword,                           # 搜索关键字 ProcessCode
          "orders": [                                   # 排序条件
            {
              "direction": int(direction),              # 排序方式：0 ASC 1 DESC
              "property": property                      # 要排序的字段名
            }
          ],
          "page": int(page),                            # 请求的页码
          "processType": processType,                   # 流程类型
          "size": int(size),                            # 每页记录数
          "startDateOfEnd": startDateOfEnd,             # 开始时间
          "startDateOfStart": startDateOfStart,
          "status": int(status)                         # 流程状态：0 已完成 1 进行中
        }
        return params

    def certain_params(self):
        params = {
              "endDateOfEnd": "",
              "endDateOfStart": "",
              "keyword": "",
              "orders": [
            {
              "direction": 0,                       # 排序方式：0 ASC 1 DESC
              "property": 'processCode'             # 要排序的字段名
            }
          ],
              "page": 1,
              "processType": "",
              "size": 100,
              "startDateOfEnd": "",
              "startDateOfStart": "",
              "status": 1
            }
        return params

    def list_instance(self,data):
        url = self.LBprocess + '/process/instances'
        resp = self.Webrequests.post_json(url,data,self.headers_process).json()
        return resp

class DeleteTemplate(CenterInterface):
    # 批量删除流程模板
    def delete_template(self,*templeIds):
        url = self.LBprocess + '/process/template'
        resp = self.Webrequests.delete(url,templeIds,self.headers_process).json()
        return resp

class GetTemplateDetail(CenterInterface):
    # 获取流程模板详情
    def get_template_detail(self,templateid):       # typeId
        url = self.LBprocess + f"/process/template/{templateid}"
        resp = self.Webrequests.get(url,"",self.headers_process).json()
        return resp

class UpdateSwitchStatus(CenterInterface):
    # 流程模板更新启用状态
    def update_switch_status(self,templateid):      # typeId
        url = self.LBprocess + f'/process/template/switchStatus/{templateid}'
        resp = self.Webrequests.put(url,'',self.headers_process).json()
        return resp

class ListTemplate(CenterInterface):
    # 流程模板列表
    def req_params(self,keyword,direction=0,property='updateTime',page=1,size=1000):
        params = {
          "keyword": keyword,               # 查询的关键字-流程类型名称
          "orders": [
            {
              "direction": int(direction),  # 排序方式 0 ASC 1 DESC
              "property": property          # 要排序的字段名
            }
          ],
          "page": int(page),                # 请求的页码，从1开始
          "size": int(size)                 # 每页的记录数,不指定表示不分页
        }
        return params

    def list_template(self,data):
        url = self.LBprocess + '/process/templates'
        resp = self.Webrequests.post_json(url,data,self.headers_process).json()
        return resp

class GetInstanceRecord(CenterInterface):
    # 流程审批记录获取
    def get_instance_record(self,processInstanceId):        # ProcessCode
        url = self.LBprocess + f'/process/record/{processInstanceId}'
        resp = self.Webrequests.get(url,'',self.headers_process).json()
        return resp

class GetProcessTypeName(CenterInterface):
    # 流程数据筛选条件流程模板名称列表
    def get_process_type_name(self):
        url = self.LBprocess + '/process/templates/name'
        resp = self.Webrequests.get(url,'',self.headers_process).json()
        return resp

class ProcessInstanceTransfer(CenterInterface):
    # 流程实例转交
    def process_instance_transfer(self,processInstanceId,fromUser,toUser):
        url = self.LBprocess + f'/process/transfer/{processInstanceId}/from/{fromUser}/to/{toUser}'
        resp = self.Webrequests.put(url,'',self.headers_process).json()
        return resp

class CreateInstance(CenterInterface):
    # 发起人创建审批表单
    def req_params(self):
        docs = [{
                  "docMd5": "string",
                  "docName": "string",
                  "docUuid": "string",
                  "extension": "string",
                  "size": 0,
                  "sourceType": 0
                }]
        pictures = [
                {
                  "extension": "string",
                  "md5": "string",
                  "name": "string",
                  "size": 0,
                  "thumbnailMd5": "string",
                  "thumbnailSize": 0,
                  "thumbnailUuid": "string",
                  "uuid": "string"
                }
              ]
        projBinds = [
                {
                  "attrname": "string",
                  "compClass": "string",
                  "floor": "string",
                  "handle": "string",
                  "ppid": 0,
                  "projType": "string",
                  "spec": "string",
                  "subClass": "string",
                  "treenode": "string"
                }
              ]
        speech = {
                "duration": 0,
                "md5": "string",
                "size": 0,
                "uuid": "string"
        }
        params = {
              "approvalTypeId": "string",
              "approvalTypeName": "string",
              "bindType": 0,
              "content": "string",
              "deptId": "string",
              "docs": docs,
              "name": "string",
              "pictures": pictures,
              "ppid": 0,
              "priorityId": 0,
              "projBinds": projBinds,
              "remarks": "string",
              "speech": speech}
        return params

    def certain_params(self,approvalTypeId,approvalTypeName,deptId):
        params = {
                "approvalTypeId": approvalTypeId,                       # 审批类型Id
                "approvalTypeName": approvalTypeName,                   # 审批类型名称
                "bindType": 0,                                          # 绑定类型
                "content": "大吉大利",                                   # 审批内容
                "deptId": deptId,                                       # 项目部id
                "name": "徐莘伟测试流程实例",                             # 主题名称
                "priorityId": 1,                                        # 优先级
                "remarks": ''                                           # 备注
            }
        return params

    def create_instance(self,data):
        url = self.LBprocess + '/approval/operation/ApprovalForm'
        resp = self.Webrequests.post_json(url,data,self.headers_process).json()
        return resp

class SubmitTask(CenterInterface):
    # 审批人提交审批
    def certain_params(self,formTaskId):
        params = {
          "formTaskId": formTaskId,   # tenantTaskId审批过程任务id
          "message": "access"       # 审批意见
        }
        return params

    def submit_task(self,data):
        url = self.LBprocess + '/approval/operation/submit'
        resp = self.Webrequests.post_json(url,data,self.headers_process).json()
        return resp

class FindInstanceInfo(CreateInstance):
    # 查询流程实例详情
    def find_instance_info(self,instanceid):
        url = self.LBprocess + f'/approval/common/approvalFormDetail/{instanceid}'
        resp = self.Webrequests.get(url,'',self.headers_process).json()
        return resp

class ProcessJump(CenterInterface):
    # Process 302 跳转
    def jump(self):
        url = self.LBprocess + '/process/jump'
        resp = self.Webrequests.get(url,'',self.headers_process).json()
        return resp