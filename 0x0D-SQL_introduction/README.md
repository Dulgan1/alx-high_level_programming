# SQL - Introduction

This folder and each file in it, illustrates basic knowledge and understanding
of databases and structured query language (SQL) - Basic Queries 

- **File 0**
	> Query to show all databases in a mysql server.
- **File 1**
	> Creates adatabase if it doesn't exists.
- **File 2**
	> Deletes/Removes a databse if it exists.
- **File 3**
	> Lists tables in a database (mysql).
- **File 4**
	> Creates a table named first\_table with attr id INT name VARCHAR(256).
- **File 5**
    > Shows full deacription of a table, without using DESCRIBE [tablename].
- **File 6**
    > Lists all record of a table.
- **File 7**
    > Inserts new record to table of a database, defining columns.
- **File 8**
    > Shows number of records with same value (id = 89).
- **File 9**
    > Creates a table, and adds records in a database.
- **File 10**
    > Displays score and name coloumns in the table second\_table in order of scores
# Usage
	cat [filename] | mysql -hlocalhost -uroot -p [database]

# Environment
    - Ubuntu 20.04 LTS
    - MySQL 8.0
