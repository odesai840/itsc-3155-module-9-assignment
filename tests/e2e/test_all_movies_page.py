# TODO: Feature 1
from flask.testing import FlaskClient

def test_create_movie(test_app: FlaskClient):
    # Send a GET request to the '/movies' route
    response = test_app.get('/movies')
    assert response.status_code == 200

    # Send a POST request to create a new movie
    response = test_app.post('/movies', data = {
        'movieName': 'TestTitle',
        'director': 'TestDirector',
        'rating': '5'
    }, follow_redirects=True)
    assert response.status_code == 200

    # Check if the movie got added to the table
    assert b'TestTitle' in response.data
    assert b'TestDirector' in response.data
    assert b'5' in response.data

    # Bad tests
    assert b'BadTitle' not in response.data
    assert b'BadDirector' not in response.data