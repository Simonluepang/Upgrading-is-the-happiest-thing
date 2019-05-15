#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "username", "password", "DataBaseName")

# 使用cursor方法获取游标
cursor = db.cursor()

# 编写SQL语句
sql = "select * from tablename where condition"

try:
    # 执行语句
    cursor.execute(sql)
    # 获取表单内容
    results = cursor.fetchall()
    for row in results:
        row0 = row[0]
        row1 = row[1]
        print(f"{row0}+{row1}")
except:
    raise Exception("Error: unable to fetch data")

db.close()