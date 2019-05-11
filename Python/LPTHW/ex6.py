#!/usr/bin/env python 
# -*- coding:utf-8 -*-
x = "There are %d types of people." % 10 # 把10放在%d的位置
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not) # 第一个%s放binary，第二个%s放do_not

print(x)
print(y)

print("I said: %r." % x)    # %r查找的是一个函数或者一个返回值
print("I also said: '%s'." % y)     # %r也可以在引号内但不被认为是一个字符串，而是一个变量

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)   # %r把所有的传参都转化为string类型的字符串

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)    # 字符串之间允许相加得到一个更长的字符串