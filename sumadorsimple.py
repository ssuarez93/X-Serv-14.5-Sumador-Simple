#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sistemas Teleco. Sara Suárez.

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)
primer_num = None

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP request received:'
        peticion = recvSocket.recv(1024)
        print peticion
   
        try:
            numero = int(peticion.split()[1][1:])
        except ValueError:
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + 
                            "<html><body><font size=6><font face=Comic Sans MS>Debes introducir un numero despues de 'http://localhost:1234/'")
            continue

        if primer_num==None:
            num1 = numero
            primer_num = True
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + 
                            "<html><body><font size=6><font face=Comic Sans MS>Mandame el segundo numero para hacer la suma")
        else:
            num2 = numero
            resultado = num1 + num2
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + 
                            "<html><body><font size=6><font face=Comic Sans MS>" + str(num1) + " + " + str(num2) + " = " + str(resultado))
            primer_num = None

except KeyboardInterrupt:
	print "Closing binded socket"
	mySocket.close()

recvSocket.close()


