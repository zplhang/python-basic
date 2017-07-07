#!python
# -*-coding:utf-8 -*-

# 1
profit = input('Please input total profit: ')
if profit <= 10:
	bonus = profit * 0.1
elif 10 < profit <= 20:
	bonus = (profit - 10) * 0.075 + 10 * 0.1
elif 20 < profit <= 40:
	bonus = (profit - 20) * 0.05 + 20 * 0.075 + 10 * 0.1
elif 40 < profit <= 60:
	bonus = (profit - 40) * 0.03 + 20 * 0.05 + 20 * 0.075 + 10 * 0.1
elif 60 < profit <= 100:
	bonus = (profit - 60) * 0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1
elif profit > 100:
	bonus = (profit - 100) * 0.01 + 40 * 0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1
else:
	print 'Error'
print bonus

# 2
i = int(raw_input('¾»ÀûÈó£º'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
	if i > arr[idx]:
		r += (i - arr[idx]) * rat[idx]
		print (i - arr[idx]) * rat[idx]
		i = arr[idx]
print '×Ü½±½ð£º', r