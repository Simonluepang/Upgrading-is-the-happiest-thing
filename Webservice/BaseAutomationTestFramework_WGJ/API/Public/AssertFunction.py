#coding=utf-8
import unittest
import allure
from API.Public.WebRequest import *
from API.Public.CommonFunction import *
import API.Public.CommonFunction


def assert_general(result,funcName,basetime =1000,status = 200,msg = 'success'):
    assert result["status_code"] == status
    if msg!="":
        assert result['msg'][0] == msg, result['msg'][0]
    API.Public.CommonFunction.g_APICoverage.append(funcName)
    if result["responsetime"]>float(basetime):
        logInfo = '%s 接口：%s,返回时间：%.2f ms，期望时间：%.2f ms'%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),str(funcName),result["responsetime"],basetime)
        print(logInfo)
        context = str(funcName).split('.')[0]+','+str(funcName).split('.')[1]+','+str(basetime)+','+str(result["responsetime"])+'\n'
        API.Public.CommonFunction.g_InterfacePerformance.append(context)
    print(str(funcName))

@allure.step('校验预期值与实际值，key={key}，实际结果，{0},预期结果，{exceptedValue}')
def assert_commonFunction(actualValue,exceptedValue,**kwargs):
    if isinstance(actualValue[kwargs['key']],list):
        if exceptedValue != actualValue[kwargs['key']]:
            if [False for value in exceptedValue if value not in actualValue[kwargs['key']]]:assert False,'实际值不包含所有的预期值'
    elif isinstance(actualValue[kwargs['key']],str):
        assert actualValue[kwargs['key']]!="" and actualValue[kwargs['key']]!= None,'实际值不能为空'
        assert actualValue[kwargs['key']]==exceptedValue,'预期值不等于实际值'
    else:
        assert False,'只支持list和str的校验，其余暂不支持'




