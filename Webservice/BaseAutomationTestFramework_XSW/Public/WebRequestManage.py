#coding=utf-8
import requests
import json
import warnings
warnings.filterwarnings("ignore")

session = requests.session()
session.keep_alive = False

class Webrequests:

    def get(self,url,para,headers):
        try:
            r = session.get(url,params=para,headers=headers, verify=False, allow_redirects=False)
            return r
        except BaseException as e:
            print("请求失败！",str(e))



    def post(self,url,para,headers):
        try:
            r = session.post(url,data=para,headers=headers,verify=False, allow_redirects=False)
            return  r
        except BaseException as e:
            #return str(e)
            print("请求失败！",str(e))


    def post_json(self,url,para,headers):
        try:
            data = para
            data = json.dumps(data)   #python数据类型转化为json数据类型
            r = session.post(url,data=data,headers=headers,verify=False, allow_redirects=False)
            return r

        except BaseException as e:
            #return str(e)
            print("请求失败！",str(e))
        # finally:
        #     print(r.status_code)

    def delete(self,url,para,headers):
        try:
            data = para
            data = json.dumps(data)
            r = session.delete(url,data=data,headers=headers,verify = False,allow_redirects=False)
            return r
        except BaseException as e:
            #return str(e)
            print("请求失败！",str(e))

    def put(self,url,para,headers):
        try:
            data = para
            data = json.dumps(data)
            r = session.put(url,data=data,headers=headers,verify = False,allow_redirects=False)
            return r
        except BaseException as e:
            #return str(e)
            print("请求失败！",str(e))


