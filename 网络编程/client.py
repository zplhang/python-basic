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

s.connect((host, port))
print s.recv(1024)
s.close()