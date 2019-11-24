import socket
import sys
import time
import msvcrt

s = socket.socket()
host = input(str("Please enter the hostname of the server:"))
port = 25000
s.connect((host,port))
print("Connected to chat server")

while 1:
    if msvcrt.kbhit():
        m = msvcrt.getch().decode('utf-8')
        if m == "x":
            #print("Enter has been hit")
             message = m
             message = message.encode()
             conn.send(message)
             message = ""
        else:
            print (m, end="", flush=True)
    
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server: ",incoming_message)