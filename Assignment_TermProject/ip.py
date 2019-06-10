import struct
import socket


class IPPacket:
 def __init__(self, dst='127.0.0.1', src='0.0.0.0',ip_ttl = 1):
  self.dst = dst
  self.src = src
  self.ip_ttl = ip_ttl
  self.raw = None
  self.create_ipv4_feilds_list()

 def assemble_ipv4_feilds(self):
  self.raw = struct.pack('!BBHHHBBH4s4s' , 
   self.ip_ver,  
   self.ip_dfc,   
   self.ip_tol,  
   self.ip_idf,  
   self.ip_flg,  
   self.ip_ttl,  
   self.ip_proto, 
   self.ip_chk,  
   self.ip_saddr, 
   self.ip_daddr 
   )
  return self.raw


 def create_ipv4_feilds_list(self):
  ip_ver = 4
  ip_vhl = 5

  self.ip_ver = (ip_ver << 4 ) + ip_vhl

  ip_dsc = 0
  ip_ecn = 0

  self.ip_dfc = (ip_dsc << 2 ) + ip_ecn
  self.ip_tol = 80
  self.ip_idf = 54321

  ip_rsv = 0
  ip_dtf = 0
  ip_mrf = 0
  ip_frag_offset = 0

  self.ip_flg = (ip_rsv << 7) + (ip_dtf << 6) + (ip_mrf << 5) + (ip_frag_offset)
  self.ip_proto = socket.IPPROTO_ICMP
  self.ip_chk = 0
  self.ip_saddr = socket.inet_aton(self.src)
  self.ip_daddr = socket.inet_aton(self.dst)

  return
