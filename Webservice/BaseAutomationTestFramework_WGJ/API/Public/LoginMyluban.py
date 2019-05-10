#coding=utf-8
import sys

from API.swagger.login import *

sys.path.append("..")


def LoginWeb():
        param = {'username':Config['user'],"password":Config['pwd']}
        print(param)
        result = login().rest_login(**param)
        param['cookies']=result.headers['Set-Cookie'][0:46]
        return str(param)


if __name__ == "__main__":
    result = LoginWeb()
    print(result)