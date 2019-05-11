#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from sys import argv

# 参数解包，将argv解包。把argv中的东西解包，将所有参数一次赋予左边的变量名
script,first,second,third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variabel is:", third)


"""
在cmd中运行该文件，并赋予三个参数
python Part13.py Lemon Apple Banana
"""