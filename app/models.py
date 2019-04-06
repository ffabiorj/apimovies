from flask_sqlalchemy import SQLAlchemy
from app.initializer import app


db = SQLAlchemy(app)


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