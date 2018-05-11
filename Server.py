# -*- encoding: utf-8 -*-
import socket
import threading
from time import gmtime, strftime


class Server:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)#allow queue of 5 connections
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()#new 1 list出來 name:mylist

    def checkConnection(self):
        connection, addr = self.sock.accept()
        print('Accept a new connection', connection.getsockname(), connection.fileno())

        try:
            buf = connection.recv(1024).decode()
            if buf == '1':#註冊過的使用者
                # start a thread for new connection
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()

            else:
                connection.send(b'please go out!')
                connection.close()
        except:
            pass

    # send whatToSay to every except people in exceptNum
    def tellOthers(self, exceptNum, whatToSay):#server會給使用者connect id(身分證)，並記錄他
        for c in self.mylist:
            if c.fileno() != exceptNum:#如果不等於自己id的話，words會送給其他人，不會送給自己
                try:
                    c.send(whatToSay.encode())
                except:
                    pass

    def subThreadIn(self, myconnection, connNumber):
        self.mylist.append(myconnection)#append附/添加
        while True:
            try:#在server不斷接收message,只負責傳送給除了發話人以外的人
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg:
                    self.tellOthers(connNumber, recvedMsg)
                else:
                    pass

            except (OSError, ConnectionResetError):
                try:
                    self.mylist.remove(myconnection)
                except:
                    pass

                myconnection.close()
                return


def main():
    s = Server('localhost', 5550)
    while True:
        s.checkConnection()#不斷地去check,隨時可接收新訊並負責傳送


if __name__ == "__main__":
    main()

