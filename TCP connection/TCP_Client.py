# Let's start from the beginning. Whenever you want to create a TCP connection with the socket module, you do two things: create a socket object and then connect to a host in some port:
#client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
#client.connect(( HOST, PORT ))
#The AF_INET parameter is used to define the standard IPv4 address (other options are AF_UNIX and AF_INET6). The SOCK_STREAM parameters indicate it is a TCP connection (other options are SOCK_DGRAM, SOCK_RAW, SOCK_RDM, SOCK_SEQPACKET).
#All right, so the next thing you want to do is to send and receive data using socket's send and recv methods

import socket

#HOST = 'www.facebook.com'
HOST = '127.0.0.1'
PORT = 9090
#DATA = 'GET / HTTP/1.1\r\nHost: facebook.com\r\n\r\n'
DATA = 'GET /HTTP/1.1 \n'

def tcp_client():
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(DATA)
    response = client.recv(4096)
    print response

if __name__ == '__main__':
    tcp_client()
