-- Creats a new database hbtn_0d_usa if it doesn't exist,
-- a new table state in hbtn_0d_usa if it doesn't exist.
-- Coloumns of state table includes id INT (unique, auto-generated and primary key)
--  and name VARCHAR(256).
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS state (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256)
	);
