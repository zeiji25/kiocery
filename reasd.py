import mysql.connector
from mysql.connector import MySQLConnection, Error

def connect():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python-mysql',
                                       user='root',
                                       password='karl2528')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM kiocery")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    connect()
