## Display movies and their total ratings

SELECT movie_id, count(movie_id) as ratingCount
FROM ratings
GROUP BY movie_id
ORDER BY ratingCount
DESC;


'''
## Result

movie_id	ratingcount
50	           583
258	           509
'''

