#!python
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi, cgitb

# 创建FieldStorage的实例
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print "Content-type:text/html"
print
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>python教程 CGI获取数据 测试程序。</title>'
print '</head>'
print '<body>'
print '<h2>%s的网址是：%s</h2>' % (site_name, site_url)
print '</body>'
print '</html>'