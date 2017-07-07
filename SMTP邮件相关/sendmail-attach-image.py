#!python
# -*-coding:utf-8 -*-

# 导入smtp模块
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 邮件发送方
sender = 'zplhang@163.com'

# 接收邮件的地址
receivers = ['zplhang@126.com']

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header('python教程', 'utf-8')
msgRoot['To'] = Header('测试', 'utf-8')
subject = 'python SMTP邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>python 邮件发送测试。。。</p>
<p><a href = "http://www.python.com">python教程链接</a></p>
<p>图片演示：</p>
<p><img src = "cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('test.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片ID，在HTML文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
	# smtpObj = smtplib.SMTP('localhost') # 出错，没有安装sendmail
	smtpObj = smtplib.SMTP()
	smtpObj.connect('smtp.163.com', 25)
	smtpObj.login('xxx@163.com', 'xxx')
	smtpObj.sendmail(sender, receivers, message.as_string())
	print '邮件发送成功'
except smtplib.SMTPException:
	print 'Error: 无法发送邮件'
