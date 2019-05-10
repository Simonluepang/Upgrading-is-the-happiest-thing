import pymysql
import gevent
import time
"""
1.使用pymysql多行插入（提高效率）--executemany
2.使用python协程（遇到I/O操作就切换任务，无需等待，提高效率）gevent.spwan + gevent.joinall
30w条数据耗时8s
"""

class MyPyMysql:
	def __init__(self):
		self.host = 'localhost'
		self.port = 3306
		self.username = 'root'
		self.password = 'xu13939201399@'
		self.db = 'dbtest'
		self.charset = 'utf8'
		self.pymysql_connect()

	def pymysql_connect(self):
		# pymysql连接MySQL数据库
		self.conn = pymysql.connect(
			host=self.host,
			port=self.port,
			user=self.username,
			password=self.password,
			db=self.db,
			charset=self.charset)
		# 连接MySQL后执行的函数
		self.asynchronous()

	def run(self,nmin,nmax):
		# 创建游标
		self.cur = self.conn.cursor()

		# 定义sql语句，插入数据
		sql = "insert into bigtest(id,value) values (%s,%s)"

		data_list = []
		for i in range(nmin,nmax):
			result = (i,f"The value is {i}.")
			data_list.append(result)

		# 执行多行插入，executemany(sql语句,数据(需要是一个元组类型的数据))
		content = self.cur.executemany(sql,data_list)
		if content:
			print('成功插入第{}条数据'.format(nmax-1))

		# 提交数据，否则数据不会保存
		self.conn.commit()

	def asynchronous(self):
		# g_l是一个任务列表
		# 定义了异步的函数，这里用到了一个gevent.spawn方法
		max_line = 10000	# 定义每次最大插入行数（max_line=10000，即一次插入10000行）
		g_l = [gevent.spawn(self.run,i,i+max_line) for i in range(1,300001,max_line)]

		# gevent.joinall方法等待所有操作都执行完毕
		gevent.joinall(g_l)
		self.cur.close()	# 关闭游标
		self.conn.close()	# 关闭pymysql连接

if __name__ == '__main__':
	start_time = time.time()	# 计算程序开始时间
	st = MyPyMysql()	# 实例化类
	print('程序耗时{:.2f}'.format(time.time()-start_time))	# 计算程序总耗时