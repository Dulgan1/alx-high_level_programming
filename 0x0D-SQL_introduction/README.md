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
    > Displays score and name coloumns in the table second\_table in order of scores.

- **File 11**
    > Displays in order of scores and from score to name, the records that have score greater or equal to 10.

- **File 12**
    > Updates a record in second\_table, score of Bob.

- **File 13**
    > Removes all records with score less or equal to 5.

- **File 14**
    > Computes the average score of all records and return in a new column average.

- **File 15**
    > Displays records with same score in second\_table and also number of occurence.

- **File 16**
    > script that lists all records of the table second\_table of the database hbtn\_0c\_0 in your MySQL server. Don’t list rows without a name value. Results should display the score and the name (in this order). Records should be listed by descending score. The database name will be passed as an argument to the mysql command.
- **File 100**
    > Converts hbtn\_0c\_0 database to utf-8.
# Usage
`cat [filename] | mysql -hlocalhost -uroot -p [database]`

# Environment
    - Ubuntu 20.04 LTS
    - MySQL 8.0
