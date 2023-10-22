# TODO: Feature 2
from app import app

def test_create_movie_valid_data():
    with app.test_client() as client:
        response = client.post('/movies', data={
            'movieName': 'Test Movie',
            'director': 'Test Director',
            'rating': 4
        })

        assert response.status_code == 302


def test_create_movie_invalid_data():
    with app.test_client() as client:
        response = client.post('/movies', data={
            'movieName': '',
            'director': 'director',
            'rating': 6
        })

        assert response.status_code == 200