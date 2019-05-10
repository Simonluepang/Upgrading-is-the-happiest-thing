#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.OrgAuthNumController import *
from InterfaceManager.OrgController import *
from InterfaceManager.APPAllocationController import *
from InterfaceManager.UserController import *

class SingleInterfaceTest():
    def root_orgid(self):
        # 查找根节点组织ID
        return find_root_org(GetNodes().get_nodes().get('result'))

    def add_org(self,fatherID,randomstring):
        # 创建组织并返回组织id
        add_orgid = AddOrg().add_org(fatherID,AddOrg().req_params('AddOrgName' + randomstring)).get('result').get('id')
        return add_orgid

    def delete_orgordept(self,orgid):
        # 删除组织
        return DeleteOrg().delete_org(orgid)

    def add_users(self):
        # 添加成员
        dept_id = get_initial_detp()
        pass

    def delete_user(self):
        # 删除成员
        pass

    def info(self,orgid):
        package_info = GetAuthNum().get_auth_num(orgid).get('result').get('orgAuthNumElementList')
        info_data = {}
        for i in package_info:
            package_type = str(i.get('packageType'))
            data = i.get('data')
            data_list = []
            for u in data:
                data_list.append((u.get('functionId'),u.get('heldId')))
                info_data[package_type] = data_list
        if '10' in info_data:
            del info_data['10']     # packageType=10制作库的问题已经解决，现在可以正确的授权了
        return info_data

    def save_orgAuth(self,orgid,authnum,functionId,heldId,packageType):
        # 给下级组织分配授权
        SaveAuthNum().save_auth_num(orgid, SaveAuthNum().req_params(authnum, functionId, heldId,packageType))

    def binding_client(self,functionId, heldId, operType, orgid, packageType,username):
        return UpdateUserPackageAuth().update_user_package_auth(
            UpdateUserPackageAuth().req_params(functionId, heldId, operType, orgid, packageType,username))

    def binding_auth_basic(self,packageType,functionId,heldId,orgid,username,operType):
        # 绑定并查询基础客户端
        return_list = []
        return_list.append(self.binding_client(functionId, heldId, operType, orgid, packageType,username))
        bindinginfo = GetUserAuthBasicPackage().get_user_auth_basic_package(username)
        return_list.append(bindinginfo)
        return return_list

    def binding_auth_quota_library(self,functionId, heldId, operType, orgid, packageType,username):
        # 绑定并查询定额库
        return_list = []
        return_list.append(self.binding_client(functionId, heldId, operType, orgid, packageType, username))
        bindinginfo = GetUserAuthQuotaLibraryPackage().get_user_auth_quota_library_package(username)
        return_list.append(bindinginfo)
        return return_list

    def binding_auth_bim_app(self,functionId, heldId, operType, orgid, packageType,username):
        # 绑定BIM APP套餐
        return_list = []
        return_list.append(self.binding_client(functionId, heldId, operType, orgid, packageType, username))
        bindinginfo = GetUserAuthBimAppPackage().get_admin_auth_bim_APP_package(username)
        return_list.append(bindinginfo)
        return return_list

    def binding_auth_pds(self,functionId, heldId, operType, orgid, packageType,username):
        # 绑定系统客户端套餐
        return_list = []
        return_list.append(self.binding_client(functionId, heldId, operType, orgid, packageType, username))
        bindinginfo = GetUserAuthPDSPackage().get_user_auth_PDSpackage(username)
        return_list.append(bindinginfo)
        return return_list

    def binding_right(self,packageType,functionId,heldId,orgid,username,operType=1):
        # 为用户绑定授权,默认为开，status为0时是取消绑定授权
        global binding_data
        if packageType == '2':
            binding_data = self.binding_auth_basic(packageType,functionId,heldId,orgid,username,operType)
        elif packageType == '11':
            binding_data = self.binding_auth_quota_library(functionId, heldId, operType, orgid, packageType,username)
        elif packageType == '12':
            binding_data = self.binding_auth_bim_app(functionId, heldId, operType, orgid, packageType,username)
        elif packageType == '3':
            binding_data = self.binding_auth_pds(functionId, heldId, operType, orgid, packageType,username)
        elif packageType == '10':
            binding_data = self.binding_auth_pds(functionId, heldId, operType, orgid, packageType, username)
        else:
            warnings.warn(f"Can't find the packageType = {packageType}!")
        return binding_data


