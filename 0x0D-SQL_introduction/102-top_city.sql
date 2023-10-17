-- Retrieve the top 3 cities with the highest average temperatures during the months of July and August
SELECT city, AVG(value) AS average_temperature
FROM temperatures
WHERE month IN (7, 8)  -- Filtering for July and August
GROUP BY city
ORDER BY average_temperature DESC  -- Sorting in descending order by the average temperature
LIMIT 3;  -- Limiting the results to the top 3
