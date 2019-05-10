#coding=utf-8
import sys
import inspect
sys.path.append('..')
from API.Public.CommonFunction import *
from API.Public.AssertFunction import *

globalParams=getGlobalParams()

class photoAlbum_controller:
    @allure.step('获取相册')
    def getAlbumList(self,epid=globalParams['epid'],deptid=globalParams['deptid'],token=globalParams['token'],**kwargs):
        url =URL +'/rest/projphotoalbum/photoAlbum/list/'+str(epid)+'/'+deptid
        result =response(WebRequests().get(url,json.dumps(kwargs),Headers().headers_token(token)))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        return result

    @allure.step('添加相册')
    def addAlbum(self,epid=globalParams['epid'],deptid=globalParams['deptid'],token=globalParams['token'],**kwargs):
        param = {'epId':epid,'deptId':deptid,'photoAlbumName':kwargs['photoAlbumName']}
        url =URL +'/rest/projphotoalbum/photoAlbum/add'
        result =response(WebRequests().post(url,json.dumps(param),Headers().headers_token_aplication_json(token)))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        return  result

    @allure.step('重命名相册')
    def renameAlbum(self,epid=globalParams['epid'],deptid=globalParams['deptid'],token=globalParams['token'],**kwargs):
        param = {'epid':epid,'photoAlbumId':kwargs['photoAlbumId'],'deptId':deptid,'photoAlbumName':kwargs['photoAlbumName']}
        url =URL +'/rest/projphotoalbum/photoAlbum/update/rename'
        result =response(WebRequests().post(url,json.dumps(param),Headers().headers_token_aplication_json(token)))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        return  result

    @allure.step('获取相片')
    def getPhotoList(self,epid=globalParams['epid'],token=globalParams['token'],**kwargs):
        param = {'albumId':kwargs['albumId'],'epid':epid,'keyword':'','page':1,'pageSize':100}
        url =URL +'/rest/projphotoalbum/customize/picture/list'
        result = response(WebRequests().post(url,json.dumps(param),Headers().headers_token_aplication_json(token)))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        return result

    @allure.step('添加相片')
    def addPhoto(self,epid=globalParams['epid'],token=globalParams['token'],**kwargs):
        param ={
            'albumId': kwargs['albumId'],
            'epId': epid,
            'pictureUploadInfos':[
                    {
                        'fileId':kwargs['fileId'],
                        'origin':1,
                        'pictureName':kwargs['pictureName'],
                        'thumbFileId': kwargs['thumbFileId']
                    }
            ]
        }
        url =URL +'/rest/projphotoalbum/picture/add/upload'
        result =response(WebRequests().post(url,json.dumps(param),Headers().headers_token_aplication_json(token)))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        return result

    @allure.step('旋转相片')
    def rotatePhoto(self,epid=globalParams['epid'],token=globalParams['token'],**kwargs):
        param ={
            'albumId':kwargs['albumId'],
            'epid': epid,
            'albumType':kwargs['albumType'],
            'fileId':kwargs['fileId'],
            'fileName':kwargs['fileName'],
            'pictureId':kwargs['pictureId'],
            'rotateType':kwargs['rotateType']
        }
        url =URL +'/rest/projphotoalbum/picture/update/rotate'
        result =response(WebRequests().post(url,json.dumps(param),Headers().headers_token_aplication_json(token)))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        return result

    @allure.step('重命名相片')
    def renamePhoto(self,epid=globalParams['epid'],token=globalParams['token'],**kwargs):
        param ={
            'albumId':kwargs['albumId'],
            'epid': epid,
            'photoAlbumType':kwargs['photoAlbumType'],
            'pictureId':kwargs['pictureId'],
            'pictureName':kwargs['pictureName']
        }
        url =URL +'/rest/projphotoalbum/picture/update/rename'
        result = response(WebRequests().post(url,json.dumps(param),Headers().headers_token_aplication_json(token)))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        return result

    @allure.step('删除相片')
    def deletePhoto(self,epid=globalParams['epid'],token=globalParams['token'],**kwargs):
        param ={
            'fileId':kwargs['fileId'],
            'epId': epid,
            'photoAlbumType':kwargs['photoAlbumType'],
            'pictureId':kwargs['pictureId'],
            'thumbFileId':kwargs['thumbFileId']
        }
        url =URL +'/rest/projphotoalbum/picture/delete'
        result = response(WebRequests().delete(url,param,Headers().headers_token_aplication_json(token)))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        return result

    @allure.step('删除相册')
    def deleteAlbum(self,epid=globalParams['epid'],token=globalParams['token'],**kwargs):
        url =URL +'/rest/projphotoalbum/photoAlbum/delete/'+str(epid)+'/'+kwargs['albumId']
        result = response(WebRequests().delete(url,kwargs['params'],Headers().headers_token_aplication_json(token)))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        return result