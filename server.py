import socket
import sys
import time
import msvcrt
import threading


s = socket.socket()
host = socket.gethostname()
print("Server will start on host:", host)
port = 25100
s.bind((host,port))
print("")
print("Server done binding to host and port successfully")
print ("")
print("Server is waiting for incomming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr," Has connected to the server and is now online...")
print("")

message = ""

while 1:
    if msvcrt.kbhit():
        m = msvcrt.getch().decode('ASCII')
        message += m
        if m == '\r':
            #print('FREAKING WORK')
            message = message.encode()
            conn.send(message)
            message = ""
            print("")
        elif m == '\b':
            print('\b', end="", flush=True)
            print(' ', end="", flush=True)
            print('\b', end="", flush=True)
        else:
            print (m, end="", flush=True)
def recv():
    while True:
        incoming_message = conn.recv(1024)
        incoming_message = incoming_message.decode()
        print("Client: ",incoming_message)
        if not incoming_message: continue
threading.Thread(group=None, target=recv, name=None, args=(), kwargs=None, daemon=None).start()