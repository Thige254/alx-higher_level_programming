-- Pick the top 3 cities based on their average temperature in
-- July and August, sorting by descending temperature
SELECT city AS "city", 
       AVG(value) AS "avg_temp"
FROM temperatures
WHERE month IN (7, 8)  -- Month of July & August
GROUP BY city  -- Average by City
ORDER BY avg_temp DESC  -- Order results by descending average temperature
LIMIT 3;  -- Only top 3 cities
