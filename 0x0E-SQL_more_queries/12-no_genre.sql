-- join left with where
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_sh
ow_genres ON tv_shows.id=tv_show_genres.show_id WHERE tv_show_genres.show_id IS NUL
L
