# TODO: Feature 1
from flask.testing import FlaskClient
from src.repositories import movie_repository

def test_create_movie(test_app: FlaskClient):
    # send a GET request to the '/movies' route
    response = test_app.get('/movies')
    assert response.status_code == 200

    # send a POST request to create a new movie
    response = test_app.post('/movies', data = {
        'movieName': 'TestTitle',
        'director': 'TestDirector',
        'rating': '5'
    }, follow_redirects=True)
    assert response.status_code == 200

    # check if the movie got added to the table
    assert b'TestTitle' in response.data
    assert b'TestDirector' in response.data
    assert b'5' in response.data

    # bad tests
    assert b'BadTitle' not in response.data
    assert b'BadDirector' not in response.data