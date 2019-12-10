#The core of this version of RisSpeak is from a tutorial by sentdex. Changes have been made based on my individual need IE threading for two way communication and formating.

import socket
import select
import multiprocessing

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()
sockets_list = [server_socket]
clients = {}

def recive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:
        return False
while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = recive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
        else:
            message = recive_message(notified_socket)
            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            print(f"{user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 4321

sb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sb_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sb_socket.bind((IP, PORT))
sb_socket.listen()
sb_list = [sb_socket]
sbclients = {}

def sbrecive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:
        return False
while True:
    read_sockets, _, exception_sockets = select.select(sb_list, [], sb_list)
    for notified_socket in read_sockets:
        if notified_socket == sb_socket:
            client_socket, client_address = sb_socket.accept()
            user = sbrecive_message(client_socket)
            if user is False:
                continue
            sb_list.append(client_socket)
            sbclients[client_socket] = user
            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
        else:
            message = sbrecive_message(notified_socket)
            if message is False:
                print(f"Closed connection from {sbclients[notified_socket]['data'].decode('utf-8')}")
                sb_list.remove(notified_socket)
                del sbclients[notified_socket]
                continue
            user = sbclients[notified_socket]
            print(f"{user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")
            for client_socket in sbclients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
    for notified_socket in exception_sockets:
        sb_list.remove(notified_socket)
        del sbclients[notified_socket]

p1 = multiprocessing.Process(target=recive_message)
p2 = multiprocessing.Process(target=sbrecive_message)

p1.start()
p2.start()

p1.join()
p2.join()