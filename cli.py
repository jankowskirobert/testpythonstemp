import socket
import sys
#
SERVER_PORT = 7
HOST_ADDR = 'localhost'
#
SOCKET_FAMILY = socket.AF_INET
SOCKET_TYPE = socket.SOCK_STREAM
#
ECHO_MESSAGE = b'Test 123'
client_socket = socket.socket(SOCKET_FAMILY, SOCKET_TYPE)
server_address = (HOST_ADDR, SERVER_PORT)
print('connecting to %s port %s' % server_address)
client_socket.connect(server_address)
client_socket.sendall(ECHO_MESSAGE)
receiverd_back_message = client_socket.recv(16)
print("Received: "+repr(receiverd_back_message))

