#!python
# -*-coding:utf-8 -*-

# ����Tkinterģ��
from Tkinter import *

# �������ڶ���
root = Tk()

# ���������б�
li = ['C', 'python', 'php', 'html', 'sql', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']

# ���������б����
listb = Listbox(root)
listb2 = Listbox(root)

# ��һ���б������������
for item in li:
	listb.insert(0, item)

# �ڶ����б������������ 
for item in movie:
	listb2.insert(0, item)
	
# ��������õ���������
listb.pack()
listb2.pack()

# ������Ϣѭ��
root.mainloop()