import socket
import sys
import time
import msvcrt


s = socket.socket()
host = socket.gethostname()
print("Server will start on host:", host)
port = 25000
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

#num = 0
#done = False
#while not done:
#    print(num)
#    num += 1

#    if msvcrt.kbhit():
#        print (msvcrt.getch())
#        done = True
while 1:
    if msvcrt.kbhit():
        m = msvcrt.getch()
        if m == 13:
            message = m
            message = message.encode()
            conn.send(message)
            message = ""
        print (m)
        
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client: ",incoming_message)