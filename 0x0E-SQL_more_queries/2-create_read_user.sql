-- Check if the database 'hbtn_0d_2' exists
SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = 'hbtn_0d_2';

-- If the database doesn't exist, create it
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user 'user_0d_2' exists
SELECT user FROM mysql.user WHERE user = 'user_0d_2';

-- If the user doesn't exist, create the user and grant SELECT privilege
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
