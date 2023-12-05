-- Create database 'hbtn_0d_2' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user 'user_0d_2' if it doesn't exist with password 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant only SELECT privilege to 'user_0d_2' for 'hbtn_0d_2' database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Apply privilege changes
FLUSH PRIVILEGES;
