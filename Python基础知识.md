# Python的基础知识

## Python的数据结构（int、str、float、list、bool、tuple、dict、set）

### 1.列表,元组和字符串

#### 列表（元组）属性

    list1 = ['a', 1, 'c', 2]

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

    import sys
    
    sys.path.append("filepath")

#### 2.os

os模块

#### 3.time

time模块

#### 4.random

    import random
    
    # 返回一个0~1（含）的随机实数
    
    random.random()
    
    # 返回一个(a,b]范围内的随机实数
    
    random.uniform(a,b)
    
    # 从给定序列中随机（均匀）地选择一个元素
    
    random.choice()
    
    # 随机地打乱一个可变序列中的元素，并确保每种可能的排列顺序出现的概率相同数
    
    random.shuffle()
    
    # 从给定序列中随机（均匀）地选择指定数量的元素，并确保所选择元素的值各不相同
    
    random.sample()
    
    

#### 5.re

##### 1.正则表达式

1.1 通配符：“.”，一个通配符只与一个字符匹配，例如'.ython'与'python'匹配但是不与'pjython'匹配

1.2 特殊字符转义“\\”,例如'python\\.org'只与'python.org'匹配

1.3 与在方括号内的字符都匹配，例如'[pj]ython'与'python'和'jython'都匹配，但不与其他字符串匹配。

1.4 要指定排除字符集，可在字符集的开头添加一个^字符，例如'[^abc]'与除a、b和c外的其他任何字符都匹配。

1.5 使用管道符实现二选一和子模式，例如'python|perl'，'p(ython|erl)'都只能与'python'或者'perl'匹配

1.6 在子模式后面加上问号，可将其指定为可选的，即可包含可不包含。例如r'(http://)?(www\.)?python\.org'可以与以下字符串做匹配

    'http://www.python.org' 
    
    'http://python.org' 
    
    'www.python.org' 
    
    'python.org'
    
1.7 指定字符串的开头和结尾，'^'和'$'

##### 2.re模块

    # 创建一个包含正则表达式的字符串对象
    
    r1 = re.compile(r'string')
    
    # 在给定字符串中查找第一个与指定正则表达式匹配的子串
    
    if re.search(pat, string): 
        
        print('Found it!')
        
    # 尝试在给定字符串开头查找与正则表达式匹配的子串
    
    re.match('p', 'python')
    
    # 根据与模式匹配的子串来分割字符串
    
    some_text = 'alpha, beta,,,,gamma delta'
    
    re.split('[, ]+', some_text)
    
    # 返回一个列表，其中包含所有与给定模式匹配的子串
    
    pat = '[a-zA-Z]+'
    
    text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
    
    re.findall(pat, text)
    
    # 从左往右将与模式匹配的子串替换为指定内容
    
    pat = '{name}'
    
    text = 'Dear {name}...'
    
    re.sub(pat, 'Mr. Gumby', text)

例如'^ht+p'与'http://python.org'和'htttttp://python.org'匹配，但与'www.http.org'不匹配

### 7.操作文件

#### 1.打开文件

    # 打开文件
    
    file = open("filepath")
    
    # 打开文件并只读
    
    file = open("filepath", 'r')
    
    # 打开文件并写入,当文件路径不存在的时候创建它
    
    file = open("filepath", 'w')
    
    # 独占写入模式，当文件已存在时引发FileExistsError异常
    
    file = open("filepath", 'x')
    
    # 写入附加模式
    
    file = open("filepath", 'a')
    
    # 二进制模式
    
    file = open("filepath", 'rb')
    
    file = open("filepath", 'wb')
    
    file = open("filepath", 'xb')
    
    file = open("filepath", 'ab')
    
    # 文本模式
    
    file = open("filepath", 'rt')
    
    file = open("filepath", 'wt')
    
    file = open("filepath", 'xt')
    
    file = open("filepath", 'at')
    
    # 读写模式
    
    file = open("filepath", 'r+')
    
    file = open("filepath", 'w+')
    
    file = open("filepath", 'x+')
    
    file = open("filepath", 'a+')
    
