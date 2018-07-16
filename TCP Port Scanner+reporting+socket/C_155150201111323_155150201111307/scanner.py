from scapy.all import *


for i in range(1,11): 
 cek=sr1(IP(dst="192.168.43.227")/TCP(sport=80, dport=i),timeout=5)[TCP].flags
 if cek=="SA":
  print("Port",i," Terbuka")
  print("-----------------------------------------------------")
 else :
  print("Port",i," Tertutup")
  print("-----------------------------------------------------")