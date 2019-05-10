#coding=utf-8
from Login.SinglePointLogin import *
builderCookie = read_dynamic_generation_txt(CookieFilePath,'builder')
SPMatchName =  ProductConfig['PLAN']['UrlmatchName']
BEMatchName = ProductConfig['BE']['UrlmatchName']
GOVMatchName = ProductConfig['GOV']['UrlmatchName']
COMatchName = ProductConfig['CO']['UrlmatchName']
BuilerMatchName = ProductConfig['builder']['UrlmatchName']
processMatchName = ProductConfig['process']['UrlmatchName']

class gov_login:
    def prod_login_common_method(cls,req_func,MatchName):
        '''
        GOV,CO等登录的公共方法，通过跳转302来最终获得cookie
        :param req_func: 请求返回的响应方法
        :param name_product_cookie: 生成在headertxt中的cookie名字,方便后续产品获取
        :return:
        '''
        #获得service_url from Location
        resp = req_func
        service_url = resp.headers['Location']

        #获得ticket_url
        token = read_dynamic_generation_txt(CookieFilePath,'pds_CASTGC_cookie')
        resp = Webrequests().get(service_url,'',headers(token))
        ticket_url = resp.headers['Location']

        #获得GOV的cookie
        resp = Webrequests().post(ticket_url,'',headers_text_xml())

        if resp.headers['Set-Cookie'] != None:
            print(u'%s获得登陆成功！'%MatchName)
            write_value_to_txt(CookieFilePath,MatchName,resp.headers['Set-Cookie'])
        else:
            print(u'%s获得登陆失败！' % MatchName)

    def gov_interface(cls,token=None):
        govUrl = read_dynamic_generation_txt(UrlFilePath,GOVMatchName)
        url = govUrl + '/webservice/managecontrol/deptMap'
        req = '''
                        <?xml version="1.0" encoding="UTF-8"?>
                <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:PROJDEPTINFO="http://webservice.managecontrol.pdsmc.lubansoft.com/">
                    <SOAP-ENV:Body>
                        <PROJDEPTINFO:getProvinceInfo/>
                    </SOAP-ENV:Body>
                </SOAP-ENV:Envelope>'''

        return Webrequests().post(url,req,headers_text_xml(token))

    def get_gov_cookie(cls):
        cls.prod_login_common_method(cls.gov_interface(), GOVMatchName)

class co_login(gov_login):
    def co_interface(self):
        coUrl = read_dynamic_generation_txt(UrlFilePath, COMatchName)
        return Webrequests().get(coUrl,'',headers())

    def get_co_cookie(cls):
        cls.prod_login_common_method(cls.co_interface(),COMatchName)

class plan_login(pds_login):
    def plan_interface(cls):
        planUrl = read_dynamic_generation_txt(UrlFilePath,SPMatchName,SpliteSymbol)
        url = planUrl + '/webservice/login/commonlogin'
        req_xml = '''
                    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:COMMONLOGIN="http://webservice.login.pds.lubansoft.com/">
            <SOAP-ENV:Body>
                <COMMONLOGIN:login2018>
                    <loginParam>
                        <enterpriseId>%s</enterpriseId>
                        <hardwareCodes>49148c4de728a29f95f561f85243385f-d0b7ebe000d64b4e31cb7ca6b13a010d</hardwareCodes>
                        <innetIp>192.168.99.1</innetIp>
                        <password>%s</password>
                        <username>%s</username>
                        <version>4.5.0</version>
                    </loginParam>
                    <productId>%s</productId>
                </COMMONLOGIN:login2018>
            </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
                    ''' % (enterpriseId, userPwd, userName, productId)
        return Webrequests().post(url,req_xml,headers_text_xml())

    def get_plan_cookie(cls):
        resp = cls.plan_interface()
        if resp.headers['Set-Cookie'] != None:
            print(u'%s获得登陆成功！'%SPMatchName)
            write_value_to_txt(CookieFilePath,SPMatchName,resp.headers['Set-Cookie'])
        else:
            print(u'%s获得登陆失败！' % SPMatchName)

class be_login(pds_login):
    def be_interface(cls):
        beUrl = read_dynamic_generation_txt(UrlFilePath,BEMatchName,SpliteSymbol)
        url = beUrl + '/webservice/lbsca/LoginValidateWebService'
        req_xml = '''
                <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns1="http://login.webservice.be.lubansoft.com/">
            <SOAP-ENV:Body>
                <ns1:loginBE>
                    <loginParam>
                        <admin>true</admin>
                        <enterpriseId>%s</enterpriseId>
                        <hardwareCodes>49148c4de728a29f95f561f85243385f-d0b7ebe000d64b4e31cb7ca6b13a010d</hardwareCodes>
                        <innetIp>192.168.99.1</innetIp>
                        <password>%s</password>
                        <productId>%s</productId>
                        <username>%s</username>
                        <version/>
                    </loginParam>
                </ns1:loginBE>
            </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
        ''' % (enterpriseId, userPwd, productId ,userName)
        return Webrequests().post(url,req_xml,headers_text_xml())



    def get_be_cookie(cls):
        resp = cls.be_interface()
        if resp.headers['Set-Cookie'] != None:
            print(u'%s获得登陆成功！'%BEMatchName)
            write_value_to_txt(CookieFilePath,SPMatchName,resp.headers['Set-Cookie'])
        else:
            print(u'%s获得登陆失败！' % BEMatchName)

class Center_login:
    def prod_login_common_method(cls,req_func,MatchName):
        '''
        builder登录的公共方法，通过跳转302来最终获得cookie
        :param req_func: 请求返回的响应方法
        :param MatchName: 该名字会生成到cookie文件，方面后续通过该名字取得cookie值
        :return:
        '''
        #获得service_url from Location
        resp = req_func
        # 获得builder的cookie
        if resp.headers['Set-Cookie'] != None:
            print(u'%s获得登陆成功！'%MatchName)
            write_value_to_txt(CookieFilePath,MatchName,resp.headers['Set-Cookie'])

        service_url = resp.headers['Location']

        #获得ticket_url
        token = read_dynamic_generation_txt(CookieFilePath,'pds_CASTGC_cookie')
        resp = Webrequests().get(service_url,'',headers(token))
        ticket_url = resp.headers['Location']

        Webrequests().post(ticket_url,'',headers_text_xml())


    def center_interface(cls,MatchName):
        BuilderUrl = read_dynamic_generation_txt(UrlFilePath, MatchName, SpliteSymbol)[:-15]+'builder-web'
        url = BuilderUrl + '/subs/menu/-1'
        return Webrequests().get(url,'',headers())

    def process_interface(cls,MatchName):
        BuilderUrl = read_dynamic_generation_txt(UrlFilePath, MatchName, SpliteSymbol)
        url = BuilderUrl + '/subs/menu/-1'
        return Webrequests().get(url,'',headers())

    def get_builder_cookie(cls):
        cls.prod_login_common_method(cls.center_interface(BuilerMatchName), BuilerMatchName)

    def get_process_cookie(cls):
        cls.prod_login_common_method(cls.process_interface(processMatchName),processMatchName)


if __name__ == '__main__':
    print(BuilerMatchName)



