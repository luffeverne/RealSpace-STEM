import pymysql
import pandas as pd


def connectDatabase():
    dbconn = pymysql.connect(
        host="localhost",
        database="mydb",
        user="root",
        password="123456",
        port=3306,
        charset='utf8'
    )
    return dbconn


def clearCoordinations(cursor):
    sqlcom = "truncate table `coordinations`"
    cursor.execute(sqlcom)


def isEmptyCoordinations(conn):
    sqlcom = "select count(*) from coordinations"
    count = pd.read_sql(sqlcom, conn).values
    return count


def elemEnterDatabase(conn, cursor, allCoordinationSet):
    clearCoordinations(cursor)
    for coor in allCoordinationSet:
        param = coor
        # print(param)
        sqlcom = "insert into coordinations values(%s, %s, %s, %s)"
        cursor.execute(sqlcom, param)
        conn.commit()
        # pd.read_sql(sqlcom, connectDatabase()

def allElem(conn):
    sqlcom = "select * from mydb.`coordinations`"
    datas = pd.read_sql(sqlcom, conn).values
    return datas

def allElemExceptOne(conn):
    sqlcom = "select * from mydb.`coordinations` where x != 1 and y != 1 and z != 1"
    datas = pd.read_sql(sqlcom, conn).values
    return datas


def elemaxbx(elemName, conn):
    sqlcom = "select * from mydb.`factorstable` where element='" + elemName + "'"
    datas = pd.read_sql(sqlcom, conn).values
    return datas


def elemCoor(elemName, conn):
    sqlcom = "SELECT * FROM mydb.`coordinations` WHERE element = '" + elemName + "'"
    datas = pd.read_sql(sqlcom, conn).values
    return datas

def elemCoorExceptOne(elemName, conn):
    sqlcom = "SELECT * FROM mydb.`coordinations` WHERE element = '" + elemName + "'" + \
             "and x != 1 and y != 1 and z != 1"
    datas = pd.read_sql(sqlcom, conn).values
    return datas

