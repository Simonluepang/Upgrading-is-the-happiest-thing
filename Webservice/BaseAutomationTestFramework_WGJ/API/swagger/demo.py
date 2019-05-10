#coding=utf-8
import sys
import inspect

sys.path.append('..')
from API.Public.AssertFunction import *


class demo_module:
    def demofunction(self):
        result={'status_code':200,'msg':['success'],'responsetime':1}
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname,basetime=10)
        return result