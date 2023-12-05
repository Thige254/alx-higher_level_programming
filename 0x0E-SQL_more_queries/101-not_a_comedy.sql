-- Retrieve show titles excluding those categorized as 'Comedy'
SELECT title
FROM tv_shows
WHERE title NOT IN (
    -- Subquery to get titles of shows categorized as 'Comedy'
    SELECT title
    FROM tv_shows
    -- Join to link shows with their genres
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
-- Sort results in alphabetical order
ORDER BY title ASC;
