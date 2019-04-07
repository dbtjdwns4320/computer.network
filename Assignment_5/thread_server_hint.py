import socket
import threading
import argparse

def socket_handler(conn):
    # 여기에 클라이언트 소켓에서 데이터를 받고, 보내는 코드 작성
    # ex) conn.recv(1024)
    mail = conn.recv(1024)
    print(mail.decode())
    mail = mail[::-1]
    conn.sendall(mail)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Thread server -p port")
    parser.add_argument('-p', help = "port_number", required = True)

    args = parser.parse_args()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', int(args.p)))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=socket_handler,args =(conn,))
        t.start()
        # 여기에 socket.accept 후 리턴받은 클라이언트 소켓으로 스레드를 생성하는 코드 작성

