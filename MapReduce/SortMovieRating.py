
# import the mrjob library
from mrjob.job import MRJob
from mrjob.step import MRStep


class SortMovieRating(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_sort_ratings)
        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_count_ratings(self, key, values):
        yield str(sum(values)).zfill(5), key


    def reducer_sort_ratings(self, count, movies):
        for movie in movies:
            yield movie, count


if __name__ == '__main__':
    SortMovieRating.run()
