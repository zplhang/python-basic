#!python
# -*-coding:utf-8 -*-

# 1
for i in range(2, 86):
	if 168 % i == 0:
		j = 168 / i
		if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
			m = (i + j) / 2
			n = (i - j) / 2
			x = n * n -100
			print x
			
# 2
for m in range(168):
	for n in range(m):
		if (m + n) * (m - n) == 168:
			x = n ** 2 - 100
			print x
			
# 3
# ����������������Χ�����ڷ�Χ��ѭ�������Ƿ���������
i = 1
# ������Χ
while ((i + 1) ** 2 - i ** 2) <= 168:
	i += 1
# ѭ�����Բ���ӡ
for j in range(1, i):
	for k in range(1, i):
		if (k * k - j * j) == 168:
			print k * k - 268