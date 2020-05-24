
## HIVE views and Joins

## best movie with ratings
CREATE VIEW topMovies AS
SELECT movie_id, COUNT(movie_id) as countRating
FROM ratings
GROUP BY movie_id
ORDER BY countRating DESC;

SELECT n.name, countRating
FROM topMovies t JOIN movie_names n ON t.movie_id = n.movie_id;

#DROP VIEW topMovies;




