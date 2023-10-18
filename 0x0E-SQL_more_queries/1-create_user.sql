-- Check if the user 'user_0d_1' exists
SELECT user FROM mysql.user WHERE user = 'user_0d_1';

-- If the user doesn't exist, create the user and grant all privileges
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
