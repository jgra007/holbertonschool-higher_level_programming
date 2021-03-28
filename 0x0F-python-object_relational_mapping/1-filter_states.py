#!/usr/bin/python3
"""Conect DataBase and query"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306,)

    cur = db.cursor()
    cur.execute('SELECT id, name FROM states\
    WHERE name COLLATE latin1_general_cs LIKE "N%" ORDER BY states.id ASC;')
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
