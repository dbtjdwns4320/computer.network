import socket
import argparse
import threading
import sys
import glob

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
def recvmail():
    while True:
            mail = s.recv(1000)
            if not mail:
                break
            print('[SERVER] : %s'% mail.decode())
def sendmail():
    while True:
        mail = input()
        mail = mail.encode()
        s.sendall(mail)
    s.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p',help="port_number",required=True)
    parser.add_argument('-i',help="host_name",required=True)
    args =parser.parse_args()
    threading._start_new_thread(sendmail, ())
    threading._start_new_thread(recvmail, ())

    while True:
        pass
