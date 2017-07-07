#!python
# -*-coding:utf-8 -*-

# 导入smtp模块
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 邮件发送方
sender = 'zplhang@163.com'

# 接收邮件的地址
receivers = ['zplhang@126.com']

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header('python教程', 'utf-8')
message['To'] = Header('测试', 'utf-8')
subject = 'python SMTP邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是python教程邮件发送测试。。。', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的test.txt文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中就显示什么名字
att1['Content-Disposition'] = 'attachment; filename = "test.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的runoob.txt文件
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2['Content-Type'] = 'application/octet-stream'
att2['Content-Disposition'] = 'attachment; filename = "runoob.txt"'
message.attach(att2)

try:
	# smtpObj = smtplib.SMTP('localhost') # 出错，没有安装sendmail
	smtpObj = smtplib.SMTP()
	smtpObj.connect('smtp.163.com', 25)
	smtpObj.login('xxx@163.com', 'xxx')
	smtpObj.sendmail(sender, receivers, message.as_string())
	print '邮件发送成功'
except smtplib.SMTPException:
	print 'Error: 无法发送邮件'
