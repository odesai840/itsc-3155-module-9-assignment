# TODO: Feature 3
from src.repositories import movie_repository

def test_get_movie_by_title():
    # get movie repository
    movies = movie_repository.get_movie_repository()

    # create test movies
    movies.create_movie("Title 1", "Director", 1)
    movies.create_movie("Title 2", "Director", 2)
    movies.create_movie("Title 3", "Director", 3)
    movies.create_movie("Title 4", "Director", 4)

    # Check that get_movie_by_title returns the correct movies
    assert movies.get_movie_by_title("Title 1").movie_id == 1
    assert movies.get_movie_by_title("Title 2").movie_id == 2
    assert movies.get_movie_by_title("Title 3").movie_id == 3
    assert movies.get_movie_by_title("Title 4").movie_id == 4

    # Check that get_movie_by_title returns None when movie is not found
    assert movies.get_movie_by_title("Fake movie") == None