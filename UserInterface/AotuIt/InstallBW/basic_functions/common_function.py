#! python3
# -*- coding:utf-8 -*-
'''
Title: 公共函数
Description: 
@author: Xushenwei
@update: 2017年12月13日
'''

from win32api import GetSystemMetrics
import os,time,shutil

def verifySystemMetrics(width, height):
	"""判断屏幕分辨率是否符合要求"""
	if GetSystemMetrics(0) == width and GetSystemMetrics(1) == height:
		return True
	else:
		return False

def get_base_dir():
	"""获取脚本根目录"""
	base_dir = str(os.path.dirname(os.path.dirname(__file__)))
	base_dir = base_dir.replace("\\", "/")
	return base_dir.split('/testcase')[0]

def now():
	"""返回当前时间"""
	return time.strftime("%Y-%m-%d %H:%M:%S")

def copy_config():
	"""读取配置文件"""
	configfile = get_base_dir() + "/data/Imconfig.ini"
	shutil.copy(configfile, "C:/IMconfig.ini")
 
if __name__ == '__main__':
	print(verifySystemMetrics(1920,1080))
	print(get_base_dir())
	print(now())