#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from sys import argv
script, filename = argv

print("We're going to earse %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')    # 当该文件不存在的时候，会创建一个该文件
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")

for i in (line1,line2,line3):
    target.write(i + "\n")
'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
print("And finally, we close it.")
target.close()
