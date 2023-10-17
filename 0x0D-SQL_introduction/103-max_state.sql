-- Retrieve the peak temperature for each state,
-- and present the results in alphabetical order by state
SELECT state AS "state", 
       MAX(value) AS "max_temp"
FROM temperatures
GROUP BY state  -- Consolidate results per state
ORDER BY state ASC;  -- Arrange results by state name in ascending order
