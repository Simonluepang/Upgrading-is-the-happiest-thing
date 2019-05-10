#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.GovernContractController import *

class SingleInterfaceTest(object):
    def builder_jump(self):
        # Builder302跳转
        jump_resp = BuilderJump().jump()
        assert_pass(jump_resp)
        assert jump_resp.get('result') == True

    def get_item(self):
        # 获取与合同清单相关联的项目
        find_resp = FindList().find_list(FindList().req_params(''))
        assert_pass(find_resp)
        return find_resp.get('result')[0].get('formatId')

    def get_list(self,formatId):
        # 分页查询合同清单
        get_proj_resp = GetProject().get_project(formatId)
        assert_pass(get_proj_resp)
        return get_proj_resp.get('result')[0].get('orgid')

    def update_item(self,formatId,orgid):
        # 更新与合同清单相关联的项目
        update_resp = UpdateProject().update_project(formatId, orgid)
        assert_pass(update_resp)
        assert update_resp.get('result') == True

class TestIntergratedInterface(SingleInterfaceTest):

    def test_govern_contract_controller(self):
        '''Govern合同清单管理集成接口'''
        self.builder_jump()
        formatId = self.get_item()
        orgid =self.get_list(formatId)
        self.update_item(formatId,orgid)



if __name__ == '__main__':
    pytest.main(['test_GovernContractController.py'])


