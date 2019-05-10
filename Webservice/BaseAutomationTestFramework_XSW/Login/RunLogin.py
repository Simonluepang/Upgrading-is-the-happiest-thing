#coding=utf-8
import sys
sys.path.append("..")
from Login.GetUrl import *
#清空urlFilePath中的记录值,并将url的值
with open(urlFilePath,'w') as f:
    f.write('')
write_url_to_file(urlFilePath,SpliteSymbol).write_url_to_txt()


from Login.SinglePointLogin import *
#清空Cookie文件中的记录值,并将新的Cookie的值写入
with open(CookieFilePath,'w') as f:
    f.write('')

pds_login().login_get_CASTGC()   #获得CASTGC
pds_login().choice_enterprise_to_login()  #选择某个企业进行登陆


from Login.ClientLogin import *
#各个端登录
# co_login().get_co_cookie()
# be_login().get_be_cookie()
Center_login().get_builder_cookie()
Center_login().get_process_cookie()