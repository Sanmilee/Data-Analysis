
from starbase import Connection

c = Connection("127.0.0.1", "8000")


# create table named ratings
ratings = c.table('ratings')


# if table named ratings already exixts in the DB, delete it
if (ratings.exists()):
	print("Dropping exisiting ratings table \n")
	ratings.drop()


# create column family called rating in the ratings table
ratings.create('rating')
 

print("Parsing the ml-100k ratings data...... \n")
ratingFile = open('u.data', 'r')


# create batch object from the inbuilt function
batch = ratings.batch()


# update the batch with new rows from the loaded data
# outputs a primary key with column named userID 
# And a tuple having movieID & rating in the column family called rating 
for line in ratingFile:
	(userID, movieID, rating, timestamp) = line.split()
	batch.update(userID, {'rating': {movieID: rating}})


ratingFile.close()



print("Commiting ratings data to HBase via REST service \n")
batch.commit(finalize=True)



print("Ratings for UserID 1: \n")
print(ratings.fetch("1"))
print("Ratings for UserID 2: \n")
print(ratings.fetch("33"))

