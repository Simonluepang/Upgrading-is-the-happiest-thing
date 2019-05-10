#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.OrgController import *

class TestOrgController(object):

    def add(self):
        pass

    def test_Intergrated_interface(self):
        randomstring = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        # 获取根节点id
        orgresp = GetNodes().get_nodes()
        assert_pass(orgresp)
        root_orgid = find_root_org(orgresp.get('result'))
        # 添加组织
        addorg = AddOrg().add_org(root_orgid, AddOrg().req_params('AddOrgName' + randomstring))
        assert_pass(addorg)
        assert addorg.get('result').get('name') == 'AddOrgName' + randomstring, '添加组织名称错误'
        add_orgid = addorg.get('result').get('id')
        # 添加项目部
        adddetp = AddDept().add_dept(add_orgid, AddDept().req_params('AddDeptName' + randomstring))
        assert_pass(adddetp)
        assert (adddetp.get('result').get('parentId'), adddetp.get('result').get('name')) == (
            add_orgid, 'AddDeptName' + randomstring), '添加项目部信息错误'
        add_detpid = adddetp.get('result').get('id')
        # 编辑项目部信息
        updatedetp = UpdateDepts().update_depts(add_detpid, UpdateDepts().req_params('UpdateDeptName' + randomstring))
        assert_pass(updatedetp)
        assert (updatedetp.get('result').get('parentId'), updatedetp.get('result').get('name')) == (
            add_orgid, 'UpdateDeptName' + randomstring), '编辑项目部信息错误'
        # 编辑组织信息
        updateorg = UpdateOrg().update_org(add_orgid, UpdateOrg().req_params('UpdateOrgName' + randomstring))
        assert_pass(updateorg)
        assert (updateorg.get('result').get('parentId'), updateorg.get('result').get('name')) == (
            root_orgid, 'UpdateOrgName' + randomstring), '编辑组织信息错误'
        # 查询组织机构信息
        for i in (add_orgid, add_detpid):
            getorg = GetOrg().get_org(i)
            assert_pass(getorg)
            assert getorg.get('result').get('org').get('id') == i, '组织机构信息错误'
        # 检查机构名称是否已存在
        for o in (('UpdateDeptName' + randomstring,1), ('UpdateOrgName' + randomstring,0)):
            check_resp = CheckNodesName().check_nodes_name(CheckNodesName().req_params('', o[0],o[1]))
            assert_pass(check_resp)
            assert check_resp.get('result').get('exists') == True, '组织机构名称不存在'
        # 删除机构
        assert_pass(DeleteOrg().delete_org(add_detpid))
        assert_pass(DeleteOrg().delete_org(add_orgid))




if __name__ == '__main__':
    pytest.main(['test_OrgController.py'])