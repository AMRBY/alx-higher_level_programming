-- join left with where
SELECT * FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id WHERE tv_show_genres.show_id IS NULL;
