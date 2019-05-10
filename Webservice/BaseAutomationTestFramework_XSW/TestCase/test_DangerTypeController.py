#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.DangerFactorController import *
from InterfaceManager.DangerTypeController import *

class SingleInterfaceTest(object):
    def create_danger_factor(self,randomstring):
        # 添加隐患要素
        return AddDangerFactor().add_dangerfactor(AddDangerFactor().req_params('测试添加要素' + randomstring, 1)).get(
            'result')

    def add_danger_type(self,factor_id,randomstring):
        # 添加隐患类别
        add_response = AddDangerType().add_dangertype(AddDangerType().req_params(factor_id, '测试添加类别' + randomstring, 0))
        assert_pass(add_response)
        return add_response.get('result')

    def edit_danger_type(self,type_id,factor_id,randomstring):
        # 修改隐患类别
        assert_pass(UpdateDangerType().update_dangertype(type_id, UpdateDangerType().req_params(factor_id,
                                                                                                '测试修改类别' + randomstring,
                                                                                                1)))

    def list_danger_type(self,randomstring):
        # 查询隐患类别列表
        list_response = ListDangerType().list_dangertype(ListDangerType().req_params('', ''))
        assert_pass(list_response)
        assert list_response.get('result').get('content')[-1].get('name') == '测试修改类别' + randomstring, '修改隐患类别名称错误'
        assert list_response.get('result').get('content')[-1].get('status') == 1, '修改隐患类别可见状态错误'

    def list_allow_type(self,factor_id):
        # 查询已启用的隐患类别列表
        listallow_response = ListAllowDangerType().list_allowdangertype(factor_id)
        assert_pass(listallow_response)
        for i in listallow_response.get('result'):
            assert i.get('status') == 1, '隐患类别可见状态错误'

    def delete_danger_type(self,type_id):
        # 删除隐患类别
        assert_pass(DeleteDangerType().delete_dangertype(type_id))

    def delete_danger_factor(self,factor_id):
        # 删除新增隐患要素
        DeleteDangerFactor().delete_dangerfactor(factor_id)


class TestIntergratedInterface(SingleInterfaceTest):

    def test_danger_type_controller(self,make_random_str):
        '''隐患类别集成接口'''
        randomstring = make_random_str
        factor_id = self.create_danger_factor(randomstring)
        try:
            type_id = self.add_danger_type(factor_id,randomstring)
            self.edit_danger_type(type_id,factor_id,randomstring)
            self.list_danger_type(randomstring)
            self.list_allow_type(factor_id)
            self.delete_danger_type(type_id)
        except:
            raise Exception
        finally:
            self.delete_danger_factor(factor_id)





if __name__ == "__main__":

    pytest.main(['test_DangerTypeController.py'])







