serverAddress = 'http://127.0.0.1:4723/wd/hub'
desired_caps = {
	# 测试平台
	'platformName': 'Android',
	# adb devices获得
	'deviceName': 'emulator-5554',
	# 测试机的安卓版本
	'platformnVersion': '5.1.1',
	# aapt dump badging获得
	'appPackage': 'com.lubansoft.bimview4phone',
	# 'appPackage' : 'com.lubansoft.bimview4phone.entp',
	# aapt dump badging获得
	'appActivity': 'com.lubansoft.myluban.login.StartupActivity',
	# 使用Unicode编码方式发送字符串
	'unicodeKeyboard': True,
	# 屏蔽软键盘，绕过键盘输入中文
	'resetKeyboard': True,
	# 允许定位toast元素
	'automationName': 'Uiautomator2'
}

