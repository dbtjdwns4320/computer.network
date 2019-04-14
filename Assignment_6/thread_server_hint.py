import socket
import threading
import argparse

def recvmail():
    # 여기에 클라이언트 소켓에서 데이터를 받고, 보내는 코드 작성
    # ex) conn.recv(1024)
    while True:
        mail = conn.recv(1024)
        if not mail:
            break
        else :
            print('[USER] : %s' % mail.decode())
    conn.close()
def sendmail():
    while True:
        mail = input('')
        mail = mail.encode()
        conn.sendall(mail)
    conn.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Thread server -p port")
    parser.add_argument('-p', help = "port_number", required = True)
    args = parser.parse_args()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', int(args.p)))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        threading._start_new_thread(sendmail,())
        threading._start_new_thread(recvmail,())

    while True:
        pass


