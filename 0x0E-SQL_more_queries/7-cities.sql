-- Creates database hbtn_0d_usa if it doesn't exist
-- Then creats a table cities  if it doesn't exist in hbtn_0d_usa,
-- with coloumns id INT (unique, auto-generated and can't be null and primary key)
-- 		 state_id INT (can't be null, foreign key referencing to state table id)
--		 name VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
