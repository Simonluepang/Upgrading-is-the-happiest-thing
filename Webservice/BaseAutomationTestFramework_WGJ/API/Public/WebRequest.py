#coding=utf-8
import sys,requests,json,warnings
sys.path.append('..')
from API.Public.Pylogging import *

warnings.filterwarnings("ignore")
session = requests.session()
#log = Logger('Error',level='crit')
session.keep_alive = False

class WebRequests:

    def get(self,url,para,headers):
        try:
            r = session.get(url,params=para,headers=headers, verify=False, allow_redirects=False)
            return r
        except BaseException as e:
            print(str(e))
        finally:
            print(str(r.status_code))

    def post(self,url,para,headers):
        try:
            r = requests.post(url,data=para,headers=headers,verify=False, allow_redirects=False)
            return  r
        except BaseException as e:
            print(str(e))
        finally:
            print(str(r.status_code))

    def post_json(self,url,para,headers):
        try:
            data = para
            data = json.dumps(data)   #python数据类型转化为json数据类型
            r = session.post(url,data=data,headers=headers,verify=False, allow_redirects=False )
            return r

        except BaseException as e:
            print(str(e))
        finally:
            print(str(r.status_code))

    def post_file(self,url,para,headers):
        try:
            r = requests.post(url,headers=headers,files=para,verify=False, allow_redirects=False)
            return  r
        except BaseException as e:
            print(str(e))
        finally:
            print(str(r.status_code))

    def delete(self,url,para,headers):
        try:
            data = para
            data = json.dumps(data)
            r = session.delete(url,data=data,headers=headers,verify = False,allow_redirects=False)
            return r
        except BaseException as e:
            print(str(e))
        finally:
            print(str(r.status_code))

    def put(self,url,para,headers):
        try:
            data = para
            data = json.dumps(data)
            r = session.put(url,data=data,headers=headers,verify = False,allow_redirects=False)
            return r
        except BaseException as e:
            print(str(e))
        finally:
            print(str(r.status_code))


