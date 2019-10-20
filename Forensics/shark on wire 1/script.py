from scapy.all import *
from scapy.layers.inet import IP, UDP

def capture_1():
    packets =rdpcap("capture.pcap")
    flag1 = ""
    flag2 = ""
    for packet in packets:
        if packet.haslayer(Raw):
            try:
                data = str(packet[Raw].load)
                ipSrc= str(packet[IP].src)
                ipDst= str(packet[IP].dst)
                if len(data)==1 and ipSrc=="10.0.0.2":
			if ipDst=="10.0.0.12":
                    		flag1+=data
			elif ipDst=="10.0.0.13":
                    		flag2+=data
            except:
                pass
    print(flag1)
    print(flag2)

if __name__ == '__main__':
    capture_1()
