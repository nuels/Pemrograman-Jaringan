import socket
import os
import select

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind( ('0.0.0.0', 6667) )

tcp_sock.listen(100)

list_monitor = [tcp_sock]

while True :
    inputready, outputready, errorready = select.select(list_monitor,[ ],[ ])
    
    for conn in inputready:
        if conn==tcp_sock:
            conn, client_address = tcp_sock.accept()
            list_monitor.append(conn)
        else :
            try :
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
            except(socket.error):
                list_monitor.remove(conn)
                conn.close()
