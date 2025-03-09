#!/usr/bin/python3
"""
Module that takes the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_4_usa,
it returns all the cities of a defined state.
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

    # Execute the SQL query using parameterized query to prevent SQL injection
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the cities as a comma-separated string
    print(", ".join(row[0] for row in rows))

    # Close cursor and database connection
    cur.close()
    db.close()
