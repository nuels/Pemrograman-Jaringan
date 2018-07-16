from scapy.all import *

ip_source="192.168.56.1"
ip_target="192.168.56.101"

for i in range(1,65535): 
	perin=sr1(IP(src=ip_source, dst=ip_target)/TCP(dport=i))
	cek=perin[TCP].flags
	if cek=="SA":
		print("Port",i," Terbuka")
		print("-----------------------------------------------------")
	else :
		print("Port",i," Tertutup")
		print("-----------------------------------------------------")


#65535