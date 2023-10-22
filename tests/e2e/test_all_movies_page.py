# TODO: Feature 1
from flask.testing import FlaskClient

def test_create_movie(test_app: FlaskClient):
    # Send a GET request to the '/movies' route
    response = test_app.get('/movies')
    assert response.status_code == 200

    # Send a POST request with test data
    response = test_app.post('/movies', data={
        'title': 'SomeTitle1',
        'director': 'SomeDirector1',
        'rating': 5
    })
    assert response.status_code == 302