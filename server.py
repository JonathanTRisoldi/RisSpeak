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

message = ""
while 1:
    if msvcrt.kbhit():
        m = msvcrt.getch().decode('utf-8')
        message += m
        if m = 'x':
            print("Enter has been hit")
            #message = message.encode()
            #conn.send(message)
            #message = ""
            #print("")
        else:
            print (m, end="", flush=True)
        
    # incoming_message = conn.poll(1024)
    # incoming_message = incoming_message.decode()
    # print("Client: ",incoming_message)