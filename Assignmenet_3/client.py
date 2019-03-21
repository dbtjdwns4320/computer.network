import socket
import argparse
import sys
import glob

def run(host, port,file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 8888))
        filename = file
        s.sendall(filename.encode())
        resp = s.recv(1024)
        print('파일 내용을 출력합니다')
        print(resp.decode())
        if not resp:
            print('전송 실패')
            return
        with open(file,'wb') as f:

            try:
                f.write(resp)
                resp = s.recv(1024)
            except Exception as e:
                print(e)
        print('파일 다운로드 성공')
        print('현재 디렉토리의 파일 목록입니다.')
        file_list = glob.glob('*')
        print(file_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host -f file")
    parser.add_argument('-p',help="port_number",required=True)
    parser.add_argument('-i',help="host_name",required=True)
    parser.add_argument('-f',help="file_name",required=True)
    args =parser.parse_args()
    run(host=args.i, port=int(args.p),file = args.f)
