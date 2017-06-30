#!python
# -*- coding: UTF-8 -*-

# 导入模块
import cgi, os
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

# 获取文件名
fileitem = form['filename']

# 检查文件是否上传
if fileitem.filename:
	# 设置文件路径
	fn = os.path.basename(fileitem.filename)
	open(os.getcwd() + '/tmp/' + fn, 'wb').write(fileitem.file.read())
	
	message = '文件“' + fn + '”上传成功。'
else:
	message = '文件没有上传'

print """\
Content-type: text/html\n
<html>
<head>
<meta charset='utf-8'>
<title>python教程(www.python.com)</title>
</head>
<body>
	<p>%s</p>
</body>
</html>
""" % (message, )