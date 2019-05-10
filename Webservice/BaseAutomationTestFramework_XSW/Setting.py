#coding=utf-8
import os

LoginConfig =  { "pdsUrl":"http://pds.lubansoft.com",
              "user": '徐莘伟',
              "pwd" : "e10adc3949ba59abbe56e057f20f883e",
              "epid": 1096,
              "productId":100}
OrderConfig = {
    "username": '徐莘伟',
    'packageType': 2,
    'functionName': '鲁班土建(企业)VIP'}


root = os.path.dirname(os.path.abspath(__file__)) #当前文件目录
Path = {    'CookiePath':  os.path.join(root,'Data','Cookie.txt'),
            'UrlPath' : os.path.join(root,'Data','Url.txt')        }


#其他配置
SpliteSymbol = '==>'    #写入txt文件key和value的分隔符

"""
# 正式外网
LoginConfig =  { "pdsUrl":"http://pds.lubansoft.com",
              "user": '徐莘伟',
              "pwd" : "e10adc3949ba59abbe56e057f20f883e",
              "epid": 1096,
              "productId":100}
OrderConfig = {
    "username": '徐莘伟',
    'packageType': 2,
    'functionName': '鲁班土建(企业)VIP'}
# 测试外网
LoginConfig =  { "pdsUrl":"http://pdscenter.lubansoft.net",
              "user": 'xushenwei',
              "pwd" : "96e79218965eb72c92a549dd5a330112",
              "epid": 3,
              "productId":100}
OrderConfig = {
    "username": '徐莘伟',
    'packageType': 2,
    'functionName': '鲁班土建云功能套餐'}
OrderConfig = {
    "functionName": "鲁班土建(企业)BIM应用套餐",
    "packageType": 12,
    "username": 'xushenwei'
}
# 测试内网
LoginConfig =  { "pdsUrl":"http://192.168.13.195:8080/pds",
              "user": 'xushenweitest',
              "pwd" : "96e79218965eb72c92a549dd5a330112",
              "epid": 1035,
              "productId":100}
OrderConfig = {
    "functionName": "鲁班土建（企业）BIM应用套餐",
    "packageType": 12,
    "username": 'xushenwei'
}
"""