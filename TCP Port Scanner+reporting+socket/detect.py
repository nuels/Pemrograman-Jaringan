from scapy.all import *
import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect( ("127.0.0.1", 6667) )

def handle_packet(packet):
	sumber=packet[IP].src
	if (sumber=="192.168.43.104") :
		for i in range(1,11) :
			if i==10 :
				data = "Ada Serangan dari :"+sumber
				tcp_sock.send( data.encode('ascii') )

sniff(iface="wlp6s0", filter="tcp", prn=handle_packet)

