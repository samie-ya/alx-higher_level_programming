#!/usr/bin/python3
"""This script prints the name of the state given as an input"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
