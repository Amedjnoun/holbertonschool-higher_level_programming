#!/usr/bin/python3
"""Script that lists all cities of a state from the database hbtn_0e_4_usa"""
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

    # Execute the SQL query with safe parameter binding
    cursor.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Fetch all the rows
    cities = cursor.fetchall()

    # Format results as a comma-separated string
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    # Close cursor and database connection
    cursor.close()
    db.close()
