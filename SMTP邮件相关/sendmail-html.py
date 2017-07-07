#!python
# -*-coding:utf-8 -*-

# 导入smtp模块
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 邮件发送方
sender = 'zplhang@163.com'

# 接收邮件的地址
receivers = ['zplhang@126.com']

mail_msg = """
<p>Python邮件发送测试。。。</p>
<p><a href = "http://www.python.com">这是一个链接</a></p>
"""

# 消息格式
	# 第一个是文本内容
	# 第二个plain设置文本格式
	# 第三个utf-8设置编码
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header('python教程', 'utf-8')
message['To'] = Header('测试', 'utf-8')

subject = 'Python SMTP邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
	# smtpObj = smtplib.SMTP('localhost') # 出错，没有安装sendmail
	smtpObj = smtplib.SMTP()
	smtpObj.connect('smtp.163.com', 25)
	smtpObj.login('xxx@163.com', 'xxx')
	smtpObj.sendmail(sender, receivers, message.as_string())
	print '邮件发送成功'
except smtplib.SMTPException:
	print 'Error: 无法发送邮件'
