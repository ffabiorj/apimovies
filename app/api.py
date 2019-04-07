from flask import Blueprint, request, jsonify
from app.models import Movie, Cast
from app.serializers import MovieSchema


api = Blueprint('api', __name__)

@api.route('/')
def status():
    return 'Hello World'

@api.route('/movies', methods=['GET'])
def movies():
    movie = Movie.query.all()
    movie_schema = MovieSchema()
    return movie_schema.jsonify(movie, many=True)