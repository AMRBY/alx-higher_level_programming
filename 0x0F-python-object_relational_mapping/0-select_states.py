#!/usr/bin/python3
"""
Module that list all `states` from the database `hbtn_0e_0_usa`
"""
import MySQLdb
from sys import argv


def main():
    """
    main function to print states table
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
