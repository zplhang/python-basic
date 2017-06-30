#!python
# -*- coding: UTF-8 -*-

# HTTP头部
print 'Content-Disposition: attachment; filename = "foo.txt"'
print 

# 打开文件
fo = open('file-save.py', 'rb')

# 相当于下载服务器的file-sava.py文件内容保存到foo.txt文件中

str = fo.read()
print str

# 关闭文件
fo.close()