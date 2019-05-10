#coding=utf-8
import sys,os,time
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)
from API.Public.LoginMyluban import *
from API.swagger.project_dashboard import *



#将登陆的cookie写入到txt中
print ('start Setup.py')
#覆盖率初始化
checkAPICoverageRate(status='Init')
#获取cookies并写到txt中
Cookie = LoginWeb()
with open(Path["cookieRoot"],"w") as f:
    f.write(Cookie)
project_dashboard().showListProjectDashboard_New()
project_dashboard().showDeptIDContent()
#写覆盖率
checkAPICoverageRate()
#删除超过上限的性能报告CSV文件
deleteRedundantPerformanceCSVFile()
