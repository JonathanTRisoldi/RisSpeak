import socket
import sys
import time

s = socket.socket()
host = input(str("Please enter the hostname of the server:"))
port = 25000
s.connect((host,port))
print("Connected to chat server")

while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server: ",incoming_message)

    message = input(str(">>"))
    message = message.encode()
    s.send(message)