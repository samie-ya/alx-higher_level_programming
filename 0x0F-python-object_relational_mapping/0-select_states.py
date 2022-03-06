#!/usr/bin/python3
"""This file prints all state from database"""

if __name__ == "__main__":

    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd="root", db="hbtn_0e_0_usa",
                         charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
