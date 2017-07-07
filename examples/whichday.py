#!python
# -*-coding:utf-8 -*-

# 1
year = int(input('year: '))
month = int(input('month: '))
day = int(input('day: '))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
	sum = months[month - 1]
else:
	print 'data error'

sum += day
leap = 0
# 闰年满足条件：年份被4整除，并且年份若是100的整数倍，要被400整数
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
	leap = 1
if leap == 1 and month > 2:
	sum += 1
print 'It is the %dth day.' % sum

# 2
year = int(raw_input('年：'))
month = int(raw_input('月：'))
day = int(raw_input('日：'))
month_commonyear = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
month_leapyear = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
	dth = month_leapyear[month - 1] + day
else:
	dth = month_commonyear[month - 1] + day
print '这一天是本年的第%d天' % dth

# 3
import time
# import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')
day = raw_input('输入日期（格式如xxxx-xx-xx）：')
t = time.strptime(day, '%Y-%m-%d')
# %j表示年内的第x天
print time.strftime('今年的第%j天', t)

# 4 考虑实际情况，处理输入月份为13或者天数为77时的错误
year = int(raw_input('请输入年份：'))
month = int(raw_input('请输入月份：'))
day = int(raw_input('请输入日期：'))
months = [31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dth = 0

if 0 < month <= 12:
	if 0 < day <= 31:
		dth = dth + day
		if month > 2:
			if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
				dth = dth + 1
		for i in range(12):
			if (i + 1) < month:
				dth = dth + months[i]
				i += 1
		print '这是本年第%d天。' % dth
	else:
		print '输入的日期有错误，请重新输入。'
else:
	print '输入的月份有错误，请重新输入。'
				