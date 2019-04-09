import os
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.models import Movie, Cast


api_key = os.getenv('THEMOVIEDB_API_KEY')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def get_movies():
    req_movies = requests.get('https://api.themoviedb.org/3/trending/all/week?api_key={}'.format(api_key))
    movies = req_movies.json()
    return movies.get('results', [])


def get_credits(movie_id):
    if not movie_id:
        return []
    req_credits = requests.get('https://api.themoviedb.org/3/movie/{}/credits?api_key={}'.format(movie_id, api_key))    
    return req_credits.json()


def get_movie_detail(movie_id):
    if not movie_id:
        return {}
    req_movie_detail = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, api_key))    
    return req_movie_detail.json()        


def get_director(crews):
    director = ''
    for item in crews:
        if item.get('job') == 'Director':
            director = item.get('name')
            break
    return director


def get_first_genre(genres):
    genre = ''
    if len(genres) > 1:
        genre = genres[0].get('name')
    return genre


def save_movie(movie, director, genre):
    movie = Movie(title=movie.get('title'), director=director, genre=genre)
    db.session.add(movie)
    db.session.commit()
    return movie


def save_cast(casts, movie_id):
    cast = [ Cast(role=cast.get('character'), name=cast.get('name'), movie_id=movie_id) for cast in casts ]
    db.session.bulk_save_objects(cast)
    db.session.commit()
    
    
def main():
    for movie in get_movies():
        if not movie.get('title'):
            continue

        print('[crawler][save] movie: {}'.format(movie.get('title')))

        credits = get_credits(movie.get('id'))
        casts = credits.get('cast', [])
        crews = credits.get('crew', [])

        director = get_director(crews)
        movie_detail = get_movie_detail(movie.get('id'))
        genre = get_first_genre(movie_detail.get('genres', []))

        movie = save_movie(movie, director, genre)
        save_cast(casts, movie.id)


if __name__ == "__main__":
    if api_key:
        print('[crawler] Start...')
        main()
        print('[crawler] Finish')