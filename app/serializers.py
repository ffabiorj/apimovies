from flask_marshmallow import Marshmallow
from app.models import Movie, Cast, User


ma = Marshmallow()


class CastSchema(ma.Schema):
    class Meta:
        fields = ('role', 'name')


class MovieSchema(ma.ModelSchema):
    class Meta:
        model = Movie

    casts = ma.Nested(CastSchema, many=True)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User