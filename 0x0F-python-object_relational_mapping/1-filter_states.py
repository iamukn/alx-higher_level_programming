#!/usr/bin/python3

"""
Script to list all states that begins
with letter N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    connects python to
    MySQL server
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name \
            LIKE BINARY 'N%' ORDER BY states.id ASC")

    rows = cur.fetchall()

    for i in rows:
        print(i)
