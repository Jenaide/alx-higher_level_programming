#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
import sys
import MySQLdb


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    data = MySQLdb.connect(host='localhost', user=username, passwrd=password, dbname=data, port=3306) #open db connection
    cur = db.cursor() #opens cursor connection
    numb_rows = cur.execute('SELECT * FROM states ORDER BY states.id;')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close() #closes the cursor connection
    db.close() #closes the database connection
