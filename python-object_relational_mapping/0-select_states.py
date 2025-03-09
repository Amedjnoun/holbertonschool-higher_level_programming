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
