# Python的基础知识

## Python的数据结构（int、str、float、list、bool、tuple、dict、set）

### 1.列表,元组和字符串

#### 列表（元组）属性

#### list1 = ['a', 1, 'c', 2]

序列索引

    list1[0] = 'a', list1[-1] = 2

使用切片功能来访问特定范围内的元素,切片也是可以被赋值的

    list1[2:4] = [1, 'c'], list1[-3:] = [1, 'c', 2], list1[:2] = ['a', 1]

复制了一个list1列表

    a = list1[:]

想每隔几个元素取一个元素的话，就需要使用步长了

    list1[::2] =['a', 'c']

序列是可以拼接的，但是列表和字符串是不能拼接的

    list1 + [1,2,3] = ['a', 1, 'c', 2, 1, 2, 3]

序列中可以检查成员资格，使用关键字 in 

    'a' in list1 = True

序列中可以使用max、min、len关键字来获取列表的最大值、最小值以及列表的长度

使用list关键字可以用字符串来创建列表

    a = list('Hello')

使用join关键字可以把列表组成字符串

    '*'.join([1,2,3,4,5]) = '1*2*3*4*5'

根据列表的下标来更改列表的值,记住不能给不存在的下标赋值

    list1[2] = 3 ,list1 = ['a', 3, 'c', 2]

使用del关键字根据列表下标来删除列表中的元素
    
    del list1[1]

#### 列表（元组）方法

1.将一个对象放入列表末尾：

    list1.append('a')

2.就地清空列表：

    list1.clear()

3.复制列表，生成一个新的列表：

    list2 = list1.copy()

4.计算指定元素在列表中出现了多少次：

    list1.count(1)

5.扩展列表：

    list1.extend(list2)

6.查找指定值第一次在列表中出现的下标：

    list1.index(1)

7.将一个对象插入列表：

    list1.insert(3, 'four') 在列表第四个位置插入'four'

8.从列表中取出一个值：

    list1.pop() = 2, pop方法可以传参，代表从某个位置取值，不传参数默认从列表末尾取值

9.删除第一个为指定值的元素：

    list1.remove('c')

10.对列表进行就地排序，使用sort方法，该方法可接受两个参数key和reverse：

    list1.sort(key=len, reverse=True)

11.按照相反的顺序排列列表中的元素：

    list1.reverse()

#### 字符串方法

#### stc = "With a moo-moo here, and a moo-moo there"

1.通过在两边填充字符，让字符串居中：

    stc.center()

2.在字符串中查找子串，未找到则返回-1：

    stc.find('and')

3.合并列表中的字符串，无法合并int类型：

    list1.join()

4.返回字符串的小写版本：

    stc.lower()

5.返回字符串的大写版本：

    stc.title()

6.将指定子串替换为另一个字符串：

    stc.replace('moo','ddo')

7.将字符串拆分为列表：

    stc.split()

8.将字符串的开头和结尾的空格删除：

    stc.strip()

9.单字符转化，translate。在转化以前需要先创建转化表

    table = str.maketrans('oo', 'dd', 'and') 依次为被替换掉的字符，需替换的字符，需删除的字符

    stc.translate(table)

### 2.字典

    dict1 = {
		'Alice' : '2341',
		'Beth' : '9201',
		'Cecil' : '3258'
        }

#### 1.字典属性

