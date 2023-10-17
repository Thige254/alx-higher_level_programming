-- Script lists score and name columns of all records in the table 'second_table'.
-- Thew name is ordered by score in descending, and is not NULL

SELECT 
    score,
    name 
FROM 
    second_table 
WHERE 
    name != "" 
ORDER BY 
    score DESC;
