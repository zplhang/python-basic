#!python
# -*- coding: UTF-8 -*-

# 导入模块
import os
import Cookie

print 'Content-type: text/html'
print 

print """
<html>
	<head>
		<meta charset="utf-8">
		<title>python教程(www.python.com)</title>
	</head>
	<body>
		<h1>读取Cookie信息</h1>
"""
if 'HTTP_COOKIE' in os.environ:
	cookie_string = os.environ.get('HTTP_COOKIE')
	c = Cookie.SimpleCookie()
	c.load(cookie_string)
	
	try:
		data = c['name'].value
		print 'Cookie data: ' + data + '<br>'
	except KeyError:
		print 'cookie 没有设置或者已过去<br>'
print """
	</body>
</html>
"""