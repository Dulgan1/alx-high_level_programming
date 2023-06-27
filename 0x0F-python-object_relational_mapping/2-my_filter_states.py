#!/usr/bin/python3

"""
    Script displays all states in states table
    in a database with filter given from cmdline argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    curs = db.cursor()
    curs.execute("""SELECT * FROM states
                 WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4]))

    for row in curs.fetchall():
        if row[1] == argv[4]:
            print(row)

    curs.close()
    db.close()
