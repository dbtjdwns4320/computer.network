import struct
import socket

class ICMPPacket:
	def __init__(self,
		     	ic_type = 8,
			ic_code = 0,
			ic_check = 0,
			ic_id = 1,
			ic_sn = 1,
			data = '' ,
			):
	
		self.ic_type = ic_type
		self.ic_code = ic_code
		self.ic_check = ic_check
		self.ic_id = ic_id
		self.ic_sn = ic_sn
		self.data = data
		self.raw = None
		self.icmp_mk()
	
	def icmp_mk(self):
	  self.raw = struct.pack('bbHHh',
				self.ic_type,
				self.ic_code,
				self.ic_check,
				self.ic_id,
				self.ic_sn,
				)
	  self.ic_check = self.check_mk(self.raw + self.data.encode())
	  self.raw = struct.pack('bbHHh',
				self.ic_type,
				self.ic_code,
				self.ic_check,
				self.ic_id,
				self.ic_sn,
				)
	  return

	def check_mk(self,mes):
	
		
		z = 0
		
		for i in range(0,len(mes),2):
			x = ord(mes[i])
			y = ord(mes[i+1])
			z = z + (x + (y << 8))
		z = z + (z >> 16)
		z = ~z & 0xffff
		return z













				
