-- Creates a table id_not_null, if it doesn't exist already
-- with coloumns [id of type INT, with default value and name of type VARCHAR(256)]
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
