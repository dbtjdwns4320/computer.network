import socket
import argparse
import os

def run_server(port=8888,file_dir = 0):
    host = '127.0.0.1'
    with socket.socket(family=socket.AF_INET, type= socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen(1)
        conn, addr = s.accept()
        filename = conn.recv(1024)
        filename = filename.decode()
        dir = file_dir + filename
        size = os.path.getsize(dir)
        size = str(size)
        size = size.encode()
        conn.sendall(size)
        print('파일 크기:',os.path.getsize(dir))
        with open(file_dir+filename, 'rb') as f:
            try:
                data = f.read(os.path.getsize(dir)))
                conn.sendall(data)
                print('파일 전송완료')
            except Exception as e:
                print(e)
        conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo server -p port -d dir")
    parser.add_argument('-p',help="port_number",required=True)
    parser.add_argument('-d',help="dir",required=True)
    args = parser.parse_args()
    run_server(port=int(args.p),file_dir=args.d)
