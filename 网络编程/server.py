#!python
# -*-coding:utf-8 -*-

# ����socketģ��
import socket

# ����socket����
s = socket.socket()

#��ȡ����������
host = socket.gethostname()

# ���ö˿�
port = 12345

# �󶨶˿�
s.bind((host, port))

# �������ȴ��ͻ�������
s.listen(5)
while True:
	# �����ͻ�������
	c, addr = s.accept()
	print '���ӵ�ַ��', addr
	c.send('��ӭ����python�̡̳�')
	# �ر�����
	c.close()