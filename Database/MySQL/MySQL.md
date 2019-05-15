### [Python 如何连接MySQL数据库操作](https://github.com/Simonluepang/Upgrading-is-the-happiest-thing/blob/master/Database/MySQL/test_PyMySQL.py)

### [插入大数据，30万条数据](https://github.com/Simonluepang/Upgrading-is-the-happiest-thing/blob/master/Database/MySQL/bigTest.py)
--
使用MySQL语句中的多行插入,并且使用python中的协程

1.使用pymysql多行插入（提高效率）--pymsql.connect.().cursor().executemany(sql,datalist)

2.使用python协程（遇到I/O操作就切换任务，无需等待，提高效率）gevent.spwan + gevent.joinall

可以做到8s插入30w条数据

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
    
    create table tableName (字段名1 varchar(20)，字段名2 int(20)，...）；
    
    
查看表单
    
    show tables;
    
删除表单

    drop table tableName;
    
表插入数据

    insert into tableName (字段名1，字段名2) values (值1,值2),(值11,值22）;
    
表查询数据

    select 字段名 from 表单名 where 条件 limit 数据范围
    
删除表中数据

    delete from 表名 where 条件
    
修改表中数据

    update 表名 set 字段名='新值' where 条件
    
