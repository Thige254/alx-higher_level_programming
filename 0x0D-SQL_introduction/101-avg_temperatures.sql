-- Script calculates the average temperature for each city,
-- then sort the results by descending temperature
SELECT city AS "city", 
       AVG(value) AS "avg_temp"
FROM temperatures
GROUP BY city  -- average temps
ORDER BY avg_temp DESC;  -- descending average temps
