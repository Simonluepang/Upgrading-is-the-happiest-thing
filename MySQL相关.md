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