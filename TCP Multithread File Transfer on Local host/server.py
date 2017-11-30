# Local File Transfer - Our server code above can only interact with one client.
# If we try to connect with a second client, however, it simply won't reply to the new client.
# To let the server interact with multiple clients, we need to use multi-threading.

import socket
from threading import Thread
from SocketServer import ThreadingMixIn

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024


def server():
    class ClientThread(Thread):
        def __init__(self, ip, port, sock):
            Thread.__init__(self)
            self.ip = ip
            self.port = port
            self.sock = sock
            print " New thread started for "+ip+":"+str(port)

        def run(self):
            filename='mytext.txt'
            f = open(filename,'rb')
            while True:
                l = f.read(BUFFER_SIZE)
                while (l):
                    self.sock.send(l)
                    #print('Sent ',repr(l))
                    l = f.read(BUFFER_SIZE)
                if not l:
                    f.close()
                    self.sock.close()
                    break

    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((TCP_IP, TCP_PORT))
    threads = []

    while True:
        tcpsock.listen(5)
        print "Waiting for incoming connections..."
        (conn, (ip,port)) = tcpsock.accept()
        print 'Got connection from ', (ip, port)
        newthread = ClientThread(ip, port, conn)
        newthread.start()
        threads.append(newthread)

    for t in threads:
        t.join()


if __name__ == '__main__':
    server()
