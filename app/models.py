from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256


db = SQLAlchemy()

class Movie(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    brazilian_title = db.Column(db.String(120))
    director = db.Column(db.String(100))
    genre = db.Column(db.String(100))

    def __str__(self):
        return self.title


class Cast(db.Model):

    __tablename__ = 'casts'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100))
    name = db.Column(db.String(100))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    movie = db.relationship("Movie", backref=db.backref('casts', lazy=True))

    def __str__(self):
        return self.role


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def gen_hash(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)