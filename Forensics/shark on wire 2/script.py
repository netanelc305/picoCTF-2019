from scapy.all import *
from scapy.layers.inet import IP, UDP

packets =rdpcap("capture.pcap")
flag = ""
for packet in packets:
    if packet.haslayer(Raw):
        try:
            ipSrc = str(packet[IP].src)
            ipDst = str(packet[IP].dst)
            sPort = str(packet[IP].sport)
            if ipSrc=="10.0.0.66" and ipDst=="10.0.0.1":
                flag+=chr(int(sPort[1:]))
        except:
            pass
print(flag)