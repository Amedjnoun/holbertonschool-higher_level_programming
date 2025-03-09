#!/usr/bin/python3
"""
Module that retrieves a particular state name.

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_0_usa,
it returns the state name we search as fourth argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query with user input using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        sys.argv[4])
    cur.execute(query)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row with exact match (to handle case sensitivity)
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
