import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

data=(sys.argv[1])
sock.sendto( data.encode('ascii'), ("255.255.255.255", 6666) )
server_data, server_addr = sock.recvfrom(100)
print(server_data.decode('ascii'))