from datetime import timedelta
from json import loads
from unittest import TestCase
from flask_jwt_extended import create_access_token
from flask import url_for
from app.initializer import init_app
from app.models import User, Movie, Cast, db


class UserFactory():
    def __init__(self):
        self.default = self.create_user()
        self.token = self.create_jwt_acess_token()

    def create_user(self):
        user = User(username='api_movies_test', password='q1w2e3r4')
        user.gen_hash()
        db.session.add(user)
        db.session.commit()
        return user

    def create_jwt_acess_token(self):
        return create_access_token(
            identity=self.default.id,
            expires_delta=timedelta(seconds=600000)
        )


class MovieFactory():
    def __init__(self):
        self.default = self.create_movie()

    def create_movie(self):
        movie = Movie(title='test', brazilian_title='test', director='teste', genre='action')
        db.session.add(movie)
        db.session.commit()
        cast = Cast(role='teste', name='teste', movie_id=movie.id)
        db.session.add(cast)
        db.session.commit()
        return movie


class BaseTests(TestCase):
    def setUp(self):
        self.app = init_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()
        self.user = UserFactory()

    def tearDown(self):
        db.drop_all()