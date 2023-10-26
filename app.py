from flask import Flask, redirect, render_template, request, make_response

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True, movies=movie_repository.get_all_movies())


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2

    # getting data from form
    movie_name = request.form.get('movieName')
    director = request.form.get('director')
    rating = request.form.get('rating', type=int)

    # validating data
    if not movie_name or not director or rating not in range(1,6):
        response = make_response("Invalid input", 400)
        return response
    
    # saving movie rating to movie repo
    movie_repository.create_movie(movie_name, director, rating)

    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    search = request.args.get("search")
    movie = None
    if (search):
        movie = movie_repository.get_movie_by_title(search)
    return render_template('search_movies.html', search_active=True, movie=movie)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    return render_template('get_single_movie.html')


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')
