import socket
import struct

#alternatif pilihan sock
#tcp_sock.setsockopt(socket.SQL_SOCKET, socket.SOCK_STREAM)
# Inisiasi objek socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
tcp_sock.connect( ("127.0.0.1", 6667) )

# Kirim data
data =255
#Representasi variabel data sebagai unsigned int, dan little endian
tcp_sock.send( struct.pack("<I",data) )

# Baca data yang dikirim balik oleh server
data = tcp_sock.recv(100)
data = data.decode('ascii')
print(data)

tcp_sock.close()