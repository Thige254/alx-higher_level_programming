-- Script lists all privileges of the MySQL users 'user_0d_1' & 'user_0d_2' on the localhost server

-- Lists privileges for user_0d_1 if exists
SELECT CONCAT('SHOW GRANTS FOR ''', user, '''@''', host, ''';') AS query
FROM mysql.user
WHERE user = 'user_0d_1' AND host = 'localhost';

-- Lists privileges for user_0d_2 if exists
SELECT CONCAT('SHOW GRANTS FOR ''', user, '''@''', host, ''';') AS query
FROM mysql.user
WHERE user = 'user_0d_2' AND host = 'localhost';
