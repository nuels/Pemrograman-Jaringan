import socket
import select

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.bind( ('0.0.0.0', 6667) )

tcp_sock.listen(10)

list_monitor = [ tcp_sock ]

while True :

    inputready, outputready, errorreadey = select.select(list_monitor, [ ], [ ])

    for conn in inputready :

        if conn == tcp_sock :
            conn, client_address = tcp_sock.accept()
            list_monitor.append(conn)
        else :
            try :
                data = conn.recv(100)
                data = data.decode('ascii')
                print(data)
                print()
            except(socket.error):
                list_monitor.remove(conn)
                print("Koneksi ditutup")
                conn.close()