#!/usr/bin/env python3
"""
Module that list all `states` from the database `hbtn_0e_0_usa`
"""
import MySQLdb
import sys


def main():
    """
    main function to print states table
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)


if __name__ == "__main__":
    main()
