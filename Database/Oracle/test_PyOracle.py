#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cx_Oracle                                          #引用模块cx_Oracle

'''SELECT'''
conn=cx_Oracle.connect('load/123456@localhost/ora11g')    #连接数据库
c=conn.cursor()                                           #获取cursor
x=c.execute('SELECT sysdate FROM dual')                   #使用cursor进行各种操作
x.fetchone()
c.close()                                                 #关闭cursor
conn.close()                                              #关闭连接

'''INSERT'''
conn=cx_Oracle.connect('load/123456@loaclhost/ora11g')
c=conn.cursor()
x=c.execute('insert into demo(v) values(:1)',['nice'])
conn.commit();
c.close()
conn.close()