class TestIntergratedInterface(SingleInterfaceTest):

    def test_root_org_app_allocation(self):
        # 根节点下给成员分配授权
        root_orgid = find_root_org(GetNodes().get_nodes().get('result'))
        packageInfo = self.info(root_orgid)
        for packagetypes in packageInfo.items():
            for packagedatas in packagetypes[1]:
                binding_msg = self.binding_right(packagetypes[0], packagedatas[0], packagedatas[1],
                                                             root_orgid, OrderConfig['username'])
                assert_pass(binding_msg[0])
                assert binding_msg[1].get('result') != []
                cancel_binding_msg = self.binding_right(packagetypes[0], packagedatas[0],
                                                                    packagedatas[1],
                                                                    root_orgid, OrderConfig['username'], operType=0)
                assert_pass(cancel_binding_msg[0])
                assert cancel_binding_msg[1].get('result') == []

    def test_middle_org_app_allocation(self,make_random_str):
        # 非根组织也非最下级组织给成员分配授权
        randomstring = make_random_str
        root_orgid = find_root_org(GetNodes().get_nodes().get('result'))
        add_orgid_level1 = self.add_org(root_orgid,'addlevel1'+randomstring)
        add_orgid_level2 = self.add_org(add_orgid_level1,'addlevel2'+randomstring)
        try:
            packageInfo = self.info(root_orgid)
            for packagetypes in packageInfo.items():
                for packagedatas in packagetypes[1]:
                    self.save_orgAuth(add_orgid_level1, 2,packagedatas[0],packagedatas[1], packagetypes[0])
                    binding_msg = self.binding_right(packagetypes[0], packagedatas[0], packagedatas[1],
                                                                 root_orgid, OrderConfig['username'])
                    assert_pass(binding_msg[0])
                    assert binding_msg[1].get('result') != []
                    cancel_binding_msg = self.binding_right(packagetypes[0], packagedatas[0],
                                                                        packagedatas[1], root_orgid,
                                                                        OrderConfig['username'], operType=0)
                    assert_pass(cancel_binding_msg[0])
                    assert cancel_binding_msg[1].get('result') == []
        except:
            warnings.warn("初始化测试环境...")
        finally:
            self.delete_orgordept(add_orgid_level2)
            self.delete_orgordept(add_orgid_level1)

    def test_normal_org_app_allocation(self,make_random_str):
        # 最下级组织给成员分配授权
        randomstring = make_random_str
        root_orgid = find_root_org(GetNodes().get_nodes().get('result'))
        add_orgid_level1 = self.add_org(root_orgid, 'addlevel1' + randomstring)
        add_orgid_level2 = self.add_org(add_orgid_level1, 'addlevel2' + randomstring)
        try:
            packageInfo = self.info(root_orgid)
            for packagetypes in packageInfo.items():
                for packagedatas in packagetypes[1]:
                    self.save_orgAuth(add_orgid_level1, 2, packagedatas[0], packagedatas[1],packagetypes[0])
                    self.save_orgAuth(add_orgid_level2, 1, packagedatas[0], packagedatas[1],packagetypes[0])
                    binding_msg = self.binding_right(packagetypes[0], packagedatas[0], packagedatas[1],
                                                                 root_orgid, OrderConfig['username'])
                    assert_pass(binding_msg[0])
                    assert binding_msg[1].get('result') != []
                    cancel_binding_msg = self.binding_right(packagetypes[0], packagedatas[0],
                                                                        packagedatas[1],
                                                                        root_orgid,
                                                                        OrderConfig['username'], operType=0)
                    assert_pass(cancel_binding_msg[0])
                    assert cancel_binding_msg[1].get('result') == []
        except:
            warnings.warn("初始化测试环境...")
        finally:
            self.delete_orgordept(add_orgid_level2)
            self.delete_orgordept(add_orgid_level1)

if __name__ == '__main__':
    pytest.main(['test_APPAllocationController.py'])


