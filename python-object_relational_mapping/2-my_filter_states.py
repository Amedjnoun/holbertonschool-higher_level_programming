#!/usr/bin/python3
"""Script that takes in an argument and displays all  matches"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    state_name = sys.argv[4]
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' "\
            "ORDER BY id ASC".format(state_name)
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
