import socket
import os

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind( ('0.0.0.0', 6667) )
tcp_sock.listen(100)

while True :
    conn, client_address = tcp_sock.accept()
    
    perintah = conn.recv(100)
    nama = conn.recv(100)
    
    perintah = perintah.decode('ascii')
    nama = nama.decode('ascii')
    if perintah=="new":
        file = open(nama,"w") 
        kirim="OK File "+nama+" Berhasil Dibuat\n"
        conn.send(kirim.encode('ascii'))
        print("=>File "+nama+" Berhasil Dibuat\n")
    elif perintah=="del" :
        os.remove(nama)
        kirim="OK File "+nama+" Berhasil Dihapus\n"
        conn.send(kirim.encode('ascii'))
        print("=>File "+nama+" Berhasil Dihapus\n")
    elif perintah=="read":
        f = open(nama,"r")
        kirim=f.read()
        conn.send(kirim.encode('ascii'))
    else :
        print("\n")
        
    break    
    tcp_sock.close()
