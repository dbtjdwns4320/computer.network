import struct
import socket
class UDPPacket:
 def __init__(self , udp_src_port =   53, udp_dst_port = 33434):
   self.udp_src_port = udp_src_port
   self.udp_dst_port = udp_dst_port
   self.raw = None
   self.create_UDP_feilds_list()

 def assemble_udp(self):
  self.raw = struct.pack('!HHHH',
   self.udp_src_port,
   self.udp_dst_port,
   self.udp_len,
   self.udp_chk,
   )
  return self.raw 

 def create_UDP_feilds_list(self):
   self.udp_len = 8
   self.udp_chk = 1
   return
