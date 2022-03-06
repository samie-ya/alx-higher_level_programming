#!/usr/bin/python3
"""This script avoids sql injection"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s", (state,))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
