import socket
import argparse
import sys
import glob

def run(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 8888))
        mail = input('문자 입력:')
        s.sendall(mail.encode())
        mail = s.recv(1024)
        print(mail.decode())
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p',help="port_number",required=True)
    parser.add_argument('-i',help="host_name",required=True)
    args =parser.parse_args()
    run(host=args.i, port=int(args.p))
