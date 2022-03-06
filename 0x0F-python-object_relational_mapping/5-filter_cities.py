#!/usr/bin/python3
"""This script will print the cities of the given user input"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                 ON cities.state_id = states.id WHERE states.name = %s\
                 ORDER BY cities.id ASC", (state,))
    row = cur.fetchall()
    ls = []
    for r in row:
        ls.append(r[0])
    print(', '.join(ls))
    cur.close()
    db.close()
