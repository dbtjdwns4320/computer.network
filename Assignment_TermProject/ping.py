import socket
import os
import random
import timeit
import select
import struct
import argparse
from icmp import *
from ip import *
from sniffer import *
from ip_2 import *
from udp import *
count = 1
total_ttl = 1
result_count = 0
def single_ping_request(s, addr=None):
    global total_ttl,count
    pkt_id = 0
    packet = ICMPPacket(icmp_id=pkt_id).raw
    ip = IPPacket()
    ip.dst = addr
    ip.ip_ttl = total_ttl
    ip.create_ipv4_feilds_list()
    ip.assemble_ipv4_feilds()
    while packet:

        sent = s.sendto(ip.raw + packet, (addr, 1))
        packet = packet[sent:]
        if count == 3:
            total_ttl += 1
            count -= 3
        count += 1
        return 1

def udp_re(s, addr= None):
    global total_ttl,count
    ip = IPPacket_2()
    ip.dst = addr
    ip.ip_ttl = total_ttl
    ip.create_ipv4_feilds_list_2()
   
    ip.assemble_ipv4_feilds_2()
    udp = UDPPacket()
    udp.udp_dst_port = random.randrange(30000,50000)
    udp.create_UDP_feilds_list()
    udp.assemble_udp()
   
    for i in range(0,3):
        sent = s.sendto(ip.raw + udp.raw,(addr,1))
    if count == 3:
        total_ttl += 1
        count -= 3 
    count += 1   
  
def icmp_ping():
    global total_ttl,count,result_count
    small_flag = 1
    return_ip = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    hostname = input()
    addr = socket.gethostbyname(hostname)
    print("traceroute to " + hostname + "(" + addr + ")" + ", 30 hops max")
    while True:
      print(total_ttl, end=" ")
      while result_count != 0:
          start = timeit.default_timer()
          single_ping_request(s, addr)
          return_ip = sniffing(nic = 'enp0s3')
          stop = timeit.default_timer()
          time_ms = stop - start
          if time_ms <= 1:
              print('<1ms',end=" ")
          else:
              print('%dms' % time_ms,end=" ")
          result_count -= 1
      result_count += 3
      print(return_ip)  
    s.close()
    return

def udp_ping():
    global total_ttl,count,result_count
    small_flag = 1
    return_ip = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    hostname = input()
    addr = socket.gethostbyname(hostname)
    print("traceroute to " + hostname + "(" + addr + ")")
    while True:
        print(total_ttl,end =" ")
        while result_count != 0:
            start = timeit.default_timer()
            udp_re(s, addr)
            return_ip = sniffing(nic='enp0s3')
            stop = timeit.default_timer()
            time_ms = stop - start
            if time_ms <= 1:
                print('<1ms',end=" ")
            else:
                print('%dms' % time_ms,end=" ")
            result_count -= 1
        result_count += 3
        print(return_ip) 
    s.close()
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "icmp tracer -i  udp tracer -u")
    parser.add_argument('type',type =str)
    args = parser.parse_args()
    if args.type == 'ICMP':
        icmp_ping()
    elif args.type == 'UDP':
        udp_ping()




