# TODO: Feature 2
import pytest
from app import create_movie

def test_create_movie_valid_data():
    movie_name = 'Movie'
    director = 'Director'
    rating = 4

    result = create_movie(movie_name, director, rating)
    assert result == 'Success'


def test_create_movie_invalid_data():
        movie_name = ''
        director = 'director'
        rating = 6

        result = create_movie(movie_name, director, rating)
        assert result == 'Failure'