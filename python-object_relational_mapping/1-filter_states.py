#!/usr/bin/python3
"""Script that lists all states with a name starting with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Display results - ensure binary string comparison for exact uppercase N match
    for state in states:
        if state[1][0] == 'N':  # Ensure it starts with uppercase N
            print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
