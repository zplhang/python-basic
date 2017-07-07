#!python
# -*-coding:utf-8 -*-

import threading
import time

class myThread(threading.Thread):
	def __init__(self, threadId, name, counter):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.name = name
		self.counter = counter
		
	# 把要执行的代码写在run()函数里，线程创建后会直接运行run()函数
	def run(self):
		print 'Starting ' + self.name
		# 获得锁，成功后返回True，可选的timeout参数不填时将一直阻塞直到获得锁，否则超时后返回False
		threadLock.acquire()
		print_time(self.name, self.counter, 3)
		# 释放锁
		threadLock.release()
		
def print_time(threadName, delay, counter):
	while counter:
		time.sleep(delay)
		print '%s: %s' %(threadName, time.ctime(time.time()))
		counter -= 1
		
threadLock = threading.Lock()
threads = []
		
# 创建线程
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

# 开启线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
	t.join()

print 'Exiting Main Thread'