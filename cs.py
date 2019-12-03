import socket
import sys
import time
import msvcrt

s = socket.socket()
host = input(str("Please enter the hostname of the server:"))
port = 25100
s.connect((host,port))
print("Connected to chat server")
crid = input(str("Please enter the reciver ID:"))

message = ""
while 1:
    if msvcrt.kbhit():
        m = msvcrt.getch().decode('ASCII')
        message += m
        if m == '\r':
            #print('FREAKING WORK')
            message = message.encode()
            s.send(message)
            message = ""
            print("")
        elif m == '\b':
            print('\b', end="", flush=True)
            print(' ', end="", flush=True)
            print('\b', end="", flush=True)
        else:
            print (m, end="", flush=True)