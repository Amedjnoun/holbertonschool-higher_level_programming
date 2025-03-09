# SQL - More Queries

## Description
This project builds on basic SQL knowledge with more complex queries and database operations in MySQL. Topics covered include user management, privileges, constraints (PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE), joins, subqueries, and unions.

## Learning Objectives
By the end of this project, you should be able to explain without external help:

* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What's a PRIMARY KEY
* What's a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve data from multiple tables in one request
* What are subqueries
* What are JOIN and UNION operations

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

## How to Import a SQL Dump
```bash
# Create database
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p

# Import data
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

## File Descriptions
File | Description
--- | ---
0-privileges.sql | Lists all privileges of the MySQL users user_0d_1 and user_0d_2
1-create_user.sql | Creates the MySQL server user user_0d_1 with all privileges
2-create_read_user.sql | Creates database hbtn_0d_2 and user user_0d_2 with SELECT privilege only
3-force_name.sql | Creates table force_name with a NOT NULL constraint
4-never_empty.sql | Creates table id_not_null with default value constraint
5-unique_id.sql | Creates table unique_id with a UNIQUE constraint
6-states.sql | Creates database hbtn_0d_usa and table states with PRIMARY KEY
7-cities.sql | Creates table cities with FOREIGN KEY reference to states
8-cities_of_california_subquery.sql | Lists cities of California using a subquery
9-cities_by_state_join.sql | Lists all cities with their state names using JOIN
10-genre_id_by_show.sql | Lists shows with at least one linked genre
11-genre_id_all_shows.sql | Lists all shows with their genre IDs (including NULL)
12-no_genre.sql | Lists shows with no linked genres
13-count_shows_by_genre.sql | Lists genres with number of shows linked to each
14-my_genres.sql | Lists all genres of the show Dexter
15-comedy_only.sql | Lists all Comedy shows
16-shows_by_genre.sql | Lists all shows and their linked genres

## Usage
To execute any SQL script, use the following command:
```bash
cat script_name.sql | mysql -hlocalhost -uroot -p [database_name]
```

## Resources
* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
* [MySQL constraints](https://dev.mysql.com/doc/refman/8.0/en/constraints.html)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
* [SQL technique: multiple joins](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
* [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
* [SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
* [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
* [MySQL Tutorial](https://www.mysqltutorial.org/)
* [SQL Style Guide](https://www.sqlstyle.guide/)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
