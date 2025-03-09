# SQL Introduction

## Description
This project serves as an introduction to SQL (Structured Query Language) and relational databases using MySQL. It covers basic SQL commands for database and table management, as well as data manipulation and querying techniques.

## Learning Objectives
By the end of this project, you should be able to explain without external help:

* What's a database
* What's a relational database
* What SQL stands for
* What MySQL is
* How to create a database in MySQL
* What DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

## Requirements
* All files executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
* All files should end with a new line
* All SQL queries should have a comment just before (see example below)
* All files should start with a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE, etc.)
* Allowed editors: vi, vim, emacs
* The length of files will be tested using wc

## SQL Comment Format
```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## Installation

### For Ubuntu 22.04
```bash
# Update package list
sudo apt update

# Install MySQL server
sudo apt install -y mysql-server

# Start MySQL service
sudo service mysql start

# Connect to MySQL
sudo mysql
```

### For Ubuntu 20.04
```bash
# Update package list
sudo apt update

# Install MySQL server
sudo apt install mysql-server

# Start MySQL service
sudo service mysql start

# Connect to MySQL (credentials are root/root in sandbox)
sudo mysql
```

## File Descriptions
File | Description
--- | ---
0-list_databases.sql | Script that lists all databases of the MySQL server
1-create_database_if_missing.sql | Creates the database hbtn_0c_0 if it doesn't exist
2-remove_database.sql | Deletes the database hbtn_0c_0 if it exists
3-list_tables.sql | Lists all tables of a specified database
4-first_table.sql | Creates a table called first_table with id (INT) and name (VARCHAR(256))
5-full_table.sql | Prints the full description of first_table without using DESCRIBE or EXPLAIN
6-list_values.sql | Lists all rows of the first_table
7-insert_value.sql | Inserts a new row in first_table (id = 89, name = "Best School")
8-count_89.sql | Displays the number of records with id = 89 in first_table
9-full_creation.sql | Creates second_table with multiple rows
10-top_score.sql | Lists all records of second_table, ordered by score
11-best_score.sql | Lists records with score >= 10 in second_table
12-no_cheating.sql | Updates Bob's score to 10 without using his id
13-change_class.sql | Removes all records with score <= 5 in second_table
14-average.sql | Calculates the average score of all records in second_table
15-groups.sql | Lists the number of records with the same score in second_table
16-no_link.sql | Lists all records of second_table with a name value, ordered by score

## Usage
To execute any SQL script, use the following command:
```bash
cat script_name.sql | mysql -hlocalhost -uroot -p [database_name]
```

## Resources
* [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
* [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
* [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
* [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
