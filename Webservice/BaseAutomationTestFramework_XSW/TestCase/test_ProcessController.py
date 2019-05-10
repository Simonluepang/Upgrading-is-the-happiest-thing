#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.ProcessController import *
from InterfaceManager.RoleController import *
from InterfaceManager.OrgController import *

# class TemplateData():
#
#     def find_role(self):
#         # 查找角色ID
#         getRoleresp = FindRoles().find_roles().get('result')
#
#         # 返回列表形式
#         role_id_list = []
#         for i in getRoleresp:
#             role_id_list.append(i.get('roleId'))
#         return role_id_list
#
#         # 返回字典形式
#         # role_id_dict = {}
#         # for i in getRoleresp:
#         #     role_id_dict[i.get('roleName')] = i.get('roleId')
#         # return role_id_dict
#
#     def range_data(self):
#         """
#         五个流程节点，均为或签，审批人为角色，全员可发起
#         :return:
#         """
#         processNodeList = PublishTemplate().range_process_node_list(1, PublishTemplate().list_made(
#             'fd8d17a9f0ac4356b5d811602e525d99'), 0, 5)
#         empty_list = []
#         templateparams = PublishTemplate().req_params(processNodeList,"testrematks","testname",0,empty_list,empty_list)
#         return templateparams
#
#     def data0(self):
#         params = {
#                 "id": "",
#                 "processNodeList": [
#                     {
#                         "approvalType": 1,
#                         "approverList": [],
#                         "approverType": 1,
#                         "nodeName": "Begin"
#                     },
#                     {
#                         "approvalType": 1,
#                         "approverList": [
#                             "xushenwei"
#                         ],
#                         "approverType": 1,
#                         "nodeName": "End"
#                     }
#                 ],
#                 "remark": "string",
#                 "sponsorRoleList": [],
#                 "sponsorType": 0,
#                 "sponsorUserList": [],
#                 "typeName" : "xswtest_CertainTemplate"
#             }
#         return params
#
#     def data1(self):
#         remarks = "全员可发起,或签节点1：一个指定角色"
#         node = PublishTemplate().node_info(1,PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd'),0,'或签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data2(self):
#         remarks = "全员可发起,或签节点1：一个指定成员"
#         node = PublishTemplate().node_info(1,PublishTemplate().list_made('xushenwei'),1,'或签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data3(self):
#         remarks = "全员可发起,或签节点1：两个指定角色"
#         node = PublishTemplate().node_info(1, PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd',
#                                                                           'c8f76d321b864adda8e017e6bb554580'), 0,
#                                            '或签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data4(self):
#         remarks = "全员可发起,或签节点1：两个指定成员"
#         node = PublishTemplate().node_info(1, PublishTemplate().list_made('xushenwei',
#                                                                           'bv-api-test'), 1,
#                                            '或签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data5(self):
#         remarks = "全员可发起,会签节点1：一个指定角色"
#         node = PublishTemplate().node_info(2,PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd'),0,'会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data6(self):
#         remarks = "全员可发起,会签节点1：一个指定成员"
#         node = PublishTemplate().node_info(2,PublishTemplate().list_made('xushenwei'),1,'会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data7(self):
#         remarks = "全员可发起,会签节点1：两个指定角色"
#         node = PublishTemplate().node_info(2, PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd',
#                                                                           'c8f76d321b864adda8e017e6bb554580'), 0,
#                                            '会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data8(self):
#         remarks = "全员可发起,会签节点1：两个指定成员"
#         node = PublishTemplate().node_info(2, PublishTemplate().list_made('xushenwei',
#                                                                           'bv-api-test'), 1,
#                                            '会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data9(self):
#         remarks = "两个发起角色,或签节点1：两个指定成员"
#         node = PublishTemplate().node_info(1, PublishTemplate().list_made('xushenwei',
#                                                                           'bv-api-test'), 1,
#                                            '或签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd','c8f76d321b864adda8e017e6bb554580')
#         sponserUser = PublishTemplate().list_made()
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',1,sponsorRole,sponserUser)
#         return data
#
#     def data10(self):
#         remarks = "两个发起成员,或签节点1：两个指定成员"
#         node = PublishTemplate().node_info(1, PublishTemplate().list_made('xushenwei',
#                                                                           'bv-api-test'), 1,
#                                            '或签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = PublishTemplate().list_made()
#         sponserUser = PublishTemplate().list_made('xushenwei','bv-api-test')
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',1,sponsorRole,sponserUser)
#         return data
#
#     def data11(self):
#         remarks = "两个发起成员两个发起角色,或签节点1：两个指定成员"
#         node = PublishTemplate().node_info(1, PublishTemplate().list_made('xushenwei',
#                                                                           'bv-api-test'), 1,
#                                            '或签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd',
#                                                   'c8f76d321b864adda8e017e6bb554580')
#         sponserUser = PublishTemplate().list_made('xushenwei','bv-api-test')
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',1,sponsorRole,sponserUser)
#         return data
#
#     def data12(self):
#         """会签角色为多个"""
#         remarks = "两个发起成员两个发起角色,或签节点1：两个指定成员;会签节点：两个指定角色"
#         node1 = PublishTemplate().node_info(1, PublishTemplate().list_made('xushenwei',
#                                                                           'bv-api-test'), 1,
#                                            '或签节点1')
#         node2 = PublishTemplate().node_info(2, PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd',
#                                                                           'bv-c8f76d321b864adda8e017e6bb554580-test'), 0,
#                                            '会签节点2')
#         node_list = PublishTemplate().node_info_list(node1,node2)
#         sponsorRole = PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd',
#                                                   'c8f76d321b864adda8e017e6bb554580')
#         sponserUser = PublishTemplate().list_made('xushenwei','bv-api-test')
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',1,sponsorRole,sponserUser)
#         return data
#
#     def data13(self):
#         remarks = "全员可发起,只有发起人节点"
#         node_list = PublishTemplate().node_info_list()
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data14(self):
#         remarks = "IOS客户端测试用审批流程"
#         node1 = PublishTemplate().node_info(1,PublishTemplate().list_made('六月','xiong1'),1,'或签节点1')
#         node2 = PublishTemplate().node_info(1, PublishTemplate().list_made('六月', 'xiong1'), 1, '或签节点2')
#         node3 = PublishTemplate().node_info(2, PublishTemplate().list_made('xiong2', 'jumao'), 1, '会签节点3')
#         node_list = PublishTemplate().node_info_list(node1,node2,node3)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list, remarks, 'IOS客户端测试用审批流程', 0, sponsorRole, sponserUser,
#                                             templateid='cX0f4d5fb1b94a599162e1cffaa5a426')
#         return data
#
#     def data15(self):
#         """或签角色为多个"""
#         remarks = "两个发起成员两个发起角色,会签节点1：两个指定成员;或签节点：两个指定角色"
#         node1 = PublishTemplate().node_info(2, PublishTemplate().list_made('xushenwei',
#                                                                           'bv-api-test'), 1,
#                                            '会签节点1')
#         node2 = PublishTemplate().node_info(1, PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd',
#                                                                           'bv-c8f76d321b864adda8e017e6bb554580-test'), 0,
#                                            '或签节点2')
#         node_list = PublishTemplate().node_info_list(node1,node2)
#         sponsorRole = PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd',
#                                                   'c8f76d321b864adda8e017e6bb554580')
#         sponserUser = PublishTemplate().list_made('xushenwei','bv-api-test')
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',1,sponsorRole,sponserUser)
#         return data
#
#     def data16(self):
#         remarks = "全员可发起,或签节点1：指定角色，角色信息为空"
#         node = PublishTemplate().node_info(1,PublishTemplate().list_made(''),0,'或签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data17(self):
#         remarks = "全员可发起,会签节点1：指定角色，角色信息为空"
#         node = PublishTemplate().node_info(2,PublishTemplate().list_made(''),0,'会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data18(self):
#         remarks = "全员可发起,或签节点1：指定成员，成员信息为空"
#         node = PublishTemplate().node_info(1,PublishTemplate().list_made(''),1,'或签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data19(self):
#         remarks = "全员可发起,会签节点1：指定成员，成员信息为空"
#         node = PublishTemplate().node_info(2,PublishTemplate().list_made(''),1,'会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data20(self):
#         remarks = "全员可发起,会签节点1：指定成员，审批方式不正确"
#         node = PublishTemplate().node_info(123,PublishTemplate().list_made('xushenwei'),1,'会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data21(self):
#         remarks = "全员可发起,会签节点1：指定成员，审批人类型不正确"
#         node = PublishTemplate().node_info(2,PublishTemplate().list_made('xushenwei'),34,'会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data22(self):
#         remarks = "全员可发起,会签节点1：指定成员，没有该审批人"
#         node = PublishTemplate().node_info(2,PublishTemplate().list_made('阿斯顿发送到发送到发送到发士大夫'),1,'会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data23(self):
#         remarks = "全员可发起,会签节点1：指定角色，没有该角色"
#         node = PublishTemplate().node_info(2,PublishTemplate().list_made('阿斯顿发送到发送到发送到发士大夫'),0,'会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data24(self):
#         remarks = "全员可发起,会签节点1：指定成员，节点名称为空"
#         node = PublishTemplate().node_info(2,PublishTemplate().list_made('xushenwei'),1,'')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',0,sponsorRole,sponserUser)
#         return data
#
#     def data25(self):
#         """节点为空"""
#         params = {
#             "id": "",
#             "processNodeList": [],
#             "remark": "节点为空",
#             "sponsorRoleList": [],
#             "sponsorType": 0,
#             "sponsorUserList": [],
#             "typeName": "节点为空"
#         }
#         return params
#
#     def data26(self):
#         remarks = "全员可发起,会签节点1：指定成员，流程名称为空"
#         node = PublishTemplate().node_info(2,PublishTemplate().list_made('xushenwei'),1,'会签节点1')
#         node_list = PublishTemplate().node_info_list(node)
#         sponsorRole = []
#         sponserUser = []
#         data = PublishTemplate().req_params(node_list,remarks,'',0,sponsorRole,sponserUser)
#         return data
#
#     def data27(self):
#         remarks = "节点名称重复"
#         node1 = PublishTemplate().node_info(2, PublishTemplate().list_made('xushenwei',
#                                                                           'bv-api-test'), 1,
#                                            '会签节点1')
#         node2 = PublishTemplate().node_info(2, PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd'), 0,
#                                            '会签节点1')
#         node_list = PublishTemplate().node_info_list(node1,node2)
#         sponsorRole = PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd',
#                                                   'c8f76d321b864adda8e017e6bb554580')
#         sponserUser = PublishTemplate().list_made('xushenwei','bv-api-test')
#         data = PublishTemplate().req_params(node_list,remarks,'徐莘伟测试发布审批流程',1,sponsorRole,sponserUser)
#         return data
#
#     def data28(self):
#         remarks = "0103测试模板-xyj"
#         node1 = PublishTemplate().node_info(1, PublishTemplate().list_made('xiong1',
#                                                                           'xiong2'), 1,
#                                            '或签节点1')
#         node2 = PublishTemplate().node_info(2, PublishTemplate().list_made('jumao','七月'), 1,
#                                            '会签节点2')
#         node_list = PublishTemplate().node_info_list(node1,node2)
#         sponsorRole = PublishTemplate().list_made()
#         sponserUser = PublishTemplate().list_made()
#         data = PublishTemplate().req_params(node_list,remarks,'0103测试模板-xyj',0,sponsorRole,sponserUser)
#         return data
#
#     def data29(self):
#         '''重复使用data'''
#         remarks = "请勿创建实例，该流程类型下实例有被删除的风险！！！！！"
#         node1 = PublishTemplate().node_info(2, PublishTemplate().list_made('xushenwei',
#                                                                           'bv-api-test'), 1,
#                                            '会签节点1')
#         node2 = PublishTemplate().node_info(1, PublishTemplate().list_made('58ff5d1b92584c74aef64ca91547b0cd'), 0,
#                                            '或签节点2')
#         node_list = PublishTemplate().node_info_list(node1,node2)
#         sponsorRole = PublishTemplate().list_made()
#         sponserUser = PublishTemplate().list_made()
#         data = PublishTemplate().req_params(node_list, remarks, '徐莘伟专用流程类型请勿引用', 0, sponsorRole, sponserUser,
#                                             'fX6c1a260ff5457a943e5e37ae905dab')
#         return data
#
#     def data30(self):
#         remarks = "0104模板(1)-xyj"
#         node1 = PublishTemplate().node_info(2, PublishTemplate().list_made('六月',
#                                                                           'xiong1'), 1,
#                                            '会签节点1')
#         node2 = PublishTemplate().node_info(1, PublishTemplate().list_made('七月','xiong2','xushenwei'), 1,
#                                            '或签节点1')
#         node3 = PublishTemplate().node_info(2, PublishTemplate().list_made('jumao',
#                                                                           '浮香丘'), 1,
#                                            '会签节点2')
#         node4 = PublishTemplate().node_info(1, PublishTemplate().list_made('xialujie'), 1,
#                                            '或签节点2')
#         node_list = PublishTemplate().node_info_list(node1,node2,node3,node4)
#         sponsorRole = PublishTemplate().list_made()
#         sponserUser = PublishTemplate().list_made()
#         data = PublishTemplate().req_params(node_list,remarks,'0104模板(1)-xyj',0,sponsorRole,sponserUser,'Xd00e8b7cf5741219e21dfeb9788bd7a')
#         return data


