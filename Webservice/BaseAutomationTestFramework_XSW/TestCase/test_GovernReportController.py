#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.GovernReportController import *
from InterfaceManager.RoleController import *

class GovernReportController(object):
    def test_Intergrated_interface(self):
        '''原Govern报表订阅集成接口'''
        roleid = FindRoles().find_roles().get('result')[0].get('roleId')
        # 数据类型列表下拉框数据
        getdata_resp = GetDataType().get_datatype()
        assert_pass(getdata_resp)
        assert len(getdata_resp.get('result')) == 2
        # 组织节点列表下拉框数据
        getnode_resp = GetOrgNodes().get_orgnodes()
        assert_pass(getnode_resp)
        # 查询对应角色的报表模板权限,返回有权限的报表id列表
        get_reportlist_resp = GetReportRoleList().get_reportrolelist(roleid)
        assert_pass(get_reportlist_resp)
        # 添加角色对应的报表权限
        add_resp = AddReportPermissions().add_reportpermissions(AddReportPermissions().req_params('', 1, roleid))
        assert_pass(add_resp)
        # 获取报表列表数据
        list_resp = GetReportList().get_reportlist(GetReportList().req_params(1, 1))
        assert_pass(list_resp)
        # 删除角色对应的报表权限
        delete_resp = DeleteReportPermissions().del_reportpermissions(DeleteReportPermissions().req_params('', 1, roleid))
        assert_pass(delete_resp)


if __name__ == '__main__':
    pytest.main(['test_GovernReportController.py'])
