#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

cur = db.cursor()

state = "SELECT * FROM states"

cur.execute(state)

rows = cur.fetchall()

for i in rows:
    print(i)
