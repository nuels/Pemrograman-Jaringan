import socket
from function import send_terimination, recv_termination
# Inisiasi objek socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
tcp_sock.connect( ("127.0.0.1", 6667) )

# Kirim data
data = "Deployment merupakan proses pe-release-an perangkat lunak yang telah dibuat .Maintenance dilakukan bila didapati bug ataupun error pada perangkat lunak yangdibuat. Evolution merupakan merubah sebagian atau bahkan semua sistem yang adapada perangkat lunak yang telah dibuat dalam rangka menjadikan perngkat lunak menjadi lebih baik, yang diubah pada evolution biasanya berupa, system environtment,maupun user target."
send_terimination(tcp_sock, data)
# Baca data yang dikirim balik oleh server
data = recv_termination(tcp_sock)
print(data)

tcp_sock.close()