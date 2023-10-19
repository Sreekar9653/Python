import mysql.connector as m
import sqlite3 as sq
try:
    con=m.connect(host="localhost", database="hinfo", user="root",password="")
    print("Mysql version is ",con.get_server_info())
    sql=sq.connect('Sqlite3_Python.db')
    cu=sql.cursor()
    cu.execute("select sqlite_version();")
    print("SQLite3 version is ",cu.fetchall())
except:
    print("Something went wrong")
