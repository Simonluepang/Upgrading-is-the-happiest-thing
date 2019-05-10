#coding=utf-8
import os

Config = {
    "mainUrl":"http://www.myluban.com/myluban",
    "user": '15800968817',
    "pwd" : "d82d3131e87c04392f8f129e7c9ad73d",
    'PerformanceStatistics': 10,
}


root = os.path.dirname(os.path.abspath(__file__))
Path = {
    "cookieRoot":root + os.sep + "Data" + os.sep + "cookie.txt",
    "Data": root+os.sep+"Data"+os.sep+"Value"+os.sep,
    "globalParams": root + os.sep + "Data" + os.sep + "globalParams.txt",
    "swagger": root+os.sep+"swagger",
    'Logging': root + os.sep + "loggingReport" + os.sep,
    'InterfacePerformance':root + os.sep + "Data" + os.sep+'InterfacePerformance'+os.sep,
    'APICoverageRate': root + os.sep + "Data" + os.sep+'APICoverageRate.csv'


}


MySQLDB = {
    'LOCAL':{
            'host' : '192.168.3.75',
            'port' : '3306',
            'user' : 'center',
            'password' : 'center123',
            'database' : 'builder_bv5.5'
    },
    'REL':{
            'host' : '192.168.3.75',
            'port' : '3306',
            'user' : 'center',
            'password' : 'center123',
            'database' : 'builder_bv5.5',
            'charset' : 'latin1'
    },
    'PROD':{
            'host' : '192.168.3.75',
            'port' : '3306',
            'user' : 'center',
            'password' : 'center123',
            'database' : 'builder_bv5.5',
            'charset' : 'latin1'
    }

}
