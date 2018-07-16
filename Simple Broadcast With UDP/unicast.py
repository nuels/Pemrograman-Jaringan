import socket
import datetime
from datetime import datetime, timedelta

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind( ("0.0.0.0", 6666) )

while True:
	data, client_addr = sock.recvfrom(100)
	print (data)
	data = data.decode('ascii')
	if data == "today":
		today= datetime.now().strftime('%A %d. %B %Y')
		sock.sendto(today.encode('ascii'), client_addr)
	elif data == "yesterday":
		yesterday = (datetime.now() - timedelta(1)).strftime('%A %d. %B %Y')
		sock.sendto(yesterday.encode('ascii'), client_addr)
	elif data == "tomorrow":
		tomorrow = (datetime.now() + timedelta(1)).strftime('%A %d. %B %Y')
		sock.sendto(tomorrow.encode('ascii'), client_addr)
	else:
		print("Salah")
	