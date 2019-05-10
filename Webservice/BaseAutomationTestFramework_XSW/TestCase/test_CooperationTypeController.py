#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.CooperationTypeController import *

class SingleInterfaceTest():

    def add_coo(self,randomstring):
        # 添加协作
        add_resp = AddCooperationType().add_cooperationtype(AddCooperationType().req_params('添加' + randomstring))
        assert_pass(add_resp)

    def get_add_id(self,randomstring):
        # 获取添加的协作id
        list_add_resp = ListAllCooperationType().list_allcooperationtype(
            ListAllCooperationType().req_params('添加' + randomstring))
        assert_pass(list_add_resp)
        return list_add_resp.get('result').get('result')[0].get('id')

    def update_coo(self,add_id,randomstring):
        # 修改协作类型
        update_resp = UpdateCooperationType().update_cooperationtype(
            UpdateCooperationType().req_params(add_id, '修改' + randomstring))
        assert_pass(update_resp)
        list_update_resp = ListAllCooperationType().list_allcooperationtype(
            ListAllCooperationType().req_params('修改' + randomstring))
        assert_pass(list_update_resp)
        assert list_update_resp.get('result').get('result')[0].get('name') == '修改' + randomstring
        assert list_update_resp.get('result').get('result')[0].get('isShow') == 1

    def list_shown(self):
        # 查询已显示的协作类型
        list_shown_resp = ListShownCooperationType().list_showncooperationtype()
        assert_pass(list_shown_resp)
        assert list_shown_resp.get('result')[-1].get('isShow') == 1

    def is_rev(self,add_id):
        # 查询协作类型是否有关联协作
        is_rev_resp = IsRelevanceCO().is_relevance_CO(add_id)
        assert_pass(is_rev_resp)
        assert is_rev_resp.get('result') == False

    def delete_coo(self,add_id):
        # 删除协作类型
        delete_resp = DeleteCooperationType().delete_cooperationtype(add_id)
        assert_pass(delete_resp)

class TestIntergratedInterface(SingleInterfaceTest):

    def test_cooperation_controller(self,make_random_str):
        '''协作类型集成接口'''
        randomstring = make_random_str
        self.add_coo(randomstring)
        add_id = self.get_add_id(randomstring)
        self.update_coo(add_id, randomstring)
        self.list_shown()
        self.is_rev(add_id)
        self.delete_coo(add_id)



if __name__ == '__main__':
    pytest.main(['test_CooperationTypeController.py'])