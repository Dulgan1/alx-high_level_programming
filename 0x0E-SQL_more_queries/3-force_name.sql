-- Creates  new table force_name, if it doesn't exist
-- with columns id and name cannot be null when adding records
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
