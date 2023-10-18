-- Script lists all privileges of the MySQL users 'user_0d_1' & 'user_0d_2' on the localhost server

-- This down here lists privileges for user_0d_1
DO @exists := EXISTS (SELECT 1 FROM mysql.user WHERE user='user_0d_1' AND host='localhost');
IF @exists THEN
    SHOW GRANTS FOR 'user_0d_1'@'localhost';
END IF;

-- This down here lists privileges for user_0d_2
DO @exists := EXISTS (SELECT 1 FROM mysql.user WHERE user='user_0d_2' AND host='localhost');
IF @exists THEN
    SHOW GRANTS FOR 'user_0d_2'@'localhost';
END IF;
