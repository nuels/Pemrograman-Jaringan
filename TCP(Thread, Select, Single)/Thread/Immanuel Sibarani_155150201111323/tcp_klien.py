import socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect( ("127.0.0.1", 6667) )

test=True
while test :
    print ("\nWelcome")
    print("Command : ")
    print("1. Membuat File : [new nama_file]] ")
    print("2. Menghapus File : [del nama_file]")
    print("3. Membaca File : [read nama_file]")
    print("4. Keluar : exit")
    perintah, nama=input("Enter Command : ").split()
    print("\n")
    tcp_sock.send(perintah.encode('ascii'))
    tcp_sock.send(nama.encode('ascii'))

    if perintah=="read":    
        read = tcp_sock.recv(100)
        read = read.decode('ascii')
        print(read)
    elif perintah=="new":
        new = tcp_sock.recv(100)
        new = new.decode('ascii')
        print(new)
    elif perintah=="del":
        delet = tcp_sock.recv(100)
        delet = delet.decode('ascii')
        print(delet)
    elif perintah=="exit":
        tcp_sock.close()
        break
        
    else :
        print("Command Salah")
