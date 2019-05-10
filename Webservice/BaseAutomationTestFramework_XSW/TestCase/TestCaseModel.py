#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.OrgController import *
import random,string,pytest,logging
logging.basicConfig(level=logging.INFO)

def assert_pass(request):
    assert request.get('code') == 200, '状态码不为200'
    assert request.get('msg') == 'success', '状态信息不为success'

def find_item(list,findname,checkname):
    # 在列表中寻找匹配并返回值
    for i in list:
        if i.get(findname) == checkname:
            return i
        else:
            pass

def find_root_org(orglist):
    # 查找根节点id
    for i in orglist:
        if i.get('id') == i.get('parentId'):
            return i.get('id')
        else:
            pass
def get_initial_detp():
    # 获取初始化项目部id
    return find_item(GetNodes().get_nodes().get('result'),'name','初始化项目部').get('id')

def Recombition_list(keys,data_list):
    '''
    :将list根据key重组
    :param keys:["epid","orgId"]
    :param data_list:
         [{
            "epid": 1,
            "orgId": "7c01a75941549a705cf7275e41b21f0b"

        }, {
            "epid": 713,
            "orgId": "8c01a75941549a705cf7275e41b21f0d"
        }]
    :return:
            result = {'epid_list': [1, 713], 'orgId_list': ['7c01a75941549a705cf7275e41b21f0b', '8c01a75941549a705cf7275e41b21f0d']}
    '''

    result = {}

    for key in keys:
        result[key+"_list"] = []

    for data in data_list:
        for key in keys:
            result[key +"_list"].append(data.get(key))
    return result

@pytest.fixture()
def make_random_str():
    randomstring = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    yield randomstring

if __name__ == '__main__':
    pytest.main()