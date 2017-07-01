#!python
# -*-coding:utf-8 -*-

# 导入socket模块
import socket

# 创建socket对象
s = socket.socket()

#获取本地主机名
host = socket.gethostname()

# 设置端口
port = 12345

# 绑定端口
s.bind((host, port))

# 监听并等待客户端连接
s.listen(5)
while True:
	# 建立客户端连接
	c, addr = s.accept()
	print '连接地址：', addr
	c.send('欢迎访问python教程。')
	# 关闭连接
	c.close()