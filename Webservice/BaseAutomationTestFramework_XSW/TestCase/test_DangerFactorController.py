#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.DangerFactorController import *

class SingleInterfaceTest(object):

    def add_factor(self,randomstring):
        # 添加隐患要素
        add_response = AddDangerFactor().add_dangerfactor(AddDangerFactor().req_params('测试添加要素' + randomstring, 0))
        assert_pass(add_response)
        return add_response.get('result')

    def update_factor(self,add_id,randomstring):
        # 更新隐患要素
        assert_pass(UpdateDangerFactor().update_dangerfactor(add_id, UpdateDangerFactor().req_params(
            '测试修改要素' + randomstring, 1)))

    def list_factor(self,randomstring):
        # 查询隐患要素列表
        list_response = ListDangerFactor().list_dangerfactor(ListDangerFactor().req_params(''))
        assert_pass(list_response)
        assert list_response.get('result').get('content')[2].get('name') == '测试修改要素' + randomstring, '修改隐患要素名称错误'
        assert list_response.get('result').get('content')[2].get('status') == 1, '修改隐患要素可见状态错误'

    def list_allow(self):
        # 查询已启用的隐患要素列表
        listallow_response = ListAllowDangerFactor().list_allowdangerfactor()
        assert_pass(listallow_response)
        for i in listallow_response.get('result'):
            assert i.get('status') == 1, '该隐患要素不可见'

    def delete_factor(self,add_id):
        # 删除隐患要素
        assert_pass(DeleteDangerFactor().delete_dangerfactor(add_id))

    def verify_delete(self):
        # 验证是否删除成功
        list_response_delete = ListDangerFactor().list_dangerfactor(ListDangerFactor().req_params(''))
        assert_pass(list_response_delete)
        assert len(list_response_delete.get('result').get('content')) == 2, '隐患要素未回归初始化'

class TestIntegratedInterface(SingleInterfaceTest):

    def test_danger_factor_controller(self,make_random_str):
        '''隐患要素集成接口'''
        randomstring = make_random_str
        add_id = self.add_factor(randomstring)
        self.update_factor(add_id,randomstring)
        self.list_factor(randomstring)
        self.list_allow()
        self.delete_factor(add_id)
        self.verify_delete()



if __name__ == "__main__":
    pytest.main(['test_DangerFactorController.py'])

