import os
import socket
import argparse
import struct
from ip import *
ETH_P_ALL = 0x0003
dst_packet = 1
dst_packet2 = 2
count__a = 0
def dst_ip(data):
	dst = struct.unpack('!4B',data)	 
	#print('%d.%d.%d.%d' % (dst[0],dst[1],dst[2],dst[3]))
	return_ip = str(dst[0]) +"." + str(dst[1]) + "." + str(dst[2]) + "." + str(dst[3])
	#print(return_ip)
	return return_ip

def sniffing(nic):
	global dst_packet,dst_packet2,count__a
	if os.name == 'nt':
		address_familiy = socket.AF_INET
		protocol_type = socket.IPPROTO_ICMP
	else:
		address_familiy = socket.AF_PACKET
		protocol_type = socket.ntohs(ETH_P_ALL)

	with socket.socket(address_familiy, socket.SOCK_RAW, protocol_type) as sniffe_sock:
		sniffe_sock.bind((nic, 0))

		if os.name == 'nt':
			sniffe_sock.setsockopt(socket.IPPROTO_ICMP,socket.IP_HDRINCL,1)
			sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

		data, _ = sniffe_sock.recvfrom(65535)
		if data[34] == 11:
			dst_packet = data[58:62]
			return dst_ip(data[26:30])
			
		if data[34] == 0:
			dst_packet2 = data[26:30]
			if dst_packet == dst_packet2:
				count__a += 1
				if count__a == 4:
					exit()
				return dst_ip(data[26:30])
			return dst_ip(data[26:30])

		if os.name == 'nt':
			sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This is a simpe packet sniffer')
	parser.add_argument('-i', type=str, required=True, metavar='NIC name', help='NIC name')
	args = parser.parse_args()
	while True:
		sniffing(args.i)

