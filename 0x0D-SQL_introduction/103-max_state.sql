-- Fetch the highest recorded temperature for each state, sorted alphabetically by the state's name
SELECT state, MAX(value) AS highest_temperature
FROM temperatures
GROUP BY state  -- Grouping by state to get one record per state
ORDER BY state ASC;  -- Ordering results in ascending order by state name
