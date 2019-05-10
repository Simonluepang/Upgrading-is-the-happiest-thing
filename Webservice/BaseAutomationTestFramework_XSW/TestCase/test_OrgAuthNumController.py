#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.OrgController import *
from InterfaceManager.OrgAuthNumController import *

class Initialization():

    def add_org(self,fatherID,randomstring):
        add_orgid = AddOrg().add_org(fatherID,
                                     AddOrg().req_params('AddOrgName' + randomstring)).get('result').get('id')
        return add_orgid

    def delete_orgordept(self,orgid):
        return DeleteOrg().delete_org(orgid)

    def find_info(self,orgid):
        return find_item(
            find_item(GetAuthNum().get_auth_num(orgid).get('result').get('orgAuthNumElementList'), 'packageType',
                      OrderConfig['packageType']).get('data'), 'functionName', OrderConfig['functionName'])


class TestOrgAuthNumController(Initialization):

    def test_Intergrated_interface(self):
        randomstring = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        root_orgid = find_root_org(GetNodes().get_nodes().get('result'))
        add_orgid = self.add_org(root_orgid,randomstring)
        try:
            functionId = self.find_info(root_orgid).get('functionId')
            heldId = self.find_info(root_orgid).get('heldId')
            # 获取组织授权数详情
            assert_pass(GetAuthNum().get_auth_num(add_orgid))
            # 保存组织授权
            assert_pass(SaveAuthNum().save_auth_num(add_orgid, SaveAuthNum().req_params(10, functionId, heldId,
                                                                                        OrderConfig['packageType'])))
            # 获取用户可用授权
            assert_pass(GetUserOrgAuthNum().get_user_org_auth_num(LoginConfig["user"],OrderConfig['packageType'],functionId,heldId))
            # 回收组织授权
            assert_pass(RecycleAuthNum().recycle_auth_num(add_orgid,add_orgid))
            # 删除新建组织
            assert_pass(self.delete_orgordept(add_orgid))
        except:
            warnings.warn("出了一些小差错，现在开始进行初始化组织节点操作...")
            self.delete_orgordept(add_orgid)



if __name__ == '__main__':
    pytest.main(['test_OrgAuthNumController.py'])