1.直接使用列表创建字典，使用dict关键字方法：

    a = dict([(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')])

2.使用len来查询字典中项的个数：

    num = len(dict1)

3.返回字典中的所对应键的值：

    ID = dict1['Beth']

4.修改字典中所对应键的值：

    dict1['Beth'] = '1111'

5.删除字典中所对应键的项：

    del dict1['Beth']

6.检查字典中是否存在所对应键的项：

    return 'Beth' in dict1

#### 2.字典方法

1.删除字典所有项：

    dict1.clear()

2.浅复制：

    dict2 = dict1.copy()

3.深复制：

    from copy import deepcopy
    
    dict2 = deepcopy(dict1)

4.创建一个新字典，其中包含指定的键和默认值,第一个传参的列表是即将创建字典的键，第二个传参是即将创建字典的默认值：

    dict2 = dict.fromkeys(['name', 'age'], 'something')

5.获取字典中指定键所对应的值

    ID = dict1.get('Beth')

6.返回一个包含字典所有项的列表

    list1 = dict1.items()

7.返回一个字典视图，包含指定字典中的键

    dict1.keys()
    
8.返回一个字典视图，包含指定字典中的值

    dict1.values()

9.从字典中取出一个与指定键相关联的值

    dict1.pop('Beth')

10.从字典中随机弹出一个字典项

    dict1.popitem()
    
11.使用一个字典的项来更新另一个字典

    dict1.update(dict2)
    
### 3.赋值魔法

1.序列解包

    # 可同时（并行）给多个变量赋值
    
    x, y, z = 1, 2, 3
    
    x, y = y, x
    
    # 序列解包字典
    
    dict1 = {1:'a', 2:'b'}
    
    key, value = dict1.popitem()
    
    print(key,value)
    
    # 可以使用星号运算符（*）来收集多余的值，这样无需确保值和变量的个数相同
    
    name = "Albus Oercival Wulfric Brain Dumbledore"
    
    first, *middle, last = name.split()
    
    print(middle)
    
2.链式赋值

    x = y = 2
    
3.增强赋值

    x += 1
    
### 4.循环

1.while循环

    x = 2
    
    while x <= 100:
        
        print(x)
        
        x **= 2
        
    name = 'xushenwei'
    
    while not name:
        
        name = input('Please enter your name: ')
        
    print(f"Hello,{name}!")
    
2.for循环

    words = ['this', 'is', 'an', 'ex', 'parrot']
    
    for word in words:
    
        print(word)
        
3.跳出循环

    break
    
4.结束当前循环，并跳到下一次循环开头执行

    continue
    
5.while True/break成例

    while True:														#循环永不结束
    
	word = input('Please enter a word: ')			
	
	if not word:													#如果没有输入word的话，就跳出循环
	
		break
		
	print('The word was ', word)
	
6.if...elif...else判断语句

    from math import sqrt
    
    for n in range(99, 81, -1):
    
        root = sqrt(n)
        
        if root == int(root):
        
            print(n)
            
            break
            
    else:
    
        print('Do not find it.')
        
7.简单推导，从其他列表创建列表

    list(x * x for x in range(10))
    
    list(x * x for x in range(10) if x % 3 == 0)
    
    list((x, y) for x in range(3) for y in range(3))
    
8.pass、del、exec三人行

1.pass的作用是一个占位符，意为什么都不做

2.del的作用是删除对象

    x = 1
    
    def x
    
    print(x)
    
3.exec的作用是将字符串作为代码执行

    exec("print('Hello, world!')")
    
4.eval是一个类似于exec的内置函数，用字符串表示python表达式的值

    eval(input("Enter an artithmetic expression: "))
    
### 5.抽象

1.*args表示收集参数，返回的是一个列表；**kargs表示收集关键字参数，返回的是一个字典

    def printArgs(*args,**kargs):
    
        print(args)
        
        print(kargs)
        
    printArgs(('This is a string.', 'This is another string', a=34, t='a', v='c')
    
2.分配参数,使用运算符*来实现

    def add(x,y):
    
        return x + y
        
    params = (1,2)
    
    print(add(*params))
    
3.重新关联全局变量（使其指向新值）。在函数内部给变量赋值时，该变量默认为局部变量，除非你明确的告诉Python他是全局变量。

    x =1
    
    def change_global():
    
        global x
        
        x = x + 1
        
    change_global()
    
    print(x)
    
4.作用域嵌套，Python函数可以嵌套，及可将一个函数放在另一个函数内，作用是可以使用一个函数来创造另一个函数

    def multiplier(factor):
    
	    def mulitiplyByFactor(number):
	
		    return number * factor
		    
	    return mulitiplyByFactor
	    
    # 像multiplyByFactor这样存储其所在作用域的的函数称之为闭包
	    
    double = multiplier(2)
    
    print(double(5))
    
    triple = multiplier(3)
    
    print(triple(5))
    
    print(multiplier(4)(5))
    
5.递归：基线条件+递归条件

    # 计算阶乘
    
    def factorial(n):
        
        # 递归做法
        
        if n == 1:
        
            return 1
            
        else:
        
            return n * factorial(n-1)
            
    def factorial(n):
    
        # 循环做法
    
        result = n
        
        for i in range(1,n):
            
            result *= i
            
        return result
        
6.lambda表达式：

    seq = ["foo", "x41", "?!!", "***"]

    print(list(filter(lambda x: x.isalnum(), seq)))
    
7.reduce

    from functools import reduce
    
    a = reduce(lambda x, y: x + y, seq)
    
    print(a)
    
### 6.开箱即用模块

#### 1.sys

    sys.path.append("filepath")

#### 2.os

os模块

#### 3.time

time模块

#### 4.random

random模块

#### 5.re

re模块

