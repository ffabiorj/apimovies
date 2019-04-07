from flask_marshmallow import Marshmallow
from app.models import Movie, Cast


ma = Marshmallow()


class CastSchema(ma.Schema):
    class Meta:
        fields = ('role', 'name')


class MovieSchema(ma.ModelSchema):
    class Meta:
        model = Movie

    casts = ma.Nested(CastSchema, many=True)

