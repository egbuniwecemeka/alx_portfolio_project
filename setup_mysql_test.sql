-- A script tht prepares a MySQL server for the project

-- Create a database
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create a new user identified by a password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to database
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grant select privileges on performance_schema database
GRANT SELECT ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Reload the changes
FLUSH PRIVILEGES;