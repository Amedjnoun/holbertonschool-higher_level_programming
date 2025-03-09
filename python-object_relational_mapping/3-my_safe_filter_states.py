#!/usr/bin/python3
"""Script that displays states, safe from SQL injection"""
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

    # Get the state name from command line argument
    state_name = sys.argv[4]

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query with user input safely using parameter binding
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                  (state_name,))

    # Fetch all the rows
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
