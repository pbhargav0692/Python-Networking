import socket
if __name__ == '__main__':
    hostname = 'www.google.com'
    addr = socket.gethostbyname(hostname)
    print ('IP Address of {} is {}'.format(hostname, addr))