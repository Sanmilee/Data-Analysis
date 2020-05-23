

CREATE TABLE ratings 
(user_id int, 
 movie_id int, 
 rating int, 
 rating_time int) 
row format delimited 
fields terminated by '|';


load data inpath '/user/maria_dev/ml-100k/u.data' into table ratings;


## Sample display
SELECT * FROM ratings WHERE movie_id = 50;

