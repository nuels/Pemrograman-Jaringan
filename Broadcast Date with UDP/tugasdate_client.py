import socket 
import datetime 
n_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
data = "Today"
n_socket.sendto(data.encode('ascii'), ("255.255.255.255", 6666))
server_data,server_addr = n_socket.recvfrom(1000)
#baca dari server
print(server_data.decode('ascii'))
