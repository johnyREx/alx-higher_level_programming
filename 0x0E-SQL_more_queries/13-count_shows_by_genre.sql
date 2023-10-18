-- lists all shows in hbtn_0d_tvsows that have at least 1 genre linked
SELECT tv_genres.name AS genre,
	COUNT(tv_show_genres.genre_id) AS number_shows
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_shows DESC;