class SingleWebservice(object):

    def find_role(self):
        # 查找角色ID
        getRoleresp = FindRoles().find_roles().get('result')
        # 返回列表形式
        role_id_list = []
        for i in getRoleresp:
            role_id_list.append([i.get('roleId'),i.get('roleName')])
        return role_id_list

    def process_data(self,randomstring):
        remarks = "测试添加流程类型"+randomstring
        rolelist = self.find_role()
        node = PublishTemplate().node_info(1,rolelist[0][0],rolelist[0][1],'xushenwei','徐莘伟',0,'或签节点'+randomstring)
        data = PublishTemplate().req_params(PublishTemplate().node_info_list(node),remarks,'流程类型' + randomstring,0,[],[])
        return data

    def process_instance_data(self,randomstring):
        params = {
            "id": "",
            "processNodeList": [{
                "nodeName": "发起人",
                "approverType": 0,
                "approverRoleList": [],
                "approverUserList": [],
                "approvalType": 1
            }, {
                "nodeName": "节点名称",
                "approverType": 1,
                "approverRoleList": [],
                "approverUserList": [{
                    "userName": LoginConfig["user"],
                    "realName": "徐莘伟"
                }],
                "approvalType": 1
            }],
            "remark": "",
            "sponsorRoleList": [],
            "sponsorType": 0,
            "sponsorUserList": [],
            "typeName": "生成实例用模板"+randomstring
        }
        return params

    def publish_template(self,*datas):
        # 发布流程模板
        for data in datas:
            publish_info = PublishTemplate().publish_template(data)
            # logging.warning(publish_info)
            assert_pass(publish_info)
            return publish_info.get('result')

    def delete_template(self,typeId):
        # 删除流程模板
        # logging.warning(DeleteTemplate().delete_template(DeleteTemplate().req_params(typeId)))
        assert_pass(DeleteTemplate().delete_template(typeId))

    def switch_status(self,typeId):
        # 切换流程模板状态
        # logging.warning(UpdateSwitchStatus().update_switch_status(typeId))
        assert_pass(UpdateSwitchStatus().update_switch_status(typeId))

    def list_template(self,typeName,typeId):
        # 列表查询流程模板
        listtemplateInfo = ListTemplate().list_template(ListTemplate().req_params(typeName))
        # logging.warning(listtemplateInfo)
        assert_pass(listtemplateInfo)
        assert listtemplateInfo.get('result').get('content')[0].get('id') == typeId

    def get_template_info(self,typeId):
        # 获取流程模板详情
        template_info = GetTemplateDetail().get_template_detail(typeId)
        # logging.warning(template_info)
        assert_pass(template_info)
        return template_info.get('result').get('typeName')

    def list_instance(self,proccessCode):
        # 列表查询流程实例
        instanceInfo = ListInstace().list_instance(ListInstace().req_params(proccessCode,'',1))
        logging.warning(instanceInfo)
        assert_pass(instanceInfo)
        return len(instanceInfo.get('result').get('content'))

    def delete_instance(self,processCode):
        # 删除流程实例
        # logging.warning(DeleteInstance().delete_instance(DeleteInstance().req_params(processCode)))
        assert_pass(DeleteInstance().delete_instance(processCode))

    def get_instance_record(self,processCode):
        # 获取流程审批记录
        # logging.warning(GetInstanceRecord().get_instance_record(processCode))
        record_info = GetInstanceRecord().get_instance_record(processCode)
        assert_pass(record_info)
        return record_info.get('result')[-1].get('assignee')

    def get_process_type_name(self):
        # 获取不重复的流程模板名称
        # logging.warning(GetProcessTypeName().get_process_type_name())
        assert_pass(GetProcessTypeName().get_process_type_name())

    def get_processCode(self,typeName):
        # 根据流程模板名称获取流程编号
        return find_item(ListInstace().list_instance(ListInstace().certain_params()).get('result').get('content'),
                         'processTemplate', typeName).get('processCode')

    def get_initial_detp(self):
        # 获取初始化项目部id
        return find_item(GetNodes().get_nodes().get('result'),'name','初始化项目部').get('id')

    def instance_data(self,approvalTypeId,approvalTypeName,deptId):
        # 创建实例内容
        return CreateInstance().certain_params(approvalTypeId,approvalTypeName,deptId)

    def create_instance(self,data):
        # 创建流程实例
        instaceInfo = CreateInstance().create_instance(data)
        # logging.warning(instaceInfo)
        assert_pass(instaceInfo)
        return instaceInfo

    def submit_task(self,formTaskId):
        # 审批通过
        # logging.warning(SubmitTask().submit_task(formTaskId))
        assert_pass(SubmitTask().submit_task(formTaskId))

    def get_newInstance_processCode(self,randomstring):
        # 创建流程实例并返回流程实例的流程编号
        templateId = self.publish_template(self.process_instance_data(randomstring))
        try:
            PressCode = FindInstanceInfo().find_instance_info(self.create_instance(
                self.instance_data(templateId, self.get_template_info(templateId), self.get_initial_detp())).get(
                'result')).get('result').get('serialNum')
            self.delete_template(templateId)
            return PressCode
        except:
            self.delete_template(templateId)


    def process_instance_transfer(self,processCode,fromUser,toUser):
        # 流程转发
        # logging.warning(ProcessInstanceTransfer().process_instance_transfer(processCode,'bv-api-test','xiong1'))
        assert_pass(ProcessInstanceTransfer().process_instance_transfer(processCode,fromUser,toUser))

    def process_jump(self):
        assert_pass(ProcessJump().jump())

class TestIntergratedInterface(SingleWebservice):

    def test_process_template(self,make_random_str):
        # 流程类型
        randomstring = make_random_str
        templateId = self.publish_template(self.process_data(randomstring))
        templateName = self.get_template_info(templateId)
        self.switch_status(templateId)
        self.list_template(templateName,templateId)
        self.delete_template(templateId)


    def test_process_instance_management(self,make_random_str):
        # 流程数据
        randomstring = make_random_str
        self.get_process_type_name()
        processCode = self.get_newInstance_processCode(randomstring)
        self.list_instance(processCode)
        assignee = self.get_instance_record(processCode)
        self.process_instance_transfer(processCode,assignee,'xushenweitest')
        self.delete_instance(processCode)
        self.process_jump()


if __name__ == '__main__':
    pytest.main(['test_ProcessController.py'])
    # pass