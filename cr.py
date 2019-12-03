import socket
import sys
import time
import msvcrt

s = socket.socket()
host = input(str("Please enter the hostname of the server:"))
port = 25100
s.connect((host,port))
print("Connected to chat server")
crid = input(str("Please create a reciver ID:"))

while 1:  
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Sender: ",incoming_message)