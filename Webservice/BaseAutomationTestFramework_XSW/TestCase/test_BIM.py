#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.OrgController import *
from InterfaceManager.BimParamRest import *
from InterfaceManager.BimRecycleRest import *
from InterfaceManager.BimRest import *

class SingleInterfaceTest():

    def add_org(self,randomstring):
        # 添加组织
        add_orgid = AddOrg().add_org(find_root_org(GetNodes().get_nodes().get('result')),
                                     AddOrg().req_params('AddOrgName' + randomstring)).get('result').get('id')
        return add_orgid

    def add_dept(self,orgid,randomstring):
        # 添加项目部
        add_detpid = AddDept().add_dept(orgid, AddDept().req_params('AddDeptName' + randomstring)).get('result').get(
            'id')
        return add_detpid

    def delete_orgordept(self,orgid):
        # 删除组织或者项目部
        return DeleteOrg().delete_org(orgid)

    def create_proj(self,deptId,randomstring):
        # 创建工程
        create_proj_resp = CreateProject().create_project(CreateProject().req_params(deptId, "测试添加工程" + randomstring))
        assert_pass(create_proj_resp)

    def get_proj(self,randomstring):
        # 获取工程id
        get_proj_resp = GetProject().get_project(GetProject().req_params("测试添加工程" + randomstring))
        assert_pass(get_proj_resp)
        return get_proj_resp.get('result').get('content')[0].get('projId')

    def update_proj_name(self,proj_id,randomstring):
        # 更新工程名称
        update_proj_name_resp = UpdateProjName().update_projectname(
            UpdateProjName().req_params(proj_id, "测试修改工程" + randomstring))
        assert update_proj_name_resp.get('code') == 1006
        assert update_proj_name_resp.get('msg') == '图纸工程不能修改名称。'

    def update_proj_shortinfo(self,proj_id,randomstring):
        # 更新工程信息
        update_proj_resp = UpdateProjShortInfo().update_projectshortinfo(
            UpdateProjShortInfo().req_params(proj_id, "测试修改工程" + randomstring))
        assert_pass(update_proj_resp)

    def get_used_name(self,proj_id):
        # 获取工程曾用名
        get_used_name_resp = GetProjUsedName().get_projusedname(proj_id)
        assert_pass(get_used_name_resp)

    def extract_proj(self,proj_id):
        # 抽取工程
        extractproj_resp = ExtractProject().extract_project(proj_id, 1)
        assert_pass(extractproj_resp)

    def get_extract_proj_info(self):
        # 抽取失败时获取失败详情信息
        getextractinfo_resp = GetProjExtractInfo().get_projextractinfo(1, 0000)
        assert_pass(getextractinfo_resp)

    def delete_to_recycle(self,proj_id):
        # 标记删除工程
        # delete_proj_to_recycle_resp = DeleteProjectToRecycle().delete_projecttorecycle(DeleteProjectToRecycle().req_params(proj_id))
        delete_proj_to_recycle_resp = DeleteProjectToRecycle().delete_projecttorecycle(proj_id)
        assert_pass(delete_proj_to_recycle_resp)

    def delete_porj(self,proj_id):
        # 回收站中删除工程
        delete_proj_resp = DeleteProject().delete_project(DeleteProject().req_params(proj_id))
        assert_pass(delete_proj_resp)

    def get_proj_type(self):
        # 获取企业下的所有专业类型列表
        getprojtype_resp = GetProjType().GetProjTypeget_projtype(False, 1)
        assert_pass(getprojtype_resp)
        assert len(getprojtype_resp.get('result')) != 0

    def get_major(self):
        # 获取企业能创建的专业类型
        getmajor_resp = GetMajorsByCreate().get_majorsbycreate()
        assert_pass(getmajor_resp)
        assert len(getmajor_resp.get('result')) != 0

    def get_proj_genre(self):
        # 获取企业下的所有BIM属性列表
        getprojgenre_resp = GetProjGenre().get_projgenre(False, 1)
        assert_pass(getprojgenre_resp)
        assert len(getprojgenre_resp.get('result')) != 0

    def get_proj_user_auth_info(self,deptId):
        # 创建/修改工程时获取授权用户信息列表
        getprojauthuserinfo_resp = GetProjAuthUserInfos().get_projectauthuserinfos(
            GetProjAuthUserInfos().req_params(deptId, 1, 1111))
        assert_pass(getprojauthuserinfo_resp)
        assert len(getprojauthuserinfo_resp.get('result')) != 0

class TestIntergratedInterface(SingleInterfaceTest):
    def test_BIM(self,make_random_str):
        '''BIM工程相关以及BIM工程条件相关集成接口'''
        randomstring = make_random_str
        deptId = find_item(GetNodes().get_nodes().get('result'),'name','初始化项目部').get('id')
        self.create_proj(deptId,randomstring)
        proj_id = self.get_proj(randomstring)
        self.update_proj_name(proj_id,randomstring)
        self.update_proj_shortinfo(proj_id,randomstring)
        self.get_used_name(proj_id)
        self.extract_proj(proj_id)
        self.get_extract_proj_info()
        self.delete_to_recycle(proj_id)
        self.delete_porj(proj_id)
        self.get_proj_type()
        self.get_major()
        self.get_proj_genre()
        self.get_proj_user_auth_info(deptId)

if __name__ == '__main__':
    pytest.main(['test_BIM.py'])
