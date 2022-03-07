#!/usr/bin/python3
"""This file prints all state from database that begin with letter 'N'"""

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY \
                     states.id ASC")
        rows = cur.fetchall()
        for r in rows:
            print(r)
        cur.close()
    except MySQLdb.Error as error:
        print("Failed to read data", error)
    finally:
        if db:
            db.close()
