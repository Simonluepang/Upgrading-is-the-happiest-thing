#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 运行测试用例并发送生成的测试用例报告
Description: 
@author: Xushenwei
@update: 2018年6月11日
'''
from HTMLTestRunner import HTMLTestRunner
import email.mime.text
from email.mime.multipart import MIMEMultipart
from email.header import Header
from selenium import webdriver
import smtplib, unittest, time, os, sys


def common_path(path, npos):
	n1 = path.find(npos)
	BASE_DIR = path[0:n1]
	return BASE_DIR

def browser():
	path = os.path.dirname(__file__)
	npos = 'IMTestScript'
	APPLICATION_PATH = common_path(path=path, npos=npos) + r'IMTestScript\Client\x64_vc11_unicode_release\BimIM.exe'
	options = webdriver.ChromeOptions()
	options.binary_location = APPLICATION_PATH
	driver = webdriver.Chrome (chrome_options=options)
	handles = driver.window_handles
	driver.switch_to.window(handles[-1])
	os.popen('TASKKILL/F /IM ZY.Downloader.exe')
	return driver


# ==========定义发送邮件===========
def send_mail(file_new):

	f = open(file_new, 'rb')
	mail_body = f.read()
	f.close()

	# 找到最新的测试报告
	sendfile = open(file_new, 'rb').read()

	att = email.mime.text.MIMEText(sendfile, 'base64', 'utf-8')
	att["Content-Type"] = 'application/octet-stream'
	att["Content-Disposition"] = 'attachment; filename="report.html"'

	# 上传测试报告附件
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = Header("Report",'utf-8')# 主题不能有test字样，否则会被认为是垃圾邮件
	msgRoot.attach(att)

	msgRoot['from'] = 'xushenweitest@126.com'
	msgRoot['to'] = '13939201399@163.com'

	smtp = smtplib.SMTP()
	smtp.connect("smtp.126.com")
	smtp.login("xushenweitest@126.com", "xu13939201399")
	smtp.sendmail("xushenweitest@126.com","13939201399@163.com", msgRoot.as_string())
	smtp.quit()
	print('email has send out!')
	
# ==========查找测试报告目录，找到最新生成的测试报告文件==========
def new_report(testreport):
	lists = os.listdir(testreport)
	lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
	file_new = os.path.join(testreport, lists[-1])
	return file_new


if __name__ == '__main__':
	
	#为防止每次新开机第一次运行脚本时会出现打不开的情况，故先try一下browser，不管成功与否后面都可以正常运行
	try:
		dr = browser()
		dr.quit()
	except Exception as e:
		print(e)
		dr.quit()

	discover = unittest.defaultTestLoader.discover('./IM_Test/test_case', pattern='test_*.py')
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './IM_Test/report/' + now + 'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp, title='Center自动化测试报告', description='环境：Windows7-64x 浏览器：Chrome')
	runner.run(discover)
	fp.close()
	
	file_path = new_report('./IM_Test/report')

	#send_mail(file_path)
