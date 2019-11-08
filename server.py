import socket
import sys
import time


s = socket.socket()
host = socket.gethostname()
print("Server will start on host:", host)
port = 8230
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

while 1:
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)

    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client: ",incoming_message)