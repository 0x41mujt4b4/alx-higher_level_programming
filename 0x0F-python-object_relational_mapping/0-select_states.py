#!/usr/bin/python3
import MySQLdb
from sys import argv
"""module that connect to database and fetch data"""


user = argv[1]
passwd = argv[2]
db = argv[3]
conn = MySQLdb.connect(host="localhost", port=3306,
                            user=user, passwd=passwd, db=db, charset="utf8")


def list_states():
    """function that list states from db"""
    cur = conn.cursor()
    cur.excute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    list_states()
