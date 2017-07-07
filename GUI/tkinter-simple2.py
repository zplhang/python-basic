#!python
# -*-coding:utf-8 -*-

# 导入Tkinter模块
from Tkinter import *

# 创建窗口对象
root = Tk()

# 创建两个列表
li = ['C', 'python', 'php', 'html', 'sql', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']

# 创建两个列表组件
listb = Listbox(root)
listb2 = Listbox(root)

# 第一个列表组件插入数据
for item in li:
	listb.insert(0, item)

# 第二个列表组件插入数据 
for item in movie:
	listb2.insert(0, item)
	
# 将组件放置到主窗口中
listb.pack()
listb2.pack()

# 进入消息循环
root.mainloop()