import MySQLdb

conn = MySQLdb.CONNECT(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.excute("SELECT * FROM states")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
