-- Script to list all cities from the 'hbtn_0d_usa' database,
-- and displaying cities.id, cities.name, and states.name.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
