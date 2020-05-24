
## HIVE views and Joins

## best movie with above 10 ratings
CREATE VIEW IF NOT EXISTS avgRatings AS
SELECT movie_id, AVG(rating) as avgRating, COUNT(movie_id) as countRating
FROM ratings
GROUP BY movie_id
ORDER BY avgRating DESC;

SELECT n.name, avgRating
FROM avgRatings t JOIN movie_names n ON t.movie_id = n.movie_id
WHERE countRating > 10;





