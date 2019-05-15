### [Python 如何连接MySQL数据库操作]()

### [Python 如何连接Oracle数据库操作]()

### [插入大数据，30万条数据](https://github.com/Simonluepang/Upgrading-is-the-happiest-thing/blob/master/bigTest.py)
--
使用MySQL语句中的多行插入,并且使用python中的协程

1.使用pymysql多行插入（提高效率）--pymsql.connect.().cursor().executemany(sql,datalist)

2.使用python协程（遇到I/O操作就切换任务，无需等待，提高效率）gevent.spwan + gevent.joinall

可以做到8s插入30w条数据

视图和表的区别
--
* 表是物理存在的，可以对表进行update、insert、delete等操作来修改表中的数据

* 视图是虚拟的内存表，只是一个或多个表依照某个条件组合而成的结果集，只能对视图进行select操作

子查询
--
就是内部查询，就是查询中嵌套查询

SELECT中，FROM后，WHERE中


    # 列出各门课程成绩最好的 2 位学生， 要求显示字段: 学号，姓名, 科目，成绩
    
    SELECT t1.id, a.name, t1.kemu,t1.score
    
    FROM grade t1, student a
    
    WHERE
    
     (SELECT count(*) FROM grade t2 
     
     WHERE t1.kemu=t2.kemu AND t2.score>t1.score
     
     )<2
     
    and a.id = t1.id
    
    ORDER BY t1.kemu,t1.score 
    
    DESC

分页查询
--

使用limit关键字来进行分页查询

    在表单中从第2000条数据向后查询1000条数据
    
    select * from tableName where a = condition limit 2001,1000

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
    
