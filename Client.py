import socket
import threading

class Client:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')#server決定要接收什麼，和server確認可否進入(註冊)，以byte傳送至server

    def sendThreadFunc(self):
        while True:
            try:
                myword = input()#使用者輸入
                self.sock.send(myword.encode())#送出
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)#receive接收
                print(otherword.decode())
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')

def main():
    c = Client('140.138.145.73', 5550)#看要連到哪台server id
    th1 = threading.Thread(target=c.sendThreadFunc)
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:#讓副執行序不需等執行序完成才動作(切開)
        t.setDaemon(True)#(切開)
        t.start()
    t.join()

if __name__ == "__main__":
    main()
