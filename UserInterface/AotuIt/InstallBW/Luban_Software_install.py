#！ python3
# -*- coding:utf-8 -*-
'''
Title: Luban Software Install
Description: Install & Uninstall Luban Software
@author: Xushenwei
@update: 2018/5/23
'''

import configparser, sys, shelve
from time import sleep
from basic_functions.common_function import verifySystemMetrics, get_base_dir, copy_config
from basic_functions.autoit_function import MouseControl, ProcessControl
from tkinter import *
from autoit import *


class InstallLubanSoftware(object):


	def __init__(self, command):
		"""读取配置文件"""
		config = configparser.ConfigParser()
		#config中read函数使用with语句，为上下文管理协议，自带打开和关闭
		config.read("Config.ini")
		# 读取安装包所在地址
		path = config.get('parameters', r'path')
		self.path = path + command + ".exe"
		self.InstallProcess =  command+".exe"

	def start(self):
		"""打开安装文件"""
		#检查屏幕分辨率是否适合该脚本
		if verifySystemMetrics(1920,1080) == True:
			pass
		else:
			raise Exception("分辨率不为1920*1080，请更改分辨率")

		#初始化安装环境
		processes = [ProcessControl('PDSShell.exe'), 
							ProcessControl('Luban Works.exe'),
							ProcessControl('Luban Works (Personal).exe'),
							ProcessControl('LubanPlan.exe'),
							ProcessControl('Luban Plan (Personal).exe'),
							ProcessControl('Luban Explorer.exe'), 
							ProcessControl('Luban Explorer（Civil）.exe'),
							ProcessControl('LubanGovern.exe'),
							ProcessControl('LubanCo.exe'),
							ProcessControl('BimIm.exe'),
							ProcessControl(self.InstallProcess)]
		for process in processes:
			if process.exists():
				process.close()
			else:
				pass
		sleep(2)

		#打开安装文件
		try:
			run(self.path)

		except Exception as e:
			print(e)
			print("软件安装路径有误，或者软件安装路径中有中文，/nstart_APP函数中path变量前需要加r！")
		sleep(2)

	def uninstall(self):
		"""卸载过程"""
		win_wait_active("[CLASS:#32770]")
		InstallWin = win_get_title("[CLASS:#32770]")
		text_all = win_get_text(InstallWin)
		text_part = ("删除程序")
		if text_part in text_all:
			win_wait_active(InstallWin, timeout=30, text="删除程序")
			sleep(1)
			m1 = MouseControl()
			m1.click(InstallWin , '', 1080, 765)
			# 个人版的会弹一个确定删除的框
			"""
			win_wait_active(InstallWin, timeout=30, text="是否要完全除去所选应用程序及其所有功能？")
			text1_all = win_get_text(InstallWin)
			text1_part = ('是否要完全除去所选应用程序及其所有功能？')
			if text1_part in text1_all:
				m1.click(InstallWin, '', 970, 590)
			"""
			win_wait_active(InstallWin, timeout=30, text="卸载完成")
			# 有时会出现重启计算机的页面，应防止自动重启计算机
			
			text2_all = win_get_text(InstallWin)
			text2_part = ("是，立即重新启动计算机。")
			if text2_part in text2_all:
				m1.click(InstallWin, '', 900, 550)
			
			m1.click(InstallWin , '', 1080, 765)
			sleep(3)
		else:
			win_kill(InstallWin)
			#当强行杀掉安装程序的时候，会弹出这个选择框
			win_wait_active('退出安装', timeout=30)
			sleep(1)
			m2 = MouseControl()
			m2.click('退出安装', '', 930, 600)
			sleep(3)

	def install(self):
		"""安装过程"""
		win_wait_active("[CLASS:#32770]")
		InstallWin = win_get_title("[CLASS:#32770]")
		win_wait_active(InstallWin, timeout=30, text="欢迎使用")
		m1 = MouseControl()
		m1.click(InstallWin, '', 1080, 760)
		win_wait_active(InstallWin, timeout=30, text="许可证协议")
		m1.click(InstallWin , '', 940, 680)
		for i in range(4):
			m1.click(InstallWin , '', 1080, 760)
			sleep(0.5)
		win_wait_active(InstallWin, timeout=30, text="完成")
		#BE会出现让安装鲁班协同的选项，取消勾选
		text_all = win_get_text(InstallWin)
		text_part = ('安装鲁班协同')
		if text_part in text_all:
			m1.click(InstallWin, '', 890, 520)
		sleep(1)
		m1.click(InstallWin , '', 1080, 760)
		sleep(3)


if __name__ == '__main__':

	def buttonClick():
		command = entry.get()
		ILS = InstallLubanSoftware(command)
		ILS.start()
		ILS.uninstall()
		ILS.start()
		ILS.install()
		install.destroy()

	install = Tk()
	install.title('Install Luban Software')
	install.configure(bg='white')#背景颜色
	install.maxsize(300,120)
	install.minsize(300,120)
	install.geometry("300x120+750+300")#大小300x300，位置（150,150）
	label = Label(install, text="INSTALL PATH", bg='white')
	entry = Entry(install, bg='gray')
	button = Button(install, text="START", command=buttonClick, bg='white')

	label.pack(side='top')
	entry.pack()
	button.pack(side='bottom')

	install.mainloop()