from flask import url_for
from base_tests import BaseTests, MovieFactory
from app.serializers import MovieSchema


class MoviesTests(BaseTests):
    def setUp(self):
        super().setUp()
        self.header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.user.token,
        }

    def test_get_status_code(self):
        response = self.client.get(url_for('api.movies'), headers=self.header)
        self.assertEqual(200, response.status_code)

    def test_get(self):
        movie = MovieFactory()
        movie_schema = MovieSchema()
        expected = [movie_schema.dump(movie.default).data]
        response = self.client.get(url_for('api.movies'), headers=self.header)
        self.assertListEqual(expected, response.json)

    def test_unauthorized(self):
        response = self.client.get(url_for('api.movies'))
        self.assertEqual(401, response.status_code)