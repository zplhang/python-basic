# -*- coding: utf-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect('localhost', 'root', 'zpl', 'testdb')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute()方法执行sql语句

#  更新语句
sql = 'UPDATE employee SET age = age + 1 WHERE sex = "M"'
	
try:
	# 执行sql语句
	cursor.execute(sql)
	# 提交执行
	db.commit()
except:
	# 发生错误时回滚
	db.rollback()

# 关闭数据库连接
db.close()