Python 如何连接MySQL数据库操作
==

```python
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","username","password","DataBaseName")

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
```

视图和表的区别
--
* 表是物理存在的，可以对表进行update、insert、delete等操作来修改表中的数据

* 视图是虚拟的内存表，只是一个或多个表依照某个条件组合而成的结果集，只能对视图进行select操作

cmd中操作MySQL
--
进入mysql

    mysql -hlocalhost -uroot -p
    
新建数据库

    create database dbName;

查看数据库

    show databases;
    
删除数据库

    drop database dbName;
    
连接数据库

    use dbName;
    
创建表单
    
    create table tableName (字段名1，类型1，字段名2，类型2，...）；
    
查看表单
    
    show tables;
    
删除表单

    drop table tableName;
    
表插入数据

    insert into tableName (字段名1，字段名2) values (值1,值2),(值11,值22）
    
表查询数据

    select 字段名 from 表单名 where 条件 limit 数据范围
    
删除表中数据

    delete from 表名 where 条件
    
修改表中数据

    update 表名 set 字段名='新值' where 条件