# -*- coding: utf-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect('localhost', 'root', 'zpl', 'testdb')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute()方法执行sql语句
# 如果数据表已经存在，先删除表
cursor.execute('DROP TABLE IF EXISTS employee')

# 创建数据表sql语句
sql = """CREATE TABLE employee (
	first_name CHAR(20) NOT NULL,
	last_name CHAR(20),
	age INT,
	sex CHAR(1),
	income FLOAT)"""
	
cursor.execute(sql)

# 关闭数据库连接
db.close()