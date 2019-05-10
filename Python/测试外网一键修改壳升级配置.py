#使用方式：把改文件放入要升级的shell文件夹下，双击即可实现自动填写测试外网升级文件
filename0 = 'live.conf'

with open(filename0, 'a') as file_object:
	file_object.write('\n[SERVER OPTION]')
	file_object.write('\nBIMAPP SERVER=http://bim-test.lubanexpress.com')


def alter(file, old_str, new_str):
	file_data = ''
	with open(file, "r", encoding="utf-8") as f:
		for line in f:
			if old_str in line:
				line = line.replace(old_str, new_str)
			file_data += line
	with open(file, "w",encoding="utf-8") as f:
		f.write(file_data)

alter("shconfig\shellversion.ini", 'address=http://bim.myluban.com', 'address=http://bim-test.lubanexpress.com')