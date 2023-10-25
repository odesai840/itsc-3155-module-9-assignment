# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_search_movies_page(test_app: FlaskClient):
    # Test that the page loads
    response = test_app.get('/movies')
    assert response.status_code == 200

    # Create a test movie
    response = test_app.post('/movies', data ={
        'movieName': 'Test Movie Title',
        'director': 'Director',
        'rating': '1'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    
    # Test that the movie was added 
    assert b'Test Movie Title' in response.data
    assert b'Director' in response.data
    assert b'1' in response.data

    search = test_app.get('/movies/search?search=Test+Movie+Title', follow_redirects=True)
    assert search.status_code == 200
    assert b"Test Movie Title" in search.data