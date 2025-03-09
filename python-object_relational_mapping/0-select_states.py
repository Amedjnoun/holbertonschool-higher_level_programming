#!/usr/bin/python3
"""
Module that lists all states from database

after connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_0_usa,
it returns all states from database
sorted in ascending order by states.id


Usage:
    python3 0-select_states.py
    <mysql_username> <mysql_password> <database_name>

Args :
    mysql_username: argv[1]
    mysql_password: argv[2]
    database_name: argv[3]

Returns:
    Prints all states from the database
"""

import MySQLdb
from sys import argv


def connect_database(username, password, db_name):
    """
    Args:
        username (str): mysql username
        password (str): mysql password
        database_name (str): database name

    Returns:
        Returns MySQL connection to database
    """
    return MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )


if __name__ == "__main__":
    """Main entry point"""

    with connect_database(argv[1], argv[2], argv[3]) as db:

        # ensuring query executes well  by using cursor object
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        for state in cursor.fetchall():
            print(state)
