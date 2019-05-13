import os
import socket
import argparse
import struct
ETH_P_ALL = 0x0003
ETH_SIZE = 14
def make_ethernet_header(raw_data):
	ether = struct.unpack('!6B6BH', raw_data)
	print('Ethernet Header')
	if ether[12] != 2048:
		while True:
			if ether == 2048:
				break
	return {'[dst]':'%02x:%02x:%02x:%02x:%02x:%02x' % ether[:6],
		'[src]':'%02x:%02x:%02x:%02x:%02x:%02x' % ether[6:12],
		'[ether_type]':ether[12]}

	  
		
def make_ip_header(raw2_data):
	ip = struct.unpack('!BBHHHBBH4B4B',raw2_data)
	print('\nIp_Header')
	temp = ip[0]
	temp = hex(temp)
	temp = str(temp)
	temp_2 = bin(ip[4])
	
	temp_2_flag =temp_2[2:4]
	temp_2_off = temp_2[4:17]
	#print(temp_2_flag)
	#print(temp_2_off)
	temp_2_flag = int(temp_2_flag)
	temp_2_off = int(temp_2_off)
	return{'[version]':'%s' % temp[2],
		'[header_length]':'%s' % temp[3],
		'[tos]':'%x' % ip[1],
		'[total_length]':'%d' % ip[2],
		'[ID]':'%d' % ip[3],
		'[flag]':'%03d' % temp_2_flag ,
		'[Fragment offset]':'%d' % temp_2_off ,
		'[TTL]':ip[5],
		'[Protocal]':ip[6],
		'[checksum]':ip[7],
		'[src]':'%d:%d:%d:%d' % ip[8:12],
		'[dst]':'%d:%d:%d:%d' % ip[12:16]}
	
def dumpcode(buf):
	print("\n")
	print('Raw Data')
	print("%7s"% "offset ", end='')

	for i in range(0, 16):
		print("%02x " % i, end='')

		if not (i%16-7):
			print("- ", end='')

	print("")

	for i in range(0, len(buf)):
		if not i%16:
			print("0x%04x" % i, end= ' ')

		print("%02x" % buf[i], end= ' ')

		if not (i % 16 - 7):
			print("- ", end='')

		if not (i % 16 - 15):
			print(" ")

	print("\n")

def ip_header_length(IP_SIZE):   
	IP_SIZE = hex(IP_SIZE)
	IP_SIZE = str(IP_SIZE)
	IP_TEMP = int(IP_SIZE[3])
	IP_TEMP *= 32
	IP_TEMP /= 8
	IP_SIZE = int(IP_TEMP)
	return IP_SIZE

def sniffing(nic):
	if os.name == 'nt':
		address_familiy = socket.AF_INET
		protocol_type = socket.IPPROTO_IP
	else:
		address_familiy = socket.AF_PACKET
		protocol_type = socket.ntohs(ETH_P_ALL)

	with socket.socket(address_familiy, socket.SOCK_RAW, protocol_type) as sniffe_sock:
		sniffe_sock.bind((nic, 0))

		if os.name == 'nt':
			sniffe_sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
			sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

		data, _ = sniffe_sock.recvfrom(65535)
		IP_SIZE  = ip_header_length(data[ETH_SIZE])
		IP_SIZE = IP_SIZE + ETH_SIZE
		ethernet_header = make_ethernet_header(data[:ETH_SIZE])

		for item in ethernet_header.items():
			print('{0} : {1}'.format(item[0], item[1]))

		ip_header = make_ip_header(data[ETH_SIZE:IP_SIZE])

		for item in ip_header.items():
			print('{0} : {1}'.format(item[0], item[1]))
		dumpcode(data)
		if os.name == 'nt':
			sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This is a simpe packet sniffer')
	parser.add_argument('-i', type=str, required=True, metavar='NIC name', help='NIC name')
	args = parser.parse_args()

	while True:
		sniffing(args.i)
