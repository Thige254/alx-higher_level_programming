-- This script lists all cities of California from the 'hbtn_0d_usa' database.
SELECT id, name
FROM cities
WHERE state_id IN (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id ASC;
