#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from sys import argv
# 导入sys模块中的argv函数
script, filename = argv
# 运行时需要添加脚本名称和文件名称

txt = open(filename)
# 实例化读取文件
print("Here's your file %r:" % filename)
# 打印出文件的名称
print(txt.read())
# 打印出文件的内容
txt.close()
# 处理完文件以后需要进行关闭操作
print("Type the filename again:")
file_again = input("> ")
# 让用户输入再次打印文件内容的文件名称
txt_again = open(file_again)
# 实例化再次读取文件
print(txt_again.read())
txt_again.close()
# 打印出第二次读取的文件内容