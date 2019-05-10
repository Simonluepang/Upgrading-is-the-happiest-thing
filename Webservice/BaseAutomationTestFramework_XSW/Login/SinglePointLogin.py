#coding=utf-8
import random
import re
import string

from Map.ProductIdMap import *
from Public.HeaderManage import *
from Public.WebRequestManage import *
from Setting import *

pdsUrl = LoginConfig['pdsUrl']
userName = LoginConfig['user']
userPwd = LoginConfig['pwd']
enterpriseId = LoginConfig['epid']
productId = LoginConfig['productId']
CookieFilePath = Path['CookiePath']
UrlFilePath = Path['UrlPath']
root_url = read_dynamic_generation_txt(UrlFilePath, 'builder', SpliteSymbol)[:-10].replace(":","%3A").replace("/","%2F")





class pds_login:
    '''
    1.通过该方法可以获得单点登录需要的CASTGC
    2.并选择需要登陆的企业
    ps:任何客户端都可以通过该方法获得
    '''

    def __init__(self,user = userName,pwd = userPwd,epid = enterpriseId,proId = productId ,url = pdsUrl):
        self.url = url
        self.user = user
        self.pwd = pwd
        self.epid = epid
        self.proId = proId

    def pds_login_get(self):
        url = self.url + "/login?"
        token = ''.join(random.sample(string.ascii_letters.upper() + string.digits, 32))
        resp = Webrequests().get(url, '', headers_json(
            f"UM_distinctid=1690448e64422d-0a531302fd9e44-3a3a5d0c-1fa400-1690448e6458b; JSESSIONID={token}"))
        #获得pds cookie，该cookie在获得CASTGC时需要使用
        cookie = resp.headers['Set-Cookie']
        global pds_cookie
        pds_cookie = cookie

        assert resp.status_code == 200
        assert pds_cookie != None,'pds_cookie为空'


        #通过该接口获得LT
        html = resp.text
        pattern = 'value="LT(.+?)" />'
        lt = re.findall(pattern,html)[0]

        return lt


    def login_get_CASTGC(self):
        url = self.url + "/login?service=" + root_url
        lt = self.pds_login_get()

        req = {
                    "username": self.user,
                    "password": self.pwd,
                    "productId": self.proId,
                    "lt": 'LT' + lt,
                    "execution": "e1s1",
                    "_eventId":"submit",
                    "submit":"LOGIN",

        }
        resp = Webrequests().post(url, req, headers_form_urlencoded(pds_cookie))
        assert resp.status_code == 200, ' %d error' % resp.status_code

        #获得cookie中的内容，并将GASTGC内容提取出来与pds cookie进行组装，为后面第二次跳转使用
        Cookie = resp.headers['Set-Cookie']
        CASTGC = 'CASTGC' + re.findall("CASTGC(.+?) Path=/", Cookie)[0]

        global pds_CASTGC_cookie
        pds_CASTGC_cookie = pds_cookie + ';' + CASTGC

        write_value_to_txt(CookieFilePath,'pds_CASTGC_cookie',pds_CASTGC_cookie)


    def choice_enterprise_to_login(cls):
        '''登陆某一个企业，该步骤必须执行，不然cookie中无企业信息，会导致部分接口报错'''
        url =  pdsUrl + '/rs/centerLogin/login'
        req = {"epid":enterpriseId,"username":userName,"password":userPwd}
        resp = Webrequests().post_json(url,req,headers_json())
        assert resp.status_code == 200



if __name__ == "__main__":
    # pds_login(user = '13818865948',pwd = '90f1c670b504c873a01a767d0e472aa6').login_get_CASTGC()
    #pds_login().choice_enterprise_to_login()
    print(root_url)



