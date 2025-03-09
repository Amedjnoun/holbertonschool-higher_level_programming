#!/usr/bin/python3
"""
Module that lists all states with a name starting with N.

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_0_usa,
it returns all states with a name starting with N (upper case)
sorted in ascending order by states.id.
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

    # Execute the SQL query with BINARY for case-sensitive comparison
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
