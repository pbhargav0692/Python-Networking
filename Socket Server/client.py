import socket, sys


def client():
    HOST, PORT = "localhost", 9999
    # data = " ".join(sys.argv[1:])
    data = "Hello from a client"
    print 'data = %s' %data

    # create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connect to server
        sock.connect((HOST, PORT))

        # send data
        sock.sendall(bytes(data + "\n"))

        # receive data back from the server
        received = str(sock.recv(1024))
    finally:
        # shut down
        sock.close()

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))


if __name__ == '__main__':
    client()

