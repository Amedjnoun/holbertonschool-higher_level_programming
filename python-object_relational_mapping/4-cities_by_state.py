#!/usr/bin/python3
"""
Module that lists all cities from database hbtn_0e_4_usa.

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_4_usa,
it returns all cities from database with their state names.
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

    # Execute the SQL query
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
