#!/usr/bin/python3

"""
Selecting from the database where
name == argument passed
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    connects to the database if
    name == main
    """
    db = MySQLdb.connect(host="localhost", port=3306
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4]))

    rows = cur.fetchall()

    for i in rows:
        print(i)
