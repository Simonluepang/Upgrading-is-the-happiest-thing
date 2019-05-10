#coding=utf-8
import sys
import inspect

sys.path.append('..')
from API.Public.CommonFunction import *
from API.Public.AssertFunction import *

globalParams=getGlobalParams()

class fileUpload_controller:

    @allure.step('获取上传图片')
    def pictureUpload(self,file,epid=globalParams['epid'],**kwargs):
        url =URL +'/rest/fileupload/picture/upload/'+str(epid)
        result = response(WebRequests().post_file(url,file,Headers().headers()))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        fileUpload_assert().pictureUpload(result)
        return result
