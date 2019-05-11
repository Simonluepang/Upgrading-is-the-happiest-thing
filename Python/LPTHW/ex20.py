#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from sys import argv
scrpt, input_file = argv    # 传参解包

def print_all(f):
    """
    打印所有读取的内容
    :param f: 需要读取的文件
    :return: 打印出文件内的内容
    """
    print(f.read())

def rewind(f):
    """
    讲文件游标移动到文件头的位置,若没有这一步，文件游标将从最后一行开始
    :param f:需要读取的文件
    :return:无
    """
    f.seek(16)

def print_a_line(line_count, f):
    """
    逐行打印出该行内容，行数，以及现在光标的位置
    :param line_count:需要打印的行数
    :param f:被读取的文件
    :return:无
    """
    print(line_count, f.readline(), f.tell())   # readline方法是逐行读取，然后光标停止在被读取的最后一个位置

current_file = open(input_file)

print("First let's print the whole file: \n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)


# python ex20.py test.txt
