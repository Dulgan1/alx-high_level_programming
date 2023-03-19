#!/usr/bin/python3

"""
    Script takes name of state as argument and displays
    Cities in the state from passed database
    argv[1] -> user to access db
    argv[2] -> password to access db
    argv[3] -> Database (db)
    argv[4] -> Name of state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[4])
    curs = db.cursor()

    curs.execute("""SELECT cities.name FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name LIKE '{:s}' 
                 ORDER BY cities.id ASC""".format(argv[4]))
    print(', '.join(["{:s}".format(row[0]) for row in curs.fetchall()]))

    curs.close()
    db.close()
