# TODO: Feature 2
from flask.testing import FlaskClient

def tests_create_movie(test_app: FlaskClient):
    response = test_app.get('/movies')
    assert response.status_code == 200

    # test for missing data
    response = test_app.post('/movies', data={}) # submitting an empty form
    assert response.status_code == 400