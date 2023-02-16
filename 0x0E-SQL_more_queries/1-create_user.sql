-- Creates user with all privileges, if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* FOR 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
