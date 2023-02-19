-- Creates  new table unique_id if it doesn't exist
-- with coloumns id INT and name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
