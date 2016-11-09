# -*- coding: utf-8 -*-

from socket import *

serverName = '192.168.182.128'
serverPort = 12000
#create a client socket (TCP)
clientSocket = socket(AF_INET, SOCK_STREAM)
#发起向服务器的连接（三次握手）
clientSocket.connect((serverName, serverPort))
while True:
	message = raw_input('-->')
	clientSocket.send(message)
	modifiedMessage = clientSocket.recv(1024)
	print 'From Server:', modifiedMessage
clientSocket.close()