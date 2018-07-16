from scapy.all import *

def handle_packet(packet):
	paket=packet[Raw].load
	paketnya=len(paket)
	if paketnya > 51200 :
		print("Ada Serangan ICMP Attack")
		print("Jumlah Payload : ", paketnya)
	else :
		print("Tidak Ada Serangan ICMP")	
sniff(iface="vboxnet0", filter="icmp", prn=handle_packet)

#20kb=51200 Char