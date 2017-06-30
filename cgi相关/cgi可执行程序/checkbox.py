#!python
# -*- coding: UTF-8 -*-

# 引入CGI处理模块
import cgi, cgitb

# 创建FieldStorage的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('google'):
	google_flag = "是"
else:
	google_flag = "否"
	
if form.getvalue('python'):
	python_flag = "是"
else:
	python_flag = "否"
	
print 'Content-type:text/html'
print 
print '<html>'
print '<head>'
print '<meta charset = "utf-8">'
print '<title>python教程 CGI 测试实例</title>'
print '</head>'
print '<body>'
print '<h2> python教程是否选择了：%s</h2>' % python_flag
print '<h2> Google是否选择了： %s</h2>' % google_flag
print '</body>'
print '</html>'