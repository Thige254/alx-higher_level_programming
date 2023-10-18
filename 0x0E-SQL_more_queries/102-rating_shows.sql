-- List all shows by their rating sum.
SELECT tv_shows.title, SUM(rating) AS rating
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
