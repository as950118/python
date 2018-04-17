'''
기능 - 읽기,쓰기
'''

import sqlite3
import datetime

class DAO_SQLITE3:

    conn = sqlite3.connect("test.db")
    cur = conn.cursor()

    def CREATE_TABLE():
        sql_CREATE ='''
        CREATE TABLE employee(
            employeeNum CHAR(255),
            employeeName CHAR(255),
            employeeRank CHAR(255),
            lastAccess datetime,
            PRIMARY KEY(employeeNum)
        )
        '''
        cur.execute(sql)

    def SELECT_TABLE(Select, Order):
        sql_SELECT = "SELECT " + Select + "FROM employee ORDER BY" + Order
        cur.execute(sql_SELECT)

    def INESRT_TABLE(Num, Name, Rank, Time):
        sql_SELECT = '''
        SELECT employeeNum FROM employee
        '''
        ret = cur.excute(sql)
        Num = ord(ret[0]) + 1
        # Name = input("Input Name : ")
        # Rank = input("Input Rank : ")
        Time = datetime.datetime.now()

        data = (Num, Name, Rank, Time)
        sql_INSERT='''
        INSERT INTO employee(
            employeeNum,
            employeeName,
            employeeRank,
            lastAccess,
        )
        VALUSE(
            ?, ?, ?, ?
        )
        '''
        cur.excute(sql_INSERT, data)

    def UPDATE_TABLE(Num, Name, Rank, Time):
        sql_UPDATE='''
        UPDATE employee SET (
            employeeNum=?,
            employeeName=?,
            employeeRank=?,
            lastAccess=?)
        where id=?
        '''
        data = (Num, Name, Rank, Time, Num)
        cur.excute(sql_INSERT, data)


    def EXIT_TABLE():
        conn.commit()

        conn.close()
