# TODO: Feature 2
from flask.testing import FlaskClient

def tests_create_movie(test_app: FlaskClient):
    response = test_app.get('/movies')
    assert response.status_code == 200

    response = test_app.post('/movies', data={
        'movieName': 'Test Movie',
        'director': 'Test Director',
        'rating': 4
    })
    assert response.status_code == 302