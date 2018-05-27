import sqlite3
import os
import datetime

class SQLite_DB:
    def __init__(self, Num):
        conn = sqlite3.connect('test.db');
        self.Cur = conn.cursor()

        sql = "SELECT * FROM test WHERE Num=:Num"
        self.Cur.execute(sql, {'Num':Num})

        self.Rows = self.Cur.fetchall()
        self.Num = Num

    def GetEnterTime(self):
        return self.Rows[0][3]
    def GetExitTime(self):
        return self.Rows[0][4]

    def CompareTime(self, Compare):
        if self.GetEnterTime()==Compare.GetEnterTime() and self.GetExitTime()==Compare.GetExitTime():
            return 1
        else:
            return 0

    def ChangeEnterTime(self, Compare):
        if self.CompareTime(Compare)==1:
            conn = sqlite3.connect('test.db')
            self.Cur = conn.cursor()

            sql = "UPDATE test SET EnterTime=:EnterTime WHERE Num=:Num"
            self.Cur.execute(sql, {'EnterTime' : datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"), 'Num':self.Num})
            self.Rows = self.Cur.fetchall()
            print(self.Rows)
            return 1
        else:
            return 0

    def ChangeExitTime(self, Compare):
        if self.CompareTime(Compare)==1:
            conn = sqlite3.connect('test.db');
            self.Cur = conn.cursor()
            sql = "UPDATE test SET ExitTime=:ExitTime WHERE Num=:Num"
            self.Cur.execute(sql, {'ExitTime' : datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"), 'Num':self.Num})
            self.Rows = self.Cur.fetchall()
            print(self.Rows)
            return 1
        else:
            return 0

    def GetAll(self):
        for row in self.Rows:
            print(row)

    def CloseDB(self):
        conn.close()

Server = SQLite_DB(1)
Client = SQLite_DB(1)

if Server.CompareTime(Client) and Client.CompareTime(Server):
    print("PASS")
    Server.ChangeEnterTime(Client)
    Server.ChangeExitTime(Client)
    print(Server.GetEnterTime())
else:
    print("DENIED")
