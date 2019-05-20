import socket
import argparse
import random
from ICMP import ICMPPacket

def Ping_request(s, nama = None):
	P_id = random.randrange(10000,65000)
	packet = ICMPPacket(ic_id = P_id).raw

	while packet:
		sent = s.sendto(packet, (name,1))
		packet = packet[sent:]

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
name = 'www.google.com'
print(Ping_request(s,name))

s.close()
