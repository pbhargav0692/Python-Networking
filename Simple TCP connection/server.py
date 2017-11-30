import socket

def recvall(sock,count):
    buf = ''
    while count:
        newbuf = sock.recv(count)
        print newbuf
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    print ('Listening at', sock.getsockname())
    while True:
        print ('Waiting to accept a new connection')
        sc, sockname = sock.accept()
        print ('We have accepted a connection from', sockname)
        print ('Socket Name: ', sc.getsockname())
        print ('Socket Peer: ', sc.getpeername())
        message = recvall(sc, 16)
        print ('Incoming sixteen_octet message:', repr(message))
        sc.sendall(b'farewell, client')
        sc.close()
        print ('Reply sent, socket closed')


if __name__ == '__main__':
    server('127.0.0.1', 9090)