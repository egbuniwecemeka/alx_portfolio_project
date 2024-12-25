-- A script that prepares a MySQL server for the project

-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS `hbnh_dev_db`;

-- Create the user if it does not already exist and assign a password to it
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to hbnb_dev on the hbnb_dev_db database
GRANT ALL PRIVILEGES ON 'hbnb_dev_db'.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privileges to hbnb_dev on hbnb_dev_db database 
GRANT SELECT ON 'performance_schema'.*;

-- Apply changes
FLUSH PRIVILEGES;