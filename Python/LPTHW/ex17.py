#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("Copying from %s to %s" % (from_file,to_file))

# we could do these two on one line too, how?
# indata = open(from_file).read()
inputdata = open(from_file)
indata = inputdata.read()

print("The input file is %d bytes long" % len(indata))
print("Dose the output file exist? %r" % exists(to_file))   # 将文件名字符串作为参数，如果文件存在返回True，否则返回False
print("Ready, hit RETURN to continue,CTRL-C to abort.")
input()

output = open(to_file, 'w')
output.write(indata)
print("Alright, all done!")
output.close()
inputdata.close()