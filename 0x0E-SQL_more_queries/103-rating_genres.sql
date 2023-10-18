-- Retrieve genres and their cumulative ratings
SELECT name, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_genres
-- Connect genres to shows
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Connect shows to their ratings
JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
-- Group results by genre
GROUP BY name
-- Order results by rating (highest to lowest)
ORDER BY rating DESC;
