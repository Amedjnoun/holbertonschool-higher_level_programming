# Python - Object-relational mapping

## Description
This project explores the connection between databases and Python through Object-Relational Mapping (ORM). It consists of two main parts:
* Using MySQLdb to connect to a MySQL database and execute SQL queries
* Using SQLAlchemy (an ORM) to abstract database operations into Python object manipulations

## Background Context
The purpose of an ORM is to abstract storage details away from the application logic. With an ORM:

* You can focus on "What can I do with my objects" instead of "How is this object stored?"
* You won't need to write SQL queries directly, only Python code
* Your code becomes storage-independent, allowing you to change your database without rewriting your entire project

### Example: Without ORM
```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # SQL knowledge required
query_rows = cur.fetchall()
for row in query_rows:
	print(row)
cur.close()
conn.close()
```

### Example: With ORM (SQLAlchemy)
```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # No SQL queries, only objects!
	print("{}: {}".format(state.id, state.name))
session.close()
```

## Learning Objectives
By the end of this project, you should be able to explain without external help:

* Connect to a MySQL database from a Python script
* SELECT rows from a MySQL table using Python
* INSERT rows into a MySQL table using Python
* Understand what ORM means and its benefits
* Map Python classes to MySQL tables using SQLAlchemy

## Requirements
* Python 3.8.5 on Ubuntu 20.04 LTS
* MySQLdb version 2.0.x
* SQLAlchemy version 1.4.x
* Code style checked with pycodestyle 2.7.*
* All files must be executable
* All modules, classes, and methods must have proper documentation

## Installation & Setup

### Install MySQL 8.0
```bash
sudo apt update
sudo apt install mysql-server
```

### Install MySQLdb module
```bash
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient
```

### Install SQLAlchemy module
```bash
sudo pip3 install SQLAlchemy
```

## File Descriptions
File | Description
--- | ---
0-select_states.py | Script that lists all states from the database hbtn_0e_0_usa
1-filter_states.py | Lists all states with a name starting with N (upper N) from the database
2-my_filter_states.py | Takes an argument and displays all states where name matches the argument
3-my_safe_filter_states.py | Same as task 2 but protected against SQL injection
4-cities_by_state.py | Lists all cities from the database hbtn_0e_4_usa with their state names
5-filter_cities.py | Lists all cities of a specific state from the database
model_state.py | Contains the class definition of State and an instance Base = declarative_base()
7-model_state_fetch_all.py | Lists all State objects from the database using SQLAlchemy
8-model_state_fetch_first.py | Prints the first State object from the database
9-model_state_filter_a.py | Lists all State objects containing the letter 'a' in their name
10-model_state_my_get.py | Prints the State object with the specified name
11-model_state_insert.py | Adds the State object "Louisiana" to the database
12-model_state_update_id_2.py | Changes the name of the State where id=2 to "New Mexico"
13-model_state_delete_a.py | Deletes all State objects with a name containing letter 'a'
model_city.py | Contains the class definition of City that inherits from Base
14-model_city_fetch_by_state.py | Prints all City objects from the database with their states

## Resources
* [Object-relational mappers documentation](https://en.wikipedia.org/wiki/Object-relational_mapping)
* [MySQLdb and SQLAlchemy tutorials](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
* [Various guides on Python ORM best practices](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)