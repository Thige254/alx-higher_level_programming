-- Retrieve genres and their associated show count
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres 
-- Join to get show count for each genre
RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
-- Order results by show count, descending
ORDER BY number_of_shows DESC;
