-- group by genres
SELECT l.name AS genre, COUNT(l.name) AS number_of_shows FROM tv_genres l JOIN tv_show_genres r ON l.id=r.genre_id GROUP BY l.name ORDER BY number_of_shows DESC;