class collaboration_controller_assert:
    def getDangerFactorsList_epid(self,expectedValue,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert len(actualValue['data']) >0,'data数据为空list'
        namelist =expectedValue['Factorname'].split(',')
        for name in namelist:
            assert name in actualValue['data_list']['name_list'],name

    def getDangerTypeList(self,expectedValue,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert len(actualValue['data']) >0,'data数据为空list'
        namelist =expectedValue['Typename'].split(',')
        for name in namelist:
            assert name in actualValue['data_list']['name_list'],name

    def getPageDangerLibs(self,actualValue,expectedValue=[]):
        if expectedValue ==[]:
            assert actualValue['status_code'] == 200,'返回不是200'
            assert len(actualValue['data']) >0,'data数据为空list'
            assert len(actualValue['data_list']['content_list']) >0
            assert len(actualValue['data_list']['description_list']) >0
            assert len(actualValue['data_list']['description_list']) == len(actualValue['data_list']['content_list'])

    def createCollaboration(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['data']!="" or actualValue['data']!= None
        assert actualValue['msg'] == 'success'

    def getCollaboration(self,actualValue,expectedvalue,status='Operation'):
        assert actualValue['status_code'] == 200,'返回不是200'
        if status =='Operation':
            assert actualValue['data']['name'] == expectedvalue['name'],actualValue['name']
            assert actualValue['data']['dangerLib']['content'] == expectedvalue['dangerLib']['content'] ,actualValue['data']['dangerLib']['content']
            assert actualValue['data']['dangerLib']['dangerFactorId'] == expectedvalue['dangerLib']['dangerFactorId'],actualValue['data']['dangerLib']['dangerFactorId']
            assert actualValue['data']['dangerLib']['dangerFactorName'] == expectedvalue['dangerLib']['dangerFactorName'],actualValue['data']['dangerLib']['dangerFactorName']
            assert actualValue['data']['dangerLib']['dangerTypeName'] == expectedvalue['dangerLib']['dangerTypeName'] ,actualValue['data']['dangerLib']['dangerTypeName']
            assert actualValue['data']['dangerLib']['dangerTypeId'] == expectedvalue['dangerLib']['dangerTypeId'],actualValue['data']['dangerLib']['dangerTypeId']
            assert actualValue['data']['dangerLib']['description'] == expectedvalue['dangerLib']['description'],actualValue['data']['dangerLib']['description']
            assert actualValue['msg'] == 'success'
        elif status =='Delete':
            assert actualValue['code'] == 303
            assert actualValue['msg'] == '当前协作不存在或已删除'
        elif status == 'Edit':
            assert actualValue['data']['name'] == expectedvalue['name'],actualValue['name']
            assert actualValue['data']['dangerLib']['content'] == expectedvalue['dangerLib']['content'] ,actualValue['data']['dangerLib']['content']
            assert actualValue['data']['dangerLib']['description'] == expectedvalue['dangerLib']['description'],actualValue['data']['dangerLib']['description']

    def removeCollaboration(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == 'success'

    def checkOutCollaboration(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == 'success'

    def editCollaboration(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == 'success'

    def checkInCollaboration(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == 'success'

class projectHistory_assert:
    def create_projectHistory(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        assert actualValue['data']!=""

    def get_projectHistory(self,actualValue,status= 'Add',**kwargs):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        if 'historyId' in kwargs and status =='Add':
            assert kwargs['historyId'] in actualValue['historyId_list']
            assert kwargs['historyName'] in actualValue['historyName_list']
        else:
            assert kwargs['historyId'] not in actualValue['historyId_list']
            assert kwargs['historyName'] not in actualValue['historyName_list']

    def update_projectHistory(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        assert actualValue['data']==True

    def delete_projectHistory(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        assert actualValue['data']==True

    def add_Node(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        assert actualValue['data']!=""

    def get_Node(self,actualValue,status='Add',**kwargs):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        assert actualValue['historyId']==kwargs['projectHistoryID']
        assert actualValue['historyName'] ==kwargs['projectHistoryName']
        if status =='Add':
            assert kwargs['nodeName'] in actualValue['view_nodeName_list']
            for value in actualValue['view_nodeId_list']:assert value!=""
            assert kwargs['ts'] in actualValue['view_time_list']
            for value in actualValue['view_description_list']: assert value==""
            for value in actualValue['view_views_list']: assert value ==None
        elif status == 'Edit':
            assert kwargs['nodeName'] in actualValue['view_nodeName_list']
            assert kwargs['nodeId']  in actualValue['view_nodeId_list']
            assert kwargs['ts'] in actualValue['view_time_list']
            assert kwargs['description'] in actualValue['view_description_list']
            for value in actualValue['view_views_list']: assert value !=None
        else:
            assert kwargs['nodeName'] not in actualValue['view_nodeName_list']
            assert kwargs['nodeId'] not in actualValue['view_nodeId_list']

    def update_Node(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        assert actualValue['data']==None

    def delete_Node(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        assert actualValue['data']==True

    def add_Picture(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        assert actualValue['data']!=""

    def get_detail(self,actualValue,hisotryId,historyName,description,times,attachmentName,fileId,thumbFileId,status='Add',**kwargs):
        assert_general(actualValue)
        assert hisotryId == actualValue['data_historyId']
        assert historyName == actualValue['data_historyName']
        assert description in actualValue['views_description']
        #assert times in actualValue['views_time']
        if status !='Delete':
            assert attachmentName in actualValue['views_views_attachmentName']
            assert fileId in actualValue['views_views_fileId']
            assert thumbFileId in actualValue['views_views_thumbFileId']
        else:
            assert attachmentName not in actualValue['views_views_attachmentName']
            assert fileId not in actualValue['views_views_fileId']
            assert thumbFileId not in actualValue['views_views_thumbFileId']
        for value in actualValue['views_views_originUrl']: assert "downloadSystemFileUnEncrypt/" in value
        for value in actualValue['views_views_thumbUrl']: assert "downloadSystemFileUnEncrypt/" in value
        if status == 'Sort':
            assert kwargs['attachmentId_list'] == actualValue['views_views_attachmentId']

    def sort_picture(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        assert actualValue['data']!=""

    def delete_Picture(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['msg'] == "success"
        assert actualValue['code'] == 1
        assert actualValue['data']==True

class photoAlbum_assert:

    @allure.step('校验获取的相册列表')
    def getPhotoAlbumList(self,actualValue,status ="init",**kwargs):
        if status in ["init"]:
            assert actualValue['data_albumId'][0] == "9"
            assert actualValue['data_albumName'][0] =="手机相册"
            assert actualValue['data_coverUUId'][0] == None
            assert actualValue['data_coverUrl'][0] == None
            assert actualValue['data_editFlag'][0] in [True,False]
            assert actualValue['data_photoTotalNum'][0] >=0
            assert len(actualValue['data_albumId']) >=1
        elif status in ["AddPhotoAlbum","RenamePhotoAlbum"]:
            assert kwargs['albumId'] in actualValue['data_albumId']
            pos = actualValue['data_albumId'].index(kwargs['albumId'])
            assert kwargs['photoAlbumName'] == actualValue['data_albumName'][pos]
            assert actualValue['data_coverUUId'][pos] == None
            assert actualValue['data_coverUrl'][pos] == None
            assert actualValue['data_editFlag'][pos] == True
            assert actualValue['data_photoTotalNum'][pos] ==0
        elif status in ['DeletePhotoAlbum']:
            assert kwargs['albumId'] not in actualValue['data_albumId']
            assert kwargs['photoAlbumName'] not in actualValue['data_albumName']

    @allure.step("校验获取相片列表")
    def getPhotoList(self,actualValue,status=None,**kwargs):
        assert actualValue['data_editFlag'][0] in [False,True]
        if status ==None:
            assert actualValue['data_pictureInfos'][0] ==None
            assert actualValue['data_totalPageNum'][0]==0
            assert actualValue['data_totalRecordNum'][0]==0
        elif status in ["Add",'Rename']:
            assert kwargs['fileId'] in actualValue['data_pictureInfos_fileId']
            for value in actualValue['data_pictureInfos_fileUrl']: assert 'downloadSystemFileUnEncrypt' in value
            assert None not in actualValue['data_pictureInfos_pictureId']
            assert kwargs['pictureName'] in actualValue['data_pictureInfos_pictureName']
            assert kwargs['thumbFileId'] in actualValue['data_pictureInfos_thumbFileId']
            for value in actualValue['data_pictureInfos_thumbUrl']: assert 'downloadSystemFileUnEncrypt' in value
        elif status =='Delete':
            if actualValue['data_pictureInfos'][0]!=None:
                assert kwargs['fileId'] not in actualValue['data_pictureInfos_fileId']
                assert kwargs['pictureName'] not in actualValue['data_pictureInfos_pictureName']
                assert kwargs['thumbFileId'] not in actualValue['data_pictureInfos_thumbFileId']

    def addPhotoAlbum(self,actualValue):
        assert actualValue['data'][0]!="" or actualValue['data']!= None

    def renamePhotoAlbum(self,actualValue):
        assert actualValue['data'][0]!="" or actualValue['data']!= None

    def addPhoto(self,actualValue):
        assert actualValue['data']!="" or actualValue['data']!= None

    def rotatePhoto(self,actualValue):
        assert actualValue['data']!="" or actualValue['data']!= None

    def renamePhoto(self,actualValue):
        assert actualValue['data']!="" or actualValue['data']!= None

    def deletePhoto(self,actualValue):
        assert actualValue['data']!="" or actualValue['data']!= None

class fileUpload_assert:
    def pictureUpload(self,actualValue):
        assert actualValue['data_fileId'][0] not in [None,'']
        assert actualValue['data_thumbFileId'][0] not in [None,'']

class projectDashboard_assert:
    def getdeptContent(self,actualValue,status = 'init'):
        if status in ["init"]:
            assert actualValue['data_attentionFlag'][0] == False
            for value in actualValue['data_bbsNums'] :assert str(value).isdigit()
            for value in actualValue['data_bimNums'] :assert str(value).isdigit()
            for value in actualValue['data_coNums'] :assert str(value).isdigit()
            for value in actualValue['data_dataNums'] :assert str(value).isdigit()
            #for value in actualValue['data_lastModifiedDate'] :assert str(value).isdigit()
            for value in actualValue['data_projectId'] :assert value !=None
            for value in actualValue['data_projectName'] :assert value !=None
            #for value in actualValue['data_sortStatus'] :assert str(value).isdigit()
            for value in actualValue['data_taskNums'] :assert str(value).isdigit()

    def getAttention(self,actualValue):
        assert actualValue['status_code'] == 200,'返回不是200'
        assert actualValue['data']!="" or actualValue['data']!= None
        assert actualValue['msg'] == 'success'

    def getattentionList(self,actualValue,epid,projectid,projectName,status = 'Add'):
        if status in ["Add"]:
            assert actualValue['data_attentionFlag'][0] == True
            assert actualValue['data_epid'][0] == epid
            assert actualValue['data_isProcessPermission'][0] in [True,False]
            assert actualValue['data_isProjectPermission'][0] in [True,False]
            assert actualValue['data_isSuperAdmin'][0] in [True,False]
            #for value in  actualValue['data_lastModifiedDate']: assert str(value).isdigit() or value == None
            assert actualValue['data_prjectId'][0] == projectid
            assert actualValue['data_projectName'][0] == projectName
            if actualValue['data_taskProcess'][0] !=None : assert "%" in actualValue['data_taskProcess'][0]
        elif status in ['Delete']:
            assert epid not in actualValue['data_epid']
            assert projectid not in actualValue['data_prjectId']

class UIAssertFunction(unittest.TestCase):
    def UIassertEqual(self,excepted,actualed):
        self.assertEqual(actualed,excepted)