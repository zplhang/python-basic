#!python
# -*-coding:utf-8 -*-

import threading
import time

exitFlag = 0

class myThread(threading.Thread):
	def __init__(self, threadId, name, counter):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.name = name
		self.counter = counter
		
	# 把要执行的代码写在run()函数里，线程创建后会直接运行run()函数
	def run(self):
		print 'Starting ' + self.name
		print_time(self.name, self.counter, 5)
		print 'Exiting ' + self.name
		
def print_time(threadName, delay, counter):
	while counter:
		if exitFlag:
			threading.Thread.exit()
		time.sleep(delay)
		print '%s: %s' %(threadName, time.ctime(time.time()))
		counter -= 1
		
# 创建线程
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

# 开启线程
thread1.start()
thread2.start()

print 'Exiting Main Thread'