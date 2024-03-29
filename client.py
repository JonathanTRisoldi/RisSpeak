#The core of this version of RisSpeak is from a tutorial by sentdex. Changes have been made based on my individual need IE threading for two way communication and formating and sandboxing.

import socket
import select
import errno
import sys
import threading


HEADER_LENGTH = 10

IP = input("Host IP: ")
PORT = int(input("Host Port: "))

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

def send():
    while True:
        message = input(f"")

        if message:
            message = message.encode("utf-8")
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
            client_socket.send(message_header + message)
def recive():
    while True:
        try:
            while True:
                # Recive things till error
                username_header = client_socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print("connection closed by the server")
                    sys.exit()
                
                username_length = int(username_header.decode("utf-8").strip())
                username = client_socket.recv(username_length).decode("utf-8")

                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode("utf-8").strip())
                message = client_socket.recv(message_length).decode("utf-8")

                print(f"{username}: {message}")

        except IOError as e:
            if e.errno !=errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error', str(e))
                sys.exit
                continue
        
        except Exception as e:
            print('General error', str(e))
            pass


          
if __name__=="__main__":
    t1 = threading.Thread(target=send, name='t1')
    t2 = threading.Thread(target=recive, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
