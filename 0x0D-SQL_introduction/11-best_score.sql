-- Script lists score and name columns of records
-- with score >= 10 in the table 'second_table', in descending of scores
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
