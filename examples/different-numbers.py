#!python
# -*-coding:utf-8 -*-

# 1
for i in range(1, 5):
		for j in range(1, 5):
			for k in range(1, 5):
				if (i != j) and (i != k) and (j != k):
					print i, j, k
					
# 2
list_num = [1, 2, 3, 4]

list = [i * 100 + j * 10 + k for i in list_num for j in list_num for k in list_num if( i != j and i != k and j != k)]
print '�ܸ���Ϊ��', len(list)
print list

# 3
d = []
for i in range(1, 5):
		for j in range(1, 5):
			for k in range(1, 5):
				if (i != j) and (i != k) and (j != k):
					d.append([i, j, k])
print '��������', len(d)
print d

# 4
line = []
for i in range(123, 433):
	a = i % 10 # ��λ
	b = (i % 100) // 10 # ʮλ
	c = (i % 1000) // 100 # ��λ
	if a != b and a != c and b != c and 0 < a < 5 and 0 < b < 5 and 0 < c < 5:
		line.append(i)
		print i
print 'the total number is: ',len(line)

# 5���ü���ȥ���ظ�Ԫ��
list_name = ['1', '2', '3', '4']
list_result = []
for i in list_name:
	for j in list_name:
		for k in list_name:
			if len(set(i+j+k)) == 3: # ȥ��������111��122��
				list_result += [int(i+j+k)]
print list_result