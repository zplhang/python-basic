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
# ����������������ݱ�4�����������������100����������Ҫ��400����
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
	leap = 1
if leap == 1 and month > 2:
	sum += 1
print 'It is the %dth day.' % sum

# 2
year = int(raw_input('�꣺'))
month = int(raw_input('�£�'))
day = int(raw_input('�գ�'))
month_commonyear = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
month_leapyear = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
	dth = month_leapyear[month - 1] + day
else:
	dth = month_commonyear[month - 1] + day
print '��һ���Ǳ���ĵ�%d��' % dth

# 3
import time
# import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')
day = raw_input('�������ڣ���ʽ��xxxx-xx-xx����')
t = time.strptime(day, '%Y-%m-%d')
# %j��ʾ���ڵĵ�x��
print time.strftime('����ĵ�%j��', t)

# 4 ����ʵ����������������·�Ϊ13��������Ϊ77ʱ�Ĵ���
year = int(raw_input('��������ݣ�'))
month = int(raw_input('�������·ݣ�'))
day = int(raw_input('���������ڣ�'))
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
		print '���Ǳ����%d�졣' % dth
	else:
		print '����������д������������롣'
else:
	print '������·��д������������롣'
				