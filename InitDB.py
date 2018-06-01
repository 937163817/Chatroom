from pymongo import MongoClient
from PyQt5.QtWidgets import QMainWindow,QApplication
import example_ui
import sys
from bson.objectid import ObjectId
client = MongoClient()
db = client["ChatRoom"]
collection = db["user"]

#collection.findone({'_id':ObjectId('')})
# 通訊類型
# from enum import Enum, IntEnum, unique
#
# try:
#     @unique
#     class OPERATION(Enum):
#         MSG = 0
#         NUMCHANGE = 1
#         ISALIVE = 2
#         CONNECT = 3
#         CHANGEPWD = 4
#         PWDCHANGE = 5
#         LOGIN = 6
# except ValueError as e:
#     print(e)
#
# spliteTag = '$@~&*^$'

class Main(QMainWindow,example_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)


class DataBaseChatRoom:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)  # 比较常用
        self.database = self.client["ChatRoom"]  # SQL: Database Name
        self.collection = self.database["user"]  # SQL: Table Name

    def loadData(self):
        pass
        return None

    # delete user by uname
    # dbChatRoom.deleteUser(['A'])
    def deleteUser(self, unameList=None):
        self.collection.remove({'uname':'E'})
        self.collection.delete_one({'uname':'D'})
        self.collection.delete_many({'uname':'C'})
        print([d for d in collection.find({})])
        return 'successful'

    # insert user
    # dbChatRoom.insertUser(uname='A', upwd='A')
    def insertUser(self, uname=None, upwd=None):
        self.collection.insert_one({'uname': 'E', 'upwd': 'E'})
        return 'successful'

    def updataUser(self, uname=None, upwd=None):
        pass
        return 'successful'

    # check checkUserExist
    def checkUserExist(self, uname='A'):
        pass
        return False

    # query user bu uname
    # dbChatRoom.queryByuname(uname='A', upwd='A')
    def queryByuname(self, uname='A', upwd='A'):
        pass
        return False

    # Init database
    # dbChatRoom.Initdatabase()
    def Initdatabase(self):
        userList = []
        userList.append({'uname': 'A', 'upwd': 'A'})
        userList.append({'uname': 'B', 'upwd': 'B'})
        userList.append({'uname': 'C', 'upwd': 'C'})
        userList.append({'uname': 'D', 'upwd': 'D'})
        userList.append({'uname': 'E', 'upwd': 'E'})
        self.collection.insert_many(userList)

    def colseClient(self):
        self.client.close()


def main():
    dbChatRoom = DataBaseChatRoom()
    dbChatRoom.Initdatabase()
    dbChatRoom.colseClient()
    print(collection.stats)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    MainWindow=Main()
    MainWindow.show()
    main()
    sys.exit(app.exec_())

