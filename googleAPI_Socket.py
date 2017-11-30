import socket
from urllib import quote_plus


request_text = """\
GET /maps/api/geocode/json?address = {} & sensor = false HTTP/1.1 \n\r
HOST: maps.google.com:80 \r\n
User-Agent: googleAPI-Socket.py
connection: close \r\n
\r\n
"""

def geocode(address):
    sock = socket.socket()                      # create Socket
    sock.connect(('maps.google.com', 80))
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))       # send all bytes untill it is finished
    raw_reply = b''                             # indicates bytes
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print (raw_reply.decode('utf-8'))

if __name__ == '__main__':
    geocode('513 Summit Ave, Arlington, TX')