#### 2.使用上下文管理器with对文件进行操作

    with open("filepath", w) as file:
    
        a = file.read()
        
        b = file.readline()
        
        c = file.readlines()
        
        file.write(a)
        
        file.writelines(b+c)
        
### 8.对象魔法

#### 1.使用对象的好处

1.多态

可对不同类型的对象执行相同的操作

2.封装

对外部隐藏有关对象工作原理的所有细节

3.继承

可基于通用类创建出专用类

#### 2.私有方法，不能从外部访问

    class Secretive:

        def __inaccessible(self):
        
        # 这个是一个私有方法
        
            print("Bet you can't see me...")
    
        def accessible(self):
        
            print("The secret message is : ")
            
            self.__inaccessible()
		
#### 3.指定超类，子类扩展了超类的定义。

    class Filter:
    
	'过滤序列通用类'
	
        def init(self):
        
            self.blocked = []
    
        def filter(self, sequence):
            
            #返回一个列表，内含所有在指定序列中没有包含在self.blocked内的元素
            
            return [x for x in sequence if x not in self.blocked]

    class SPAMFilter(Filter):
    
        'Filter的子类,可过滤SPAM字符'
        
        def init(self):
        
            self.blocked[SPAM]
            
#### 4.多个超类，多重继承

    class Calculator:
    
	'使用字符串来计算'
	
        def calculate(self, expression):
        
            self.value = eval(expression)
    
    class Talker:
    
        '把计算结果说出来'
        
        def talk(self):
        
            print('Hi, my value is ', self.value)
    
    class TalkingCalculator(Calculator, Talker):
    
        '该子类本身无所作为，他的所有行为都是从超类那里继承的'
        
        '从Calculator继承计算器功能，从Talker继承说话功能'
        
        pass
        
    tc = TalkingCalculator()
    
    tc.calculate('1 + 2 *3')
    
    tc.talk()
    
####  5.抽象基类，抽象类是不能（至少不应该）实例化的类，其职责是定义子类应实现的一组抽象方法

    class Talker(ABC):
    
        @abstractmethod
        
        def talk(self):

            pass
		
	a = Talker() # 该类现在无法被实例化
	
### 9.异常

#### 1.主动引发异常

    raise Exception('hyperdrive overload')
    
    # 常见的异常类
    
    raise Exception						#几乎所有的异常类都是从他派生而来的
    
    raise ArithmeticError				#引用属性或者给他赋值失败时引发
    
    raise OsError							#操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
    
    raise IndexError						#使用序列中不存在的索引时引发，为LookupError的子类
    
    raise KeyError							#使用映射中不存在的键时引发，为LookupError的子类
    
    raise NameError						#找不到名称变量时引发
    
    raise SyntaxError						#代码不正确时引发
    
    raise TypeError						#将内置操作或函数用于类型不正确的对象是引发
    
    raise ValueError						#将内置操作或函数用于这样的对象是引发：其类型正确但是包含的值不合适
    
    raise ZeroDivisionError			#在除法或者求模运算的第二个参数为零时引发
    
#### 2.自定义异常类

    class SomeCustomException(Exception):
	    pass
	    
#### 3.捕获异常并进行处理

    x = None
    
    try:
    
        x = 1 / 0
        
    except Exception as e:
    
        print(e)
        
    finally:
    
        print('Cleaning up...')
        
        del x
        
### 10.生成器

关键字：yield，主要目的是生成值的序列

    def get_primes(number):
    
    while True:
    
        if is_prime(number):
        
            yield number
            
        number += 1
        
    def solve_number_10():
    
    # She *is* working on Project Euler #10, I knew it!
    
    total = 2
    
    for next_prime in get_primes(3):
    
        if next_prime < 2000000:
        
            total += next_prime
            
        else:
        
            print(total)
            
            return
            
### 11.常用到的python库

#### 1.处理Excel文件

    import xlrd     # 使用该库来读取Excel文件信息
    
    import xlwt     # 使用该库来生成Excel文件
    
    import xluntils # 使用该库来修改Excel文件内容
    
#### 2.处理json数据

    import json


#### 3.处理doc文件

    import docx
    
    import win32com

#### 4.处理csv文件

    import csv