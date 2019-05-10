#coding=utf-8
import sys
sys.path.append("..")
from API.swagger.fileUpload_controller import *
from API.swagger.projectHisotry_controller import *
from API.Public.AssertFunction import *
from API.swagger.collaboration_controller import *
from API.swagger.project_dashboard import *



@allure.feature('测试Myluban相册')
class Test_projphotoalbum_integration:

    @allure.story('完整流程')
    def testdemo(self,teardown_module):
        photoAlbum_controller().getAlbumList(epid=globalParams['epid'],deptid=globalParams['deptid'],token=globalParams['token'])
        photoAlbumName ='自动化脚本相册'+str(int(time.time()))
        result_add_photoAlbum = photoAlbum_controller().addAlbum(epid=globalParams['epid'],deptid=globalParams['deptid'],token=globalParams['token'],photoAlbumName=photoAlbumName)
        albumId = result_add_photoAlbum['data'][0]
        photoAlbum_controller().getAlbumList(epid=globalParams['epid'],deptid=globalParams['deptid'],token=globalParams['token'])
        photoAlbumRename ='脚本相册'+str(int(time.time()))
        photoAlbum_controller().renameAlbum(epid=globalParams['epid'],deptid=globalParams['deptid'],token=globalParams['token'],photoAlbumName=photoAlbumRename,photoAlbumId=albumId)
        photoAlbum_controller().getAlbumList(epid=globalParams['epid'],deptid=globalParams['deptid'],token=globalParams['token'])
        attachmentName = "test.jpg"
        filespath = root + os.sep + "Data" + os.sep + attachmentName
        files ={'file':(attachmentName,open(filespath,'rb'))}
        result_upload_picture = fileUpload_controller().pictureUpload(files,epid=globalParams['epid'])
        fileId_local,thumbFileId_local = result_upload_picture['data_fileId'][0],result_upload_picture['data_thumbFileId'][0]
        photoAlbum_controller().addPhoto(albumId=albumId,fileId=fileId_local,pictureName=attachmentName,thumbFileId=thumbFileId_local,epid=globalParams['epid'],token=globalParams['token'])
        result = photoAlbum_controller().getPhotoList(albumId = albumId,status='Add',fileId=fileId_local,pictureName=attachmentName,thumbFileId=thumbFileId_local,epid=globalParams['epid'],token=globalParams['token'])
        photoIdlist = result['data_pictureInfos_pictureId']
        photoAlbum_controller().rotatePhoto(albumId=albumId,albumType=1,fileId=fileId_local,fileName=attachmentName,pictureId=photoIdlist[0],rotateType=1,epid=globalParams['epid'],token=globalParams['token'])
        result_get_pictureBydocument = projectHisotry_controller().getPicture(parentId=0,deptid=globalParams['deptid'],token=globalParams['token'])
        attachmentNameByDocument = result_get_pictureBydocument['data_documentName'][0]
        fileId_document = result_get_pictureBydocument['data_fileId'][0]
        photoAlbum_controller().addPhoto(albumId=albumId,fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId="",epid=globalParams['epid'],token=globalParams['token'])
        result = photoAlbum_controller().getPhotoList(albumId = albumId,status='Add',fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId=None,epid=globalParams['epid'],token=globalParams['token'])
        photoIdlist=  result['data_pictureInfos_pictureId']
        renamePhotoName = '重命名相片'+str(int(time.time()))+".png"
        photoAlbum_controller().renamePhoto(albumId=albumId,photoAlbumType=1,pictureId=photoIdlist[-1],pictureName=renamePhotoName,epid=globalParams['epid'],token=globalParams['token'])
        photoAlbum_controller().getPhotoList(albumId = albumId,status='Rename',fileId=fileId_document,pictureName=renamePhotoName,thumbFileId=None,epid=globalParams['epid'],token=globalParams['token'])
        photoAlbum_controller().deletePhoto(fileId=fileId_document,photoAlbumType=1,pictureId=photoIdlist[-1],thumbFileId=None,epid=globalParams['epid'],token=globalParams['token'])
        photoAlbum_controller().getPhotoList(albumId = albumId,status='Delete',fileId=fileId_document,pictureName=renamePhotoName,thumbFileId=None,epid=globalParams['epid'],token=globalParams['token'])
        photoAlbum_controller().deleteAlbum(params = None,albumId=albumId,epid=globalParams['epid'],token=globalParams['token'])
        photoAlbum_controller().getAlbumList(epid=globalParams['epid'],deptid=globalParams['deptid'],token=globalParams['token'])

    @allure.story('添加相册和删除相册')
    def testdemo_2(self,teardown_module):
        '''
        用例描述：testdemo_2
        测试添加相册，并删除相册
        '''
        #随机生成相册名
        photoAlbumName ='自动化脚本相册'+generate_random_str()
        #添加相册
        result_add_photoAlbum = photoAlbum_controller().addAlbum(photoAlbumName=photoAlbumName)
        #获取新添加相册的相册id
        albumId = result_add_photoAlbum['data'][0]
        #获取相册列表
        results=photoAlbum_controller().getAlbumList()
        #校验先添加相册是否在相册集中
        photoAlbum_assert().getPhotoAlbumList(results,status="AddPhotoAlbum", albumId=albumId,photoAlbumName=photoAlbumName)
        #删除相册
        photoAlbum_controller().deleteAlbum(params = None,albumId=albumId)
        #获取相册列表
        results=photoAlbum_controller().getAlbumList()
        #校验相册是否已删除
        photoAlbum_assert().getPhotoAlbumList(results,status="DeletePhotoAlbum",albumId=albumId,photoAlbumName=photoAlbumName)

    @allure.story('相册重命名')
    def testdemo_3(self,teardown_module):
        '''
        用例描述：testdemo_3
        测试添加相册，并重命名相册，最后删除
        '''
        #随机生成相册名
        photoAlbumName ='自动化脚本相册'+generate_random_str()
        #添加相册
        result_add_photoAlbum = photoAlbum_controller().addAlbum(photoAlbumName=photoAlbumName)
        #获取新添加相册的相册id
        albumId = result_add_photoAlbum['data'][0]
        #随机生成重命名相册名
        photoAlbumRename='脚本相册'+generate_random_str()
        #重命名相册
        photoAlbum_controller().renameAlbum(photoAlbumName=photoAlbumRename,photoAlbumId=albumId)
        #获取相册列表
        results=photoAlbum_controller().getAlbumList()
        #校验重命名相册是否修改成功
        photoAlbum_assert().getPhotoAlbumList(results,status="RenamePhotoAlbum", albumId=albumId,photoAlbumName=photoAlbumRename)
        #删除相册
        photoAlbum_controller().deleteAlbum(params = None,albumId=albumId)

    @allure.story('从本地上传照片')
    def testdemo_4(self,teardown_module):
        '''
        用例描述：testdemo_4
        测试添加相册，从本地上传照片，最后删除相册
        '''
        #随机生成相册名
        photoAlbumName ='自动化脚本相册'+generate_random_str()
        #添加相册
        result_add_photoAlbum = photoAlbum_controller().addAlbum(photoAlbumName=photoAlbumName)
        #获取相册id，和图片名
        albumId,attachmentName = result_add_photoAlbum['data'][0],"test.jpg"
        #获取文件路径
        filespath = root + os.sep + "Data" + os.sep + attachmentName
        #上传文件
        files ={'file':(attachmentName,open(filespath,'rb'))}
        #上传文件到服务器
        result_upload_picture = fileUpload_controller().pictureUpload(files)
        #获取文件id和缩略图id
        fileId_local,thumbFileId_local = result_upload_picture['data_fileId'][0],result_upload_picture['data_thumbFileId'][0]
        #添加照片到相册集
        photoAlbum_controller().addPhoto(albumId=albumId,fileId=fileId_local,pictureName=attachmentName,thumbFileId=thumbFileId_local)
        #获取照片列表
        result = photoAlbum_controller().getPhotoList(albumId = albumId,fileId=fileId_local,pictureName=attachmentName,thumbFileId=thumbFileId_local)
        #校验照片列表
        photoAlbum_assert().getPhotoList(result,status='Add',fileId=fileId_local,pictureName=attachmentName,thumbFileId=thumbFileId_local)
        #删除相册
        photoAlbum_controller().deleteAlbum(params = None,albumId=albumId)

    @allure.story('图片旋转')
    def testdemo_5(self,teardown_module):
        '''
        用例描述：testdemo_5
        测试添加相册，图片上传，旋转，最后删除相册
        '''
        #随机生成相册名
        photoAlbumName ='自动化脚本相册'+generate_random_str()
        #添加相册
        result_add_photoAlbum = photoAlbum_controller().addAlbum(photoAlbumName=photoAlbumName)
        #获取相册id，和图片名
        albumId,attachmentName = result_add_photoAlbum['data'][0],"test.jpg"
        #获取文件路径
        filespath = root + os.sep + "Data" + os.sep + attachmentName
        #上传文件
        files ={'file':(attachmentName,open(filespath,'rb'))}
        #上传文件到服务器
        result_upload_picture = fileUpload_controller().pictureUpload(files)
        #获取文件id和缩略图id
        fileId_local,thumbFileId_local = result_upload_picture['data_fileId'][0],result_upload_picture['data_thumbFileId'][0]
        #添加照片到相册集
        photoAlbum_controller().addPhoto(albumId=albumId,fileId=fileId_local,pictureName=attachmentName,thumbFileId=thumbFileId_local)
        #获取照片列表
        result = photoAlbum_controller().getPhotoList(albumId = albumId,fileId=fileId_local,pictureName=attachmentName,thumbFileId=thumbFileId_local)
        #获取相片列表
        photoIdlist = result['data_pictureInfos_pictureId']
        #旋转照片
        photoAlbum_controller().rotatePhoto(albumId=albumId,albumType=1,fileId=fileId_local,fileName=attachmentName,pictureId=photoIdlist[0],rotateType=1)
        #删除相册
        photoAlbum_controller().deleteAlbum(params = None,albumId=albumId)

    @allure.story('添加资料的图片')
    def testdemo_6(self,teardown_module):
        '''
        用例描述：testdemo_6
        测试添加相册，添加资料的图片，最后删除相册
        '''
        #随机生成相册名
        photoAlbumName ='自动化脚本相册'+generate_random_str()
        #添加相册
        result_add_photoAlbum = photoAlbum_controller().addAlbum(photoAlbumName=photoAlbumName)
        #获取相册id
        albumId = result_add_photoAlbum['data'][0]
        #获取资料里面的图片集
        result_get_pictureBydocument = projectHisotry_controller().getPicture(parentId=0)
        #获取图片
        attachmentNameByDocument = result_get_pictureBydocument['data_documentName'][0]
        #获取图片id
        fileId_document = result_get_pictureBydocument['data_fileId'][0]
        #添加图片
        photoAlbum_controller().addPhoto(albumId=albumId,fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId="")
        #获取图片集
        result = photoAlbum_controller().getPhotoList(albumId = albumId,fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId=None)
        #校验添加的图片
        photoAlbum_assert().getPhotoList(result,status='Add',fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId=None)
        #删除相册
        photoAlbum_controller().deleteAlbum(params = None,albumId=albumId)

    @allure.story('重命名图片')
    def testdemo_7(self,teardown_module):
        '''
        用例描述：testdemo_7
        测试添加相册，重命名图片，最后删除相册
        '''
        #随机生成相册名
        photoAlbumName ='自动化脚本相册'+generate_random_str()
        #添加相册
        result_add_photoAlbum = photoAlbum_controller().addAlbum(photoAlbumName=photoAlbumName)
        #获取相册id
        albumId = result_add_photoAlbum['data'][0]
        #获取资料里面的图片集
        result_get_pictureBydocument = projectHisotry_controller().getPicture(parentId=0)
        #获取图片
        attachmentNameByDocument = result_get_pictureBydocument['data_documentName'][0]
        #获取图片id
        fileId_document = result_get_pictureBydocument['data_fileId'][0]
        #添加图片
        photoAlbum_controller().addPhoto(albumId=albumId,fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId="")
        #获取图片集
        result = photoAlbum_controller().getPhotoList(albumId = albumId,status='Add',fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId=None)
        #获取图片id和图片重命名
        photoIdlist,renamePhotoName= result['data_pictureInfos_pictureId'],'重命名相片'+str(int(time.time()))+".png"
        #图片重命名
        photoAlbum_controller().renamePhoto(albumId=albumId,photoAlbumType=1,pictureId=photoIdlist[-1],pictureName=renamePhotoName)
        #获取图片集
        result=photoAlbum_controller().getPhotoList(albumId = albumId,status='Rename',fileId=fileId_document,pictureName=renamePhotoName,thumbFileId=None)
        #校验重命名是否成功
        photoAlbum_assert().getPhotoList(result,status='Rename',fileId=fileId_document,pictureName=renamePhotoName,thumbFileId=None)
        #删除相册
        photoAlbum_controller().deleteAlbum(params = None,albumId=albumId)

    @allure.story('图片删除')
    def testdemo_8(self,teardown_module):
        '''
        用例描述：testdemo_8
        测试添加相册，添加图片，删除图片，最后删除相册
        '''
        #随机生成相册名
        photoAlbumName ='自动化脚本相册'+generate_random_str()
        #添加相册
        result_add_photoAlbum = photoAlbum_controller().addAlbum(photoAlbumName=photoAlbumName)
        #获取相册id
        albumId = result_add_photoAlbum['data'][0]
        #获取资料里面的图片集
        result_get_pictureBydocument = projectHisotry_controller().getPicture(parentId=0)
        #获取图片
        attachmentNameByDocument = result_get_pictureBydocument['data_documentName'][0]
        #获取图片id
        fileId_document = result_get_pictureBydocument['data_fileId'][0]
        #添加图片
        photoAlbum_controller().addPhoto(albumId=albumId,fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId="")
        #获取图片集
        result = photoAlbum_controller().getPhotoList(albumId = albumId,fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId=None)
        #获取图片id
        photoIdlist=  result['data_pictureInfos_pictureId']
        #删除图片
        photoAlbum_controller().deletePhoto(fileId=fileId_document,photoAlbumType=1,pictureId=photoIdlist[-1],thumbFileId=None)
        #获取图片列表
        result = photoAlbum_controller().getPhotoList(albumId = albumId,status='Delete',fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId=None)
        #校验是否删除
        photoAlbum_assert().getPhotoList(result,status='Delete',fileId=fileId_document,pictureName=attachmentNameByDocument,thumbFileId=None)
        #删除相册
        photoAlbum_controller().deleteAlbum(params = None,albumId=albumId)




if __name__ == '__main__':
    Test_projphotoalbum_integration().testdemo_2()
