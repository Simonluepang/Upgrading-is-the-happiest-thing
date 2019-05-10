#coding=utf-8
import sys
import inspect

sys.path.append('..')
from API.Public.CommonFunction import *
from API.Public.AssertFunction import *

class project_dashboard:
    def showDeptIDContent(self,**kwargs):
        token = eval(open(Path['cookieRoot'],'r').readline())['cookies']
        params = getGlobalParams()
        url =URL + "/rest/projdashboard/listtype/dept/list/"+str(params['epid'])+'/'+str(params['orgid'])+'/2'
        result =response(WebRequests().get(url,kwargs,{"Cookie": token}))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        params['deptid']=result['data_projectId'][0]
        context = str(params)
        with open(Path['globalParams'], 'w+') as f:
            f.write(context)
        return result

    def showListProjectDashboard_New(self,**kwargs):
        context ={}
        token = eval(open(Path['cookieRoot'],'r').readline())['cookies']
        url =URL + "/rest/projdashboard/listEnterprise?"
        result =response(WebRequests().get(url,kwargs,{"Cookie": token}))
        funcname = str(self.__class__.__name__)+'.'+str(inspect.stack()[0][3])
        assert_general(result,funcname)
        context['orgid'],context['epid']=result['data_orgId'][0],result['data_epid'][0]
        context['token']=str({'projectId':context['orgid'],'epId':context['epid']})
        with open(Path['globalParams'], 'w+') as f:
            f.write(str(context))
        return result
