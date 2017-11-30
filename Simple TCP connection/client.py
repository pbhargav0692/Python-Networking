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

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print ('Client has been assigned socket name', sock.getsockname())
    sock.sendall(b'Hi there, server!')
    reply = recvall(sock, 16)
    print ('Server said', repr(reply))
    sock.close()


if __name__ == '__main__':
    client('127.0.0.1', 9090)