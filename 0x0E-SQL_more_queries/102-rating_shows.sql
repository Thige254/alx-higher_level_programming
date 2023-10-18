-- Retrieve shows and their aggregate ratings
SELECT title, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_shows
-- Link shows to their respective ratings
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
-- Group and sort by rating (from highest to lowest)
GROUP BY title
ORDER BY rating DESC;
