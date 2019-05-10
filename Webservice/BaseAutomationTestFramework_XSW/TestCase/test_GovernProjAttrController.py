#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.GovernProjAttrController import *

class SingleInterfaceTest(object):
    def get_list(self):
        # 获取工程列表
        get_attrs_resp = GetProjAttrs().get_projattrs()
        assert_pass(get_attrs_resp)
        assert len(get_attrs_resp.get('result')) == 8
        return get_attrs_resp.get('result')[0].get('id')

    def update_proj_attrs(self,get_id):
        # 修改工程性质
        update_resp = UpdateProjAttrs().update_projattrs(UpdateProjAttrs().req_params(get_id, 'ZB', '(ZB)中标合同价', '合同'))
        assert_pass(update_resp)

class TestGovernProjAttrController(SingleInterfaceTest):

    def test_Intergrated_interface(self):
        '''原Govern工程属性集成接口'''
        get_id = self.get_list()
        self.update_proj_attrs(get_id)

if __name__ == '__main__':
    pytest.main(['test_GovernProjAttrController.py'])


