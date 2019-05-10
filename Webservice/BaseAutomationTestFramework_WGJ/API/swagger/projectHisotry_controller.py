#coding=utf-8
import sys
import inspect
from API.Public.AssertFunction import *

sys.path.append('..')
from API.Public.CommonFunction import *

globalParams=getGlobalParams()

class projectHisotry_controller:

    @allure.step('获取图片')
    def getPicture(self,deptid=globalParams['deptid'],token=globalParams['token'],**kwargs):
        url =URL +'/rest/document/picture/list/'+str(deptid)+'/'+str(kwargs['parentId'])
        result = response(WebRequests().get(url,kwargs,Headers().headers_token_aplication_json(token)))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        return result