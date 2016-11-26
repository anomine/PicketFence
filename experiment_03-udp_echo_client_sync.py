import socket  # for sockets
import sys  # for exit

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

host = 'localhost'
port = 9999

while 1:
    msg = input('Enter message to send : ')

    try:
        # Set the whole string
        s.sendto(bytes(msg,'utf8'), (host, port))

        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0].decode('utf8')
        addr = d[1]

        print('Server reply : ' + reply)

    except socket.error as msg:
        print('Error Code : ' + str(msg.args[0]) + ' Message ' + msg.args[1])
        sys.exit()