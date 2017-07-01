# -*- coding: utf-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect('localhost', 'root', 'zpl', 'testdb')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute()方法执行sql语句

# 插入数据 sql语句
sql = """INSERT INTO employee (
	first_name, last_name, age, sex, income)
	VALUES ('Mac', 'Mohan', 22, 'M', 3493)"""
	
try:
	# 执行sql语句
	cursor.execute(sql)
	# 提交
	db.commit()
except:
	# 一旦出错就回滚
	db.rollback()

# 关闭数据库连接
db.close()