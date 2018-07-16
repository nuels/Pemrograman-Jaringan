#import lib socket
import socket

#inisialisasi objek socket UDP/IPv4
import datetime
from datetime import datetime, timedelta
n_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 

#ikat pada ip dan port tertentu
n_socket.bind( ("0.0.0.0", 6666) )

#baca data yang diterima dari client
while True:
	data, client_addr = n_socket.recvfrom(1000)
	print (data)
#ubah data
	data = data.decode('ascii')
	if data == "Today":
		today= datetime.now().strftime('%Y-%m-%d')
		n_socket.sendto(today.encode('ascii'), client_addr)
	elif data == "Yesterday":
		yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
		n_socket.sendto(yesterday.encode('ascii'), client_addr)
	elif data == "Tomorrow":
		tomorrow = (datetime.now() + timedelta(1)).strftime('%Y-%m-%d')
		n_socket.sendto(tomorrow.encode('ascii'), client_addr)
	else:
		print("salah format")
#sendto tujuannya dispesifikasikan
	