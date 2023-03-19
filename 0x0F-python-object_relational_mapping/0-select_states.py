#!/usr/bin/python3
"""
    Script takes argument
    and displays all states from a database
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")

    for row in curs.fetchall():
        print(row)

    curs.close()
    db.close()
