# -*- coding: utf-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect('localhost', 'root', 'zpl', 'testdb')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute()方法执行sql语句

#  查询语句
sql = 'SELECT * FROM employee WHERE income > 1000'
	
try:
	# 执行sql语句
	cursor.execute(sql)
	# 获取所有记录列表
	results = cursor.fetchall()
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		sex = row[3]
		income = row[4]
		# 打印结果
		print 'fname = %s, lname = %s, age = %d, sex = %s, income = %d' % (fname, lname, age, sex, income)
except:
	print 'Error: unable to fetch data'

# 关闭数据库连接
db.close()