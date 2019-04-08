from datetime import timedelta
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from app.models import Movie, Cast, db, User
from app.serializers import MovieSchema, UserSchema


api = Blueprint('api', __name__)


@api.route('/movies', methods=['GET'])
@jwt_required
def movies():
    movie = Movie.query.all()
    movie_schema = MovieSchema()
    return movie_schema.jsonify(movie, many=True), 200


@api.route('/movies/<id>', methods=['GET'])
@jwt_required
def movie(id):
    movie = Movie.query.get(id)
    if movie:
        movie_schema = MovieSchema()
        return movie_schema.jsonify(movie), 200
    return jsonify({}), 404

@api.route('/user', methods=['POST'])
def register():

    us = UserSchema()
    user, error = us.load(request.json)

    if error:
        return jsonify(error), 400

    user.gen_hash()

    db.session.add(user)
    db.session.commit()

    return us.jsonify(user), 201


@api.route('/login', methods=['POST'])
def login():
    user, error = UserSchema().load(request.json)

    if error:
        return jsonify(error), 400

    user = User.query.filter_by(username=user.username).first()

    if user and user.verify_password(request.json['password']):
        access_token = create_access_token(
            identity=user.id,
            expires_delta=timedelta(seconds=600000)
        )
        refresh_token = create_refresh_token(identity=user.id)

        return jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'message': 'Sucesso'
        }), 200

    return jsonify({
        'message': 'Credenciais invalidas'
    }), 401