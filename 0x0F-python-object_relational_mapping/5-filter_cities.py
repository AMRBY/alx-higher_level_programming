#!/usr/bin/python3
"""
list all 'cities' by 'states' from the database `hbtn_0e_0_usa`
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
    cur.execute("SELECT cities.name FROM cities JOIN states \
                 ON cities.state_id=states.id \
                 WHERE states.name LIKE BINARY %s \
                 ORDER BY cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()

    length = len(query_rows)
    for row in query_rows:
        length = length - 1
        if length == 0:
            print(row[0])
        else:
            print(row[0], end=", ")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
