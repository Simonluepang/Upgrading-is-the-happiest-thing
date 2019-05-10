#coding=utf-8
import sys
sys.path.append('..')
from API.Setting import *
from API.Public.WebRequest import *

URL =Config['mainUrl']

class login:
    def rest_login(self,**kwargs):
        url =URL + "/rest/login"
        header = {'Content-type': 'application/json'}
        return WebRequests().post_json(url,kwargs,header)