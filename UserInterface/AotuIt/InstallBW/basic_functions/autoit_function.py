#! python3
# -*- coding:utf-8 -*-
'''
Title: AutoIt封装类
Description: 进程、鼠标、窗口相关操作
@author: Xushenwei
@update: 2018年1月26日
'''
import autoit
# 编写一个新类，重载autoit的类，用以定制自己的功能

class ProcessControl(object):
	"""进程相关操作"""

	def __init__(self, processName):
		"""构建函数，使得所有下面的函数都使用processName"""
		self.processName = processName
		pass

	def close(self):
		"""终止进程"""
		return autoit.process_close(self.processName)

	def exists(self):
		"""检查指定进程是否存在"""
		return autoit.process_exists(self.processName)

	def wait(self, timeout=0):
		"""在指定时间以后检查进程是否存在"""
		return autoit.process_wait(self.processName, timeout=timeout)


class MouseControl(object):
	"""鼠标相关操作"""

	def __init__(self):
		pass

	def click(self, title, text, x, y, button="main", clicks=1):
		"""鼠标点击"""
		pos = autoit.win_get_pos(title, text=text)
		'''
		win_get_pos()为获取指定窗口的坐标位置和大小
		[0]X坐标
		[1]Y坐标
		[2]宽度
		[3]高度
		'''
		#autoit.mouse_click(button, x + pos[0], y + pos[1], clicks=clicks)
		autoit.mouse_click(button, x, y, clicks=clicks)

	def move(self, title, text, x, y):
		"""移动鼠标指针"""
		pos = autoit.win_get_pos(title, text=text)
		#autoit.mouse_move(x + pos[0], y + [pos][1])
		autoit.mouse_move(x, y)

	def drag(self, title, text, x1, y1,x2, y2):
		"""鼠标拖拽"""
		pos = autoit.win_get_pos(title, text=text)
		autoit.mouse_click_drag(x1, y1, x2, y2)
		#autoit.mouse_click_drag(x1 + pos[0], y1 + [pos][1], x2 + pos[0], y2 + [pos][1])

	def wheel(self, direction="up"):
		"""鼠标滚轮"""
		autoit.mouse_wheel(direction)


class WinControl(object):
	"""窗口相关操作"""

	def __init__(self, title, text=''):
		"""构造函数初始化"""
		self.title = title
		self.text = text

	def activate(self):
		"""激活指定的窗口"""
		return autoit.win_activate(self.title, text=self.text)

	def close(self):
		"""关闭指定窗口"""
		return autoit.win_close(self.title, text=self.text)

	def exists(self):
		"""检查指定窗口是否存在"""
		return autoit.win_exists(self.title, text=self.text)

	def getPos(self):
		"""获取指定窗口的坐标位置和大小"""
		return autoit.win_get_pos(self.title, text=self.text)

	def getProcess(self):
		"""获取指定窗口关联的进程ID"""
		return autoit.win_get_process(self.title, text=self.text)

	def getText(self, buf_size=256):
		"""获取指定窗口中的文本"""
		return autoit.win_get_text(self.title, buf_size, text=self.text)

	def kill(self):
		"""强行关闭指定窗口"""
		return autoit.win_kill(self.title, text=self.text)

	def move(self, x, y, width, height):
		"""移动指定的窗口或调整窗口的大小"""
		return autoit.win_move(self.title, x, y, width,height, text=self.text)

	def setState(self, flag):
		"""显示，最小化，最大化，还原窗口"""
		return autoit.win_set_state(self.title, flag, text=self.text)

	def wait(self, timeout=5):
		"""暂停脚本的执行直至指定窗口出现为止"""
		return autoit.win_wait(self.title, timeout, text=self.text)

	def waitActive(self, timeout=5):
		"""暂停脚本的执行直至指定窗口被激活"""
		return autoit.win_wait_active(self.title, timeout, text=self.text)

	def waitClose(self, timeout=5):
		"""暂停脚本的执行直至指定窗口不存在了为止"""
		return autoit.win_wait_close(self.title, timeout, text=self.text)

	def waitNotActive(self, timeout=5):
		"""暂停脚本的执行直至窗口不是激活状态为止"""
		return autoit.win_wait_not_active(self.title, timeout, text=self.text)

	def controlClick(self, control, button="main", clicks=1):
		"""向指定控件发送鼠标点击命令"""
		return autoit.control_click(self.title, control, text=self.text, button=button, clicks=clicks)

	def controlCommand(self, control, command, extra="", buf_size=256):
		"""向指定控件发送命令"""
		return autoit.control_command(self.title, control, command, buf_size, text=self.text, extra=extra)

	def controlListView(self, control, command, extra1, extra2="", buf_size=256):
		"""向指定的ListView32控件发送命令"""
		return autoit.control_list_vire(self.title, control, command, buf_size, text=self.text, extra1=extra1, extra2=extra2)

	def controlDisable(self, control):
		"""使控件变为灰色不可用状态"""
		return autoit.control_disable(self.title, control, text=self.text)

	def controlEnable(self, control):
		"""使控件从灰色不可用状态变为可用状态"""
		return autoit.control_enable(self.title, control, text=self.text)

	def controlFocus(self, control):
		"""设置输入焦点到指定窗口的空间上"""
		return autoit.control_focus(self.title, control, text=self.text)

	def controlGetText(self, control):
		"""获取控件上的文本"""
		return autoit.control_get_text(self.title, control, text=self.text)

	def controlSend(self,control, send_text, mode=0):
		"""向指定控件发送字符串"""
		return autoit.control_send(self.title, control, send_text, mode, text=self.text)

	def controlSetText(self, control, control_text):
		"""修改指定控件的文本"""
		return autoit.control_set_text(self.title, control, control_text, text=self.text)

	def controlTreeView(self, control, command, extra, buf_size=256):
		"""发送命令到TreeView32控件"""
		return autoit.control_tree_view(self.title, control, command, text=self.text, buf_size=buf_size, extra=extra)

	def statusbarGetText(self, part=1, buf_size=256):
		"""获取标准状态栏控件的文本"""
		return autoit.statusbar_get_text(self.title, self.text, part, buf_size)


		