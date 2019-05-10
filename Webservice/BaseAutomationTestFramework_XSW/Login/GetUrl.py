#coding==utf-8
#通过接口获得各个系统的url

from Public.HeaderManage import *
from Public.ResponseBase import *
from Public.WebRequestManage import *
from Setting import *

pdsUrl = LoginConfig['pdsUrl']
urlFilePath = Path['UrlPath']

class get_product_url:


    '''通过接口获得各个系统的url'''
    def interface_lbws_casLoginService(self, url=pdsUrl, token=None, **kwargs):

        url = url + '/webservice/lbws/casLoginService'
        req_xml = self.req_lbws_casLoginService()
        resp_xml = Webrequests().post(url, req_xml, headers_text_xml(token))
        return self.resp_lbws_casLoginService_getServUrlResponse(resp_xml)

    def req_lbws_casLoginService(self):

        req_xml = '''
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SASS="http://login.webservice.login.sso.lubansoft.com/">
            <SOAP-ENV:Body>
                <SASS:getServUrl/>
            </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
        '''
        return req_xml

    def resp_lbws_casLoginService_getServUrlResponse(self,data):
        '''
        将返回的url进行组装
        :param data: 返回的xml
        :return: [('pdscommon', 'http://center.lubansoft.com/pdscommon'), ('pdsdoc', 'http://pdsdoc.lubansoft.com')]
        '''
        result = resp_base(data)
        json_data = eval(pythonXmlToJson(data.text))
        severUrl_list = json_data.get("soap:Envelope").get( 'soap:Body').get('ns2:getServUrlResponse').get('return')

        key_list = ['serverName','serverURL']
        result['return_list'] = Recombition_list(key_list,severUrl_list)
        urlName = result['return_list']['serverName_list']
        urlAddress = result['return_list']['serverURL_list']
        result_serverName_serverURL = zip(urlName,urlAddress)
        return result_serverName_serverURL

class get_center_url:
    def interface_rs_centerLogin_serverurl(self,url=pdsUrl,token=None):
        url = url+ '/rs/centerLogin/serverurl'
        result = Webrequests().get(url,'',headers(token))
        return self.resp_rs_centerLogin_serverurl(result)

    def resp_rs_centerLogin_serverurl(self,data):
        result = resp_base(data)
        key = ['serverName','serverURL']
        context = data.json()
        result['return_list'] = Recombition_list(key,context)
        urlName = result['return_list']['serverName_list']
        urlAddress = result['return_list']['serverURL_list']
        result_serverName_serverURL = zip(urlName,urlAddress)
        return result_serverName_serverURL

class write_url_to_file:
    '''
    将获得的url写入url.txt文件里
    '''
    def __init__(self,urlFilePath,splitSymbol=SpliteSymbol):
        self.urlFilePath = urlFilePath
        self.splitSymbol = splitSymbol


    def write_url_to_txt(self):
        #将产品相关的url写入文件
        result_serverName_serverURL_product = get_product_url().interface_lbws_casLoginService()

        for name,url in result_serverName_serverURL_product :
            with open(self.urlFilePath,'a+') as f:
                f.write(name + self.splitSymbol + url+'\n')

        #将center相关的url写入文件
        result_serverName_serverURL_center = get_center_url().interface_rs_centerLogin_serverurl()

        for name,url in result_serverName_serverURL_center :
            with open(self.urlFilePath,'a+') as f:
                f.write(name+ self.splitSymbol + url+'\n')


if  __name__ == "__main__":
    with open(urlFilePath, 'w') as f:
        f.write('')








