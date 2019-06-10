import struct
import socket

ICMP_STRUCTURE_FMT = 'bbHHhH'
ICMP_ECHO_REQUEST = 8 
ICMP_CODE = socket.getprotobyname('icmp')
class ICMPPacket:
    def __init__(self,
        icmp_type = ICMP_ECHO_REQUEST,
        icmp_code = 0,
        icmp_chks = 0,
        icmp_id   = 0,
        icmp_seq  = 0,
        data      = 1,
        ):

        self.icmp_type = icmp_type
        self.icmp_code = icmp_code
        self.icmp_chks = icmp_chks
        self.icmp_id   = icmp_id
        self.icmp_seq  = icmp_seq
        self.data      = data
        self.raw = None
        self.create_icmp_field()

    def create_icmp_field(self):
        self.raw = struct.pack(ICMP_STRUCTURE_FMT,
	    self.icmp_type,
            self.icmp_code,
            self.icmp_chks,
            self.icmp_id,
            self.icmp_seq,
            self.data,
            )
        self.data_pack = struct.pack
        
        self.icmp_chks = self.chksum(self.raw)
        self.raw = struct.pack(ICMP_STRUCTURE_FMT,
	    	self.icmp_type,
	    	self.icmp_code,
	    	self.icmp_chks,
	    	self.icmp_id,
	    	self.icmp_seq,
                self.data,
            	)
        return 

    def chksum(self,data):
          sum = 0
          data_List = ""
          sum_data2 = []
          sum_data3 = []
          sum_data = ""
          data = str(data)
          data = data[3:]
          data = data[:len(data)-1]
          data = data.split('x')
          for i in data:
              sum_data += i
          sum_data = sum_data.split("\\")
          for i in range(0,len(sum_data),2):
              sum_data2.append(sum_data[i] + sum_data[i+1])
          for i in range(0,len(sum_data2)):
              sum += int(sum_data2[i],16)
          sum = bin(sum)
          sum = sum[2:]
          if len(sum) != 16:
              for i in range(0,16-len(sum)):
                  sum = '0' + sum
          sum = sum.replace('1' , '2')
          sum = sum.replace('0' , '1')
          sum = sum.replace('2' , '0')
          sum = int(sum,2)
          sum = hex(sum)
          sum = sum[4:6] + sum[2:4]
          sum = int(sum,16)
          return sum
      
  
#패킷 풀기 확인할려고 만드
def ext_icmp_header(data):
    icmph=struct.unpack(ICMP_STRUCTURE_FMT, data)
    data={
    'type'  :   icmph[0],
    "code"  :   icmph[1],
    "checksum": icmph[2],
    'id'    :   icmph[3],
    'seq'   :   icmph[4],
    }
    return data
