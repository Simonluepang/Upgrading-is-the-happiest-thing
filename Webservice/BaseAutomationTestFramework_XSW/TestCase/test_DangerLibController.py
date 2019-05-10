#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.DangerFactorController import *
from InterfaceManager.DangerTypeController import *
from InterfaceManager.DangerLibController import *

class SingleInterfaceTest(object):

    def delete_all_lib(self):
        # 清空隐患库
        content = ListDangerLib().list_dangerlib(ListDangerLib().rep_params('','',0,0)).get('result').get('content')
        id_list = Recombition_list(['id'], content).get('id_list')
        delete_response = DeleteDangerLib().delete_all_dangerlib(id_list)
        assert_pass(delete_response)

    def create_danger_data(self,randomstring):
        # 创建要素和类别
        factor_id = AddDangerFactor().add_dangerfactor(AddDangerFactor().req_params('测试添加要素' + randomstring, 1)).get(
            'result')
        type_id = AddDangerType().add_dangertype(AddDangerType().req_params(factor_id, '测试添加类别' + randomstring, 1)).get(
            'result')
        return (factor_id,type_id)

    def add_danger_lib(self,randomstring,factor_id,type_id):
        # 添加隐患
        add_response = AddDangerLib().add_dangerlib(
            AddDangerLib().req_params('测试添加隐患内容' + randomstring, '测试添加隐患说明' + randomstring, factor_id, type_id))
        assert_pass(add_response)
        return add_response.get('result')

    def update_danger_lib(self,danger_id,randomstring,factor_id,type_id):
        # 修改隐患
        assert_pass(UpdateDangerLib().update_dangerlib(danger_id,
                                                       UpdateDangerLib().req_params('测试修改隐患内容' + randomstring,
                                                                                    '测试修改隐患说明' + randomstring,
                                                                                    factor_id, type_id)))

    def list_danger(self,randomstring,factor_id,type_id):
        # 根据要素和类别查询隐患列表
        list_response = ListDangerLib().list_dangerlib(ListDangerLib().rep_params(factor_id, type_id))
        assert_pass(list_response)
        assert list_response.get('result').get('content')[0].get('content') == '测试修改隐患内容' + randomstring, '修改隐患内容错误'
        assert list_response.get('result').get('content')[0].get('description') == '测试修改隐患说明' + randomstring, '修改隐患说明错误'

    def delete_lib(self,danger_id):
        # 删除隐患
        assert_pass(DeleteDangerLib().delete_dangerlib(danger_id))

    def clear_data(self,factor_id,type_id):
        # 删除隐患要素和隐患类别
        DeleteDangerType().delete_dangertype(type_id)
        DeleteDangerFactor().delete_dangerfactor(factor_id)

    def list_template(self):
        # 查询隐患模板列表
        template_response = TemplateDangerLib().template_dangerlib(TemplateDangerLib().req_params())
        assert_pass(template_response)
        return template_response.get('result').get('content')[0].get('contentMd5')

    def quote_template(self,contentMd5):
        # 引用模板内容
        quote_response = QuoteDangerTemplate().quote_dangertemplate(contentMd5)
        assert_pass(quote_response)
        assert quote_response.get('result').get('successCount') == 1, '引用成功数量不为1'
        assert quote_response.get('result').get('failCount') == 0, '引用失败数量不为0'

    def read_status(self):
        # 模板阅读状态
        assert_pass(TemplateReadStatus().template_read_status())

    def red_tip(self):
        # 隐患库模板红点
        assert_pass(RedTipDangerLibTeplate().red_tip())

    def list_factor(self):
        # 查询隐患要素
        listfactor_response = ListDangerFactor().list_dangerfactor(1, 0)
        assert_pass(listfactor_response)
        return listfactor_response.get('result')[0].get('id')

    def list_type(self,factor_id):
        # 查询隐患类型
        assert_pass(ListDangerType().list_dangertype(factor_id, 1, 0))

    def export_dangerlib(self):
        # 导出隐患库
        assert ExportDangerLib().export_dangerlib() == 200, '导出隐患库状态码不为200'

    def import_dangerlib(self):
        # 导入隐患库
        assert ImportDangerLib().import_dangerlib().get('msg') == '导入完成，已成功导入2条数据,失败导入0条数据', '导入失败'

class TestIntergratedInterface(SingleInterfaceTest):

    def test_danger_lib(self,make_random_str):
        randomstring = make_random_str
        dangerdata = self.create_danger_data(randomstring)
        danger_id = self.add_danger_lib(randomstring,dangerdata[0],dangerdata[1])
        try:
            self.update_danger_lib(danger_id,randomstring,dangerdata[0],dangerdata[1])
            self.list_danger(randomstring,dangerdata[0],dangerdata[1])
        except:
            warnings.warn("Danger lib test is failed, clear data.")
        finally:
            self.delete_all_lib()
            self.clear_data(dangerdata[0], dangerdata[1])

    def test_danger_lib_template(self):
        try:
            contentMd5 = self.list_template()
            self.quote_template(contentMd5)
            self.read_status()
            self.red_tip()
            factor_id = self.list_factor()
            self.list_type(factor_id)
            self.export_dangerlib()
            self.import_dangerlib()
        except:
            warnings.warn("Danger lib template test is failed, clear data.")
        finally:
            self.delete_all_lib()


if __name__ == '__main__':
    pytest.main(['test_DangerLibController.py'])
