
import socket
import sys
import time
#
SERVER_PORT = 7
HOST_ADDR = ''
#
SOCKET_FAMILY = socket.AF_INET
SOCKET_TYPE = socket.SOCK_STREAM
MESSAGE_CHUNK_SIZE = 16
#
server_socket = socket.socket(SOCKET_FAMILY, SOCKET_TYPE)
server_address = (HOST_ADDR, SERVER_PORT)
try:
    server_socket.bind(server_address)
except socket.error as ex:
    print("Error: "+str(ex[0]))
    sys.exit()
server_socket.listen(10) #max connection
while True:
    client_connection_handler, client_address = server_socket.accept()
    with client_connection_handler:
    #    client_connection_handler, client_address = server_socket.accept()
        
        while True:
            try:
                data = client_connection_handler.recv(MESSAGE_CHUNK_SIZE);
                if data:
                    print("Client identified by: " + str(client_address) +" CONNECTED")
                    print("Message: " + str(data))
                    client_connection_handler.send(data);
                else:
                    break;

            except InterruptedError as ex:
                print("Error: "+str(ex[0]))
                sys.exit()
