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

### [MySQL相关]()

### [Oracle相关]()