# -*- coding:UTF8 -*-

"""
print u"你好，世界。"

if True:
	print "Answer"
	print "True"
else:
    print "Answer"
	# 没有严格缩进，在执行时会报错
    print "False"
	
# 第一个注释
print "Hello, Python." #第二个注释

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""

"""
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
"""

"""
raw_input("\n\nPress the enter key to exit.")

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

x = "a"
y = "b"
# 换行输出
print x
print y

print "-------"
#不换行输出
print x,
print y,

counter = 100 # 赋值整型变量
miles = 1000.3 # 浮点型
name = "John" # 字符串

print counter
print miles
print name

str = 'Hello World!'
print str
print str[0]
print str[2:5]
print str[2:]
print str * 2
print str + "TEST"

list = ['runoob', 4324, 2.44, 'john', 44]
tinylist = [21, 'john']
print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list + tinylist

dict = {}
dict['one'] = "this is one"
dict[2] = 'This is two'
tinydict = {'name' : 'john', 'code' : 4522, 'dept' : 'sales'}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()
"""

"""
a = 21
b = 10
c = 0

c = a + b
print u"1, c的值为：", c

c = a - b
print u"2, c的值为：", c

c = a * b
print u"3, c的值为：", c

c = a / b
print u"4, c的值为：", c

c = a % b
print u"5, c的值为：", c

# 修改变量a, b, c
a = 2
b = 3
c = a ** b
print u"6, c的值为：", c

a = 10
b = 4
c = a // b
print u"7, c的值为：", c
"""

"""
num = -3
if num == 3:
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:
    print 'error'
else:
    print 'roadman'
	
# python不支持switch语句
num = 9
if num > 0 and num <= 10:
    print 'hello'
	
count = 0
while(count < 9):
    print 'The count is:', count
    count += 1
print 'GoodBye'

i = 1
while i < 10:
    i += 1
    if i % 2 > 0: # 非双数时跳过输出
	    continue
    print i
	
i = 1
while 1:
    print i
    i += 1
    if i > 10:
        break
		
"""

"""
import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

"""

"""
# 在python中，while...else在循环条件为false时执行else语句块
count = 0
while count < 9:
    print count, 'is less than 9'
    count = count + 1
else:
    print count, 'is not less than 9'
	
for letter in 'Python':
    print '当前字母：', letter

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果是：', fruits[index]
print 'GoodBye'

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print '%d 等于 %d * %d' % (num, i, j)
            break
    else:
        print num, '是一个质数'

"""

"""
# 打印三角形、菱形、矩形
rows = int(raw_input('输入列数：'))
i = j = k = 1 # 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数

# 等腰直角三角形
print '等腰直角三角形'
for i in range(0, rows):
    for k in range(0, rows - i):
        print " * ", # 注意这里的，不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print "\n"
	
"""

"""

list = ['physics', 'chemistry', 1003, 3333]

print 'Value available at index 2: '
print list[2]
list[2] = 2000
print 'New value available at index 2: '
print list[2]

del list[2]
print 'After deleting value at value 2: '
print list

list1 = ['eew', 3, 'df']
print cmp(list, list1)

# python 3.x没有cmp函数，需要引入operator模块，适合任何对象

import time
localtime = time.asctime(time.localtime(time.time()))
print '本地时间为：', localtime

# 格式化日期
print time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

# 将格式字符串转换成时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

# 获取某月日历
import calendar
cal = calendar.month(2017, 6)
print cal

# 函数
def printme(str):
    print str
    return
	
printme("hello")
printme("function")

def reverse(li):
	for i in range(0, len(li) / 2):
		temp = li[i]
		li[i] = li[-i-1]
		li[-i-1] = temp

l = [1,2,3,4,5,6,7]
reverse(l)
print l

# raw_input和input的区别
	 # input 可以接收一个Python表达式作为输入，并将运算结果返回。
		str = input("请输入：");
		print "你输入的内容是: ", str
		请输入：[x*5 for x in range(2,10,2)]
		你输入的内容是:  [10, 20, 30, 40]
		# 如果是raw_input，结果是“[x*5 for x in range(2,10,2)]”
		
"""

"""

# fo = open("foo.txt", 'wb')
# fo.write('www.baidu.com/hahha/wefsld;flasj;glja;fjdslajdgjsal;jgdalsj\n')
fo = open('oof.txt', 'r+')
str = fo.read(10)
print '读取的内容是：', str

position = fo.tell()
print '当前文件位置：', position

# 把指针重新定位到开头
position = fo.seek(0, 0) 
	# seek(offset, from)
		# offset表示要移动的字节数
		# from表示开始移动的参考位置
			# 0: 文件开头
			# 1: 当前位置
			# 2: 文件末尾
str = fo.read(10)
print "重新获取内容：", str

fo.close()
print '文件名：', fo.name
print '是否已关闭：', fo.closed
print '访问模式：', fo.mode
print '末尾是否强制空格：', fo.softspace

import os
# 重命名文件，os.rename(filename, newname)
os.rename('oof.txt', 'foo.txt')
# 删除文件 os.remove(filename)
os.remove('oo.txt')

"""

"""
def temp_convert(var):
	try:
		return int(var)
	except ValueError, Argument:
		print '参数没有包含数字\n', Argument

print temp_convert('x')


def mye(level):
	if level < 1:
		raise Exception('Invalid Level', level)
		
try:
	mye(0)
except 'Invalid Level':
	print 1
else:
	print 2
	
class Networkerror(RuntimeError):
	def __init__(self, arg):
		self.args = arg
		
try:
	raise Networkerror("Bad hostname")
except Networkerror, e:
	print e.args
	
"""

"""
# python面向对象

class Employee:
	'所有员工的基类'
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		
	def displayCount(self):
		print 'Total employee: %d' % Employee.empCount
	
	def displayEmployee(self):
		print 'Name: ', self.name, ', Salary: ', self.salary
		
emp = Employee('a', 3333)
# emp.displayCount()
emp.displayEmployee()
empp = Employee('b', 44564)
# empp.displayCount()
empp.displayEmployee()
print 'Total employee: %d' % Employee.empCount
emp.age = 44
print getattr(emp, 'age')
emp.age = 8
print getattr(emp, 'age')

print hasattr(emp, 'name')
print hasattr(emp, 'aaa')
setattr(emp, 'address', 'China')
print getattr(emp, 'address')
delattr(emp, 'address')
print hasattr(emp, 'address')
# del emp.age
# print getattr(emp, 'age')

print Employee.__dict__
print Employee.__doc__
print Employee.__name__
print Employee.__module__
print Employee.__bases__

class Test:
	def prt(self):
		print self
		print self.__class__
		
t = Test()
t.prt()
print Test.__dict__
print Test.__doc__
print Test.__name__
print Test.__module__
print Test.__bases__

class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
		
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name, '销毁'
		
pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)
del pt1
del pt2
del pt3

class Parent:
	parentAttr = 100
	
	def __init__(self):
		print u'调用父类构造函数'
		
	def parentMethod(self):
		print '调用父类方法'
		
	def setAttr(self, attr):
		Parent.parentAttr = attr
		
	def getAttr(self):
		print '父类属性：', Parent.parentAttr
		
	def myMethod(self):
		print '调用父类方法'
		
class Child(Parent):
	def __init__(self):
		print '调用子类构造方法'
		
	def childMethod(self):
		print '调用子类方法 child method'
		
	def myMethod(self):
		print '调用子类方法'
		
c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(111)
c.getAttr()
c.myMethod()

class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	def __str__(self):
		return 'Vector (%d, %d)' % (self.a, self.b)
		
	def __add__(self, other):
		return Vector(self.a + other.a, self.b + other.b)
		
v1 = Vector(2, 10)
v2 = Vector(4, 22)
print v1 + v2

class JustCounter:
	__secretCount = 0 # 私有变量
	publicCount = 0 # 公开变量
	
	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print self.__secretCount
		
	def count2(self):
		print self.__secretCount
		
counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
# print counter.__secretCount # 报错，实例不能访问私有变量
print counter._JustCounter__secretCount # 可以使用 object._className__attrName 访问属性

try:
	counter.count2()
except IOError:
	print '不能调用非公有属性'
else:
	print 'ok'
# 单下划线、双下划线和头尾双下划线
	# __xxx__ python中特殊方法的专用标识（__init__）
	# __xxx 双下划线表示的是私有private变量，只允许本类访问，子类不可访问
	# _xxx 单下划线表示protected类型的变量，只允许本类和子类访问，不能用from module import *导入
	
"""

"""

# python正则表达式

# re.match(pattern, string, flags = 0) 从字符串起始位置匹配，如果不是起始位置匹配成功返回None
	# pattern 匹配的正则表达式
	# string 要匹配的字符串
	# flags 标志位，控制匹配方式，是否区分大小写，多行控制
		# re.I 使匹配对大小写不敏感
		# re.L 本地化识别匹配
		# re.M 多行匹配，影响^和$
		# re.S 使.匹配包括换行在内的所有字符
		# re.U 根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B
		# re.X 该标志通过给予更灵活的格式，以便将正则表达式写得更容易理解
	# re.match返回一个匹配的对象或者None
	# 可以使用匹配对象的group(num)或者groups()函数获取匹配表达式
	# start() 返回匹配开始的位置
	# end() 返回匹配结束的位置
	# span() 返回一个元组包含匹配（开始，结束）的位置
	
import re
print re.match('www', 'www.rxxers.com').span()
print re.match('com', 'www.xerexe.com')

line = 'Cats are smarter than dogs'
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
	print 'matchObj.group(): ', matchObj.group()
	print 'matchObj.group(1): ', matchObj.group(1)
	print 'matchObj.group(2): ', matchObj.group(2)
else:
	print 'Not match.'
	
# re.search(pattern, string, flags = 0) 在字符串内查找模式匹配，只要找到第一个匹配就返回，如果没有匹配返回None
	# search()与match()的区别
		# match()只匹配字符串的开始，search()匹配整个字符串，直到找到一个匹配。
		
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
	print 'match --> matchObj.group(): ', matchObj.group()
else:
	print 'Not match.'
	
matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
	print 'search --> matchObj.group(): ', matchObj.group()
else:
	print 'Not match.'
	
print re.search(r'\dcom', 'www.4comfeself.5comd').group()

a = '1234abc567'
print re.search(r'([0-9]*)([a-z]*)([0-9]*)', a).group()
print re.search(r'([0-9]*)([a-z]*)([0-9]*)', a).group(1)
print re.search(r'([0-9]*)([a-z]*)([0-9]*)', a).group(2)
print re.search(r'([0-9]*)([a-z]*)([0-9]*)', a).group(3)

# 检索替换
	# re.sub(pattern, repl, string, count = 0, flags = 0)
		# pattern 正则匹配的模式字符串
		# repl 替换的字符串，也可以是一个函数
		# string 被查找替换的原始字符串
		# count 模式匹配后替换的最大次数
		
phone = '2004-959-559 # 这是一个国外电话号码'

# 删除字符串中的python注释
num = re.sub(r'#.*$', '', phone)
print '电话号码是：', num

# 删除非数字-的字符串
num = re.sub(r'\D', '', phone)
print '电话号码是：', num

# 将匹配的数字乘以2
def double(matched):
	value = int(matched.group('value'))
	return str(value * 2)
	
s = 'A23G4Hfd567'
print re.sub(r'(?P<value>\d+)', double, s)

"""

# python CGI

#!python
# -*- coding: UTF-8 -*-

print "Content-type:text/html"
print
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>Hello World - 我的第一个CGI程序。</title>'
print '</head>'
print '<body>'
print '<h2>Hello World!!! 我是来自xxx的第一个CGI程序。</h2>'
print '</body>'
print '</html>'

# HTTP头部
	# Content-type:text/html 为HTTP头部的一部分，告诉浏览器文件的内容类型
	# CGI程序中HTTP头部经常使用的信息
		# Content-type 请求的与实体对应的MIME信息
		# Expires:Date 响应过期的日期和时间
		# Location:URL 用来重定向接收方到非请求URL的位置
		# Last-modified:Date 请求资源的最后修改时间
		# Content-length:N 请求的内容长度
		# Set-Cookie:String 设置HTTP Cookie
# CGI 环境变量
	# CONTENT_TYPE 传递来的信息的MIME类型
	# CONTENT_LENGTH 如果服务器和CGI程序信息传递方式是POST，该环境变量表示从标准输入STDIN可以读到的有效数据字节数。当读取所输入的数据时必须使用
	# HTTP_COOKIE 客户端的COOKIE内容
	# HTTP_USER_AGENT 提供包含了版本或其他专有数据的客户浏览器信息
	# PATH_INFO 紧接在CGI程序名后面的其他路径信息，常常作为CGI程序的参数出现
	# QUERY_STRING 如果服务器与CGI程序传递信息的方式是GET，这个环境变量的值就是传递的信息。这个信息紧跟在CGI程序名的后面，两者中间用“?”分隔
	# REMOTE_ADDR 发送请求的客户端的IP地址。这个值总是存在，它是Web客户端需要提供给Web服务器的唯一标识，可以在CGI程序中用它来区分不同的客户机。
	# REMOTE_HOST 包含发送CGI请求的客户机的主机名。
	# REQUEST_METHOD 提供脚本被调用的方法。对于使用HTTP/1.0协议的脚本，仅GET和POST有意义。
	# SCRIPT_FILENAME CGI脚本的完整路径
	# SCRIPT_NAME CGI脚本的名称
	# SERVER_NAME WEB服务器的主机名，别名或IP地址
	# SERVER_SOFTWARE 包含了调用CGI程序的HTTP服务器的名称和版本号
	
	# 获取环境变量
		#!python
		# -*- coding:utf-8 -*-
		
		import os
		
		print 'Content-type: text/html'
		print
		print '<meta charset="utf-8">'
		print '<b>环境变量</b><br>'
		print '<ul>'
		for key in os.environ.keys():
			print '<li><span style = "color:green"> %30s </span> : %s </li>' % (key, os.environ[key])
		print '</ul>'
		
# GET、POST方法
	# GET方法发送编码后的用户信息到服务端，数据信息包含在请求页面的URL上，以“?”分隔
		# http://www.test.com/cgi-bin/hello.py?key1=value1&key2=value2
		# 其他注释
			# GET请求可被缓存，请求保留在浏览器历史记录中，请求可被藏为书签
			# 请求不应在处理敏感数据时使用，请求有长度限制，请求只应当用于取回数据
			
		# GET方法传输数据 实例
		# /cgi-bin/test.py?name=菜鸟教程&url=http://www.runoob.com
		# hello-get.py
		
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
		
		# GET方法传输数据 表单实例
		# hello-get.html
		
		<!DOCTYPE html>
		<html>
		<head>
		<meta charset = "utf-8">
		<title>python教程（www.python.com）</title>
		</head>
		<body>
		<form action = "/cgi-bin/hello-get.py" method = "GET">
		站点名称：<input type = "text" name = "name"> <br />

		站点URL：<input type = "text" name = "url" />
		<input type = "submit" value = "提交" />
		</form>
		</body>
		</html>
		
		# POST方法
		# hello-post.html
		
		<!DOCTYPE html>
		<html>
		<head>
		<meta charset = "utf-8">
		<title>python教程（www.python.com）</title>
		</head>
		<body>
		<form action = "/cgi-bin/hello-get.py" method = "POST">
		站点名称：<input type = "text" name = "name"> <br />

		站点URL：<input type = "text" name = "url" />
		<input type = "submit" value = "提交" />
		</form>
		</body>
		</html>
		
		# CGI传递radio数据
		# hello-radio.html
		
		<!DOCTYPE html>
		<html>
		<head>
		<meta charset="utf-8">
		<title>菜鸟教程(runoob.com)</title>
		</head>
		<body>
		<form action="/cgi-bin/radiobutton.py" method="post" target="_blank">
		<input type="radio" name="site" value="runoob" /> 菜鸟教程
		<input type="radio" name="site" value="google" /> Google
		<input type="submit" value="提交" />
		</form>
		</body>
		</html>
		
		# radiobutton.py脚本
		
		#!python
		# 引入 CGI 处理模块 
		import cgi, cgitb 

		# 创建 FieldStorage的实例 
		form = cgi.FieldStorage() 

		# 接收字段数据
		if form.getvalue('site'):
		   site = form.getvalue('site')
		else:
		   site = "提交数据为空"

		print "Content-type:text/html"
		print
		print "<html>"
		print "<head>"
		print "<meta charset=\"utf-8\">"
		print "<title>菜鸟教程 CGI 测试实例</title>"
		print "</head>"
		print "<body>"
		print "<h2> 选中的网站是 %s</h2>" % site
		print "</body>"
		print "</html>"
		
		# CGI传递Textarea数据
		# hello-textarea.html
		
		<!DOCTYPE html>
		<html>
		<head>
		<meta charset = "utf-8">
		<title>python教程（www.python.com）</title>
		</head>
		<body>
		<form action = "/cgi-bin/textarea.py" method = "POST" target = "_blank">
		<textarea name = "textcontent" cols = "40" rows = "4" >
		在这里输入内容...
		</textarea>
		<input type = "submit" value = "提交" />
		</form>
		</body>
		</html>
		
		# textarea.py脚本
		
		#!python
		# -*- coding: UTF-8 -*-

		# 引入CGI处理模块
		import cgi, cgitb

		# 创建FieldStorage的实例
		form = cgi.FieldStorage()

		# 接收字段数据
		if form.getvalue('textcontent'):
			text_content = form.getvalue('textcontent')
		else:
			text_content = '没有内容'
			
		print 'Content-type:text/html'
		print 
		print '<html>'
		print '<head>'
		print '<meta charset = "utf-8">'
		print '<title>python教程 CGI 测试实例</title>'
		print '</head>'
		print '<body>'
		print '<h2> 输入的内容是：%s</h2>' % text_content
		print '</body>'
		print '</html>'
		
		# CGI传递下拉菜单数据
		# hello-dropdown.html
		
		<!DOCTYPE html>
		<html>
		<head>
		<meta charset = "utf-8">
		<title>python教程（www.python.com）</title>
		</head>
		<body>
		<form action = "/cgi-bin/dropdown.py" method = "POST" target = "_blank">
		<select name = "dropdown">
		<option value = "python" selected>python教程</option>
		<option value = "google">Google</option>
		</select>
		<input type = "submit" value = "提交" />
		</form>
		</body>
		</html>
		
		# dropdown.py脚本
		
		#!python
		# -*- coding: UTF-8 -*-

		# 引入CGI处理模块
		import cgi, cgitb

		# 创建FieldStorage的实例
		form = cgi.FieldStorage()

		# 接收字段数据
		if form.getvalue('dropdown'):
			dropdown_value = form.getvalue('dropdown')
		else:
			dropdown_value = '没有内容'
			
		print 'Content-type:text/html'
		print 
		print '<html>'
		print '<head>'
		print '<meta charset = "utf-8">'
		print '<title>python教程 CGI 测试实例</title>'
		print '</head>'
		print '<body>'
		print '<h2> 选中的选项是：%s</h2>' % dropdown_value
		print '</body>'
		print '</html>'
		
# CGI 使用Cookie
	# cookie在客户访问脚本的同时，通过客户的浏览器，在客户硬盘上写入记录数据，当下次客户访问脚本时取回数据信息，从而达到身份判别的功能
	# http cookie的发送是通过http头部实现的。早于文件的传输。
	# Set-cookie: name = name; expires = date; path = path; domain = domain; secure
		# name 设置cookie的值，name不能使用“;”和“,” 多个name用“;”分隔，如name1 = name1; name2 = name2
		# expires = date cookie的有效期限 格式“WDY, DD-Mon-YYYY HH:MM:SS”
		# path = path 设置cookie支持的路径。如果是目录，所有文件及子目录生效；如果是文件，cookie仅对这个文件生效。
		# domain = domain 对cookie生效的域名
		# secure 如果给出此标志，表示cookie只能通过SSL协议的HTTPS服务器来传递
	
	# 设置cookie
		#!python
		# -*- coding: UTF-8 -*-

		print 'Content-type: text/html'
		print 'Set-Cookie: name="Python教程"; expires="Wed, 26 Aug 2017 18:30:00 GMT"'
		print 
		print """
		<html>
			<head>
				<meta charset="utf-8">
				<title>python教程(www.python.com)</title>
			</head>
			<body>
				<h1>Cookie Set OK!</h1>
			</body>
		</html>
		"""
		
	# 检索cookie信息
		# cookie信息存储在CGI的环境变量HTTP_COOKIE中，格式为key1=value1;key2=value2...
		
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
		
# 文件上传下载
	# 文件上传实例
	
	# file-save.html
	<!DOCTYPE html>
	<html>
	<head>
	<meta charset = "utf-8">
	<title>python教程（www.python.com）</title>
	</head>
	<body>
	<form enctype = "multipart/form-data" action = "/cgi-bin/file-save.py" method = "POST" >
	<p> 选中文件：<input type = "file" name = "filename" /></p>
	<p><input type = "submit" value = "上传" /></p>
	</form>
	</body>
	</html>
	
	# file-save.py脚本
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
	
	# 文件下载实例
	#!python
	# -*- coding: UTF-8 -*-

	# HTTP头部
	print 'Content-Disposition: attachment; filename = "foo.txt"'
	print 

	# 打开文件
	fo = open('file-save.py', 'rb')
	# 相当于下载服务器上file-save.py文件的内容保存到foo.txt文件中

	str = fo.read()
	print str

	# 关闭文件
	fo.close()
	
# python操作Mysql数据库
	# MySQLdb是python连接Mysql数据库的接口
	
	# 1，测试连接数据库，获取数据库版本信息
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
	
	# 2,创建数据库表
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
	
	# 3，数据库插入操作
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
	
	# 4，数据库查询操作
		# python查询使用fetchone()方法获取单条数据，使用fetchall()方法获取多条数据
		# 实例，查询employee表中income大于1000的所有数据
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
		
	# 5, 数据库更新操作
		# 更新数据，将employee表中的sex为'M'的age字段增加1
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
		
	# 6，删除操作
		# 删除表里所有age大于20的数据
		# -*- coding: utf-8 -*-
		import MySQLdb

		# 打开数据库连接
		db = MySQLdb.connect('localhost', 'root', 'zpl', 'testdb')

		# 使用cursor()方法获取操作游标
		cursor = db.cursor()

		# 使用execute()方法执行sql语句

		#  删除语句
		sql = 'DELETE FROM employee WHERE age > 20'
			
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
		
	# 7，执行事务
		# 事务机制可以确保数据一致性
		# 事务4个属性(ACID)：原子性，一致性，隔离性，持久性
			# 原子性atomicity 一个事务是一个不可分割的工作单位，事务中的操作要么都做要么都不做。
			# 一致性consistency 事务必须使数据从一个一致性状态变到另一个一致性状态。
			# 隔离性isolation 一个事务的执行不能被其他事务干扰。一个事务内部的操作和使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能相互干扰。
			# 持久性durability 一个事务一旦提交，它对数据库中的数据的改变就应该是永久性的。接下来的其他操作或者故障不应该对其有任何影响。
		# commit、rollback
	# 8，错误处理
		# Warning 严重警告，例如插入数据被截断，必须是StandardError的子类
		# Error 警告之外的其他错误类，必须是StandardError的子类
		# InterfaceError 数据库接口模块本身的错误（而不是数据库的错误），必须是Error的子类
		# DatabaseError 数据库有关的错误，必须是Error的子类
		# DataError 数据处理时发生的错误，例如除零错误，数据超范围，必须是DatabaseError的子类
		# OperationalError 非用户控制的，操作数据库时发生的错误，例如连接意外断开，数据库名未找到，事务处理失败，内存分配错误等，必须是DatabaseError的子类
		# IntegrityError 完整性相关错误，例如外键检查失败，必须是DatabaseError的子类
		# InternalError 数据库内部错误，例如游标失效，事务同步失败等，必须是DatabaseError的子类
		# ProgrammingError 程序错误，例如数据表没找到或已存在，sql语法错误，参数数量错误等，必须是DatabaseError的子类
		# NotSupportedError 不支持错误， 使用了数据库不支持的函数或API，例如连接对象上使用rollback函数而数据库并不支持事务或者事务已被关闭，必须是DatabaseError的子类
		
# python网络编程
	# socket(family, type, protocol)
		# family 套接字家族，可以是AF_UNIX或者AF_INET
		# type 套接字类型，可以是面向连接(SOCK_STREAM)还是非连接(SOCK_DGRAM)
		# protocol 一般默认为0
	# Socket对象的方法
		# 服务器端
			# bind() 绑定地址到套接字。在AF_INET下，以元组(host, port)形式表示
			# listen() TCP监听，指定最大连接数量，至少为1，大部分应用程序设为5
			# accept() 被动接受TCP客户端连接（阻塞模式）
		# 客户端
			# connect() 主动初始化TCP服务器连接，地址以元组(hostname, port)给出，连接出错返回socket.error
			# connect_ex() connect()的扩展版本
		# 公共用
			# recv() 接受TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量，flag提供其他消息。
			# send() 发送TCP数据，将string中的数据发送到连接的套接字，返回要发送的字节数量。
			# sendall() 完整发送TCP数据。成功返回None，失败抛出异常。
			# recvfrom() 接收UDP数据，返回值是(data, address)，data是接收到的数据，address是发送数据的套接字地址。
			# sendto() 发送UDP数据到套接字，address形式为元组(ipaddr, port),指定远程地址，返回值是发送的字节数。
			# close() 关闭套接字
			# ......
	# 简单实例
		# 服务端
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
			
		# 客户端
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

		s.connect((host, port))
		print s.recv(1024)
		s.close()
		
	# python Internet模块
		# HTTP 网页访问，端口80，python模块：httplib, urllib, xmlrpclib
		# NNTP 阅读和张贴新闻文章，端口119，nntplib
		# FTP 文件传输，端口20，ftplib, urllib
		# SMTP 发送邮件，端口25，smtplib
		# POP3 接收邮件，端口110，poplib
		# IMAP4 获取邮件，端口143，imaplib
		# Telnet 命令行，端口23，telnetlib
		# Gopher 信息查找， 端口70，gopherlib, urllib