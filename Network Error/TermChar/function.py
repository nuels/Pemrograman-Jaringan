import struct

def send_terimination (conn, data):
    term_charr="\r\n"
    data=data+term_charr
    conn.send(data.encode('ascii'))

def recv_termination(conn):
    #variable tampung data
    data=''
    #iteraasi
    while True :
        #baca data
        buffer=conn.recv(20)
        #ubah menjadi string
        buffer=buffer.decode('ascii')
        #seleksi jika buffer mengandung term char
        if "\r\n" in buffer :
            #buang term
            data=data.replace("\r\n", "")
            #tambah buffer ke data
            data=data+buffer
            #return, keluar dari fungsi
            return data
        #else tambah buffer ke datas
        data=data+buffer
            
def send_size(conn,data):
    #hitung ukuran data
    size=len(data)
    #pack variabel size
    size=struct.pack("<I", size)
    #encode
    data=data.encode('ascii')
    data=size+data
    conn.send(datas)
    
def recv_size(conn) :
    #baca data
    size=conn.recv(4)
    size=struct.unpack("<I", size)[0]
    #bacadata
    data=conn.recv(size)
    #decode data
    data=data.decode('ascii')
    return data

#tugas
#read berdasarkan size
#bikin command untuk download
#clue rb, tidakperlu encode decode(binary)
