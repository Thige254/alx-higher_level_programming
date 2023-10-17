-- Setting the context to the hbtn_0c_0 database
USE `hbtn_0c_0`;

-- Converts the entire table `first_table` in the database hbtn_0c_0 to UTF8.
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
