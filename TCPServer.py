# -*- coding: utf-8 -*-

from socket import *

serverPort = 12000
#创建欢迎套接字
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
#监听客户的连接请求
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	#当有客户请求连接时调用accept()方法，并创建了一个连接套接字
	connectionSocket, addr = serverSocket.accept()
	data = connectionSocket.recv(1024)
	print 'From Client:', data
	capitalizedData = data.upper()
	connectionSocket.send(capitalizedData)
	connectionSocket.close()
