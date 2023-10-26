# TODO: Feature 2 (Unit Test)
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_create_movie_unit():
    movie_repo = get_movie_repository()
    
    # clear db to make sure it starts out empty
    movie_repo.clear_db()
    
    # testing whether the movie repo is initially empty
    movies = movie_repo.get_all_movies()
    assert not movies
    
    # create new movie
    movie_name = "Random Movie"
    director = "Test Director"
    rating = 4
    
    # calling create_movie function to add movie to the repository
    movie = movie_repo.create_movie(movie_name, director, rating)
    
    # check if movie has been added to repository
    movies = movie_repo.get_all_movies()
    assert movie in movies.values() # check if created movie is in dictionary values

def test_create_movie_bad_input(test_app: FlaskClient):
    response = test_app.post('/movies', data={
        'director': 'Director2',
        'rating': '4'
    }, follow_redirects=True)

    # Ensure the response status code indicates an error (e.g., 400 Bad Request)
    assert response.status_code == 400

    # Check if the response contains the expected error message
    assert b'Invalid input' in response.data

def test_create_movie_edge_case(test_app: FlaskClient):    
    response = test_app.post('/movies', data={
        'movieName': 'Random Movie2',
        'director': 'Director3',
        'rating': '0'
    }, follow_redirects=True)
    
    assert response.status_code == 400
    
    assert b'Invalid input' in response.data    