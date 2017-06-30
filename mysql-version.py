
# -*- coding: utf-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect('localhost', 'root', 'zpl', 'testdb')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute()方法执行sql语句
cursor.execute('select version()')

# 使用fetchone()方法获取一条数据
data = cursor.fetchone()

print 'Database version: %s' % data

# 关闭数据库连接
db.close()