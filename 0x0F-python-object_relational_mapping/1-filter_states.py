#!/usr/bin/python3
"""
A script that lists all states with a name with capital N
from the database
"""

import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # connection to the database
     db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # gives the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
            LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)
        # clean up
        cur.close()
        db.close()
