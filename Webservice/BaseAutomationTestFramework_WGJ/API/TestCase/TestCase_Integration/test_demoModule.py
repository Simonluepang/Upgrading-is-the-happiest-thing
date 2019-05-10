#coding=utf-8
import sys

sys.path.append("..")
from API.swagger.demo import *
from API.swagger.fileUpload_controller import *
from API.swagger.projectHisotry_controller import *
from API.Public.AssertFunction import *
from API.swagger.collaboration_controller import *
from API.swagger.project_dashboard import *


class Test_demo_Module():
    def test_1(self):
        demo_module().demofunction()

    def test_assertcommonfunction(self):
        result = {'check':'this is a test demo!'}
        result_list = {'checkList':['this is a test demo!','check list',123333]}
        result_null = {'checknull':''}
        assert_commonFunction(result,exceptedValue='this is a test demo!',key='check')
        assert_commonFunction(result,exceptedValue='this is a demo!',key='check')
        # assert_commonFunction(result_null,exceptedValue='this is a demo!',key='check')

    def test_assertcommonfunction_1(self):
        result_null = {'checknull':''}
        assert_commonFunction(result_null,exceptedValue='this is a demo!',key='checknull')

    def test_assertcommonfunction_2(self):
        result = {'check':'this is a test demo!'}
        result_list = {'checkList':['this is a test demo!','check list',123333]}
        result_null = {'checknull':''}
        assert_commonFunction(result_list,exceptedValue=['check list'],key='checkList')
        assert_commonFunction(result_list,exceptedValue=['this is a test demo!','check list',123333],key='checkList')
        assert_commonFunction(result_list,exceptedValue=['this is a demo!'],key='checkList')

    def test_assertcommonfunction_3(self):
        result_list = {'checkList':['this is a test demo!','check list',123333]}
        for value in ['this is a test demo!','check list',123333,'sssss']:
            assert_commonFunction(result_list,exceptedValue=[value],key='checkList')

if __name__ == '__main__':
    Test_demo_Module().test_assertcommonfunction_1()