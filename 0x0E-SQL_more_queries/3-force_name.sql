-- This script creates the 'force_name' table on the specified database.
-- Check for the existence and create the table 'force_name' if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
