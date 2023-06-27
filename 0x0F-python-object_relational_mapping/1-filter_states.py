#!/usr/bin/python3
"""
    Script displays all states
    starting with N from a database
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    curs = db.cursor()

    curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for row in curs.fetchall():
        if row[1][0] == 'N':
            print(row)
    curs.close()
    db.close()
