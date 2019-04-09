from flask import url_for
from base_tests import BaseTests, MovieFactory
from app.serializers import MovieSchema


class BaseMoviesTests(BaseTests):
    def setUp(self):
        super().setUp()
        self.header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.user.token,
        }


class MoviesTests(BaseMoviesTests):
    def test_get_status_code(self):
        response = self.client.get(url_for('api.movies'), headers=self.header)
        self.assertEqual(200, response.status_code)

    def test_get_movies(self):
        movie = MovieFactory()
        movie_schema = MovieSchema()
        expected = [movie_schema.dump(movie.default).data]
        response = self.client.get(url_for('api.movies'), headers=self.header)
        self.assertListEqual(expected, response.json)

    def test_unauthorized(self):
        response = self.client.get(url_for('api.movies'))
        self.assertEqual(401, response.status_code)


class MoviesDetailTests(BaseMoviesTests):
    def test_unauthorized(self):
        response = self.client.get(url_for('api.movie', id=1))
        self.assertEqual(401, response.status_code)

    def test_get_status_code_200(self):
        MovieFactory()
        response = self.client.get(url_for('api.movie', id=1), headers=self.header)
        self.assertEqual(200, response.status_code)

    def test_get_one_movie(self):
        movie = MovieFactory()
        movie_schema = MovieSchema()
        expected = movie_schema.dump(movie.default).data
        response = self.client.get(url_for('api.movie', id=1), headers=self.header)
        self.assertDictEqual(expected, response.json)

    def test_get_status_code_404(self):
        response = self.client.get(url_for('api.movie', id=0), headers=self.header)
        self.assertEqual(404, response.status_code)


class CreateUserTests(BaseTests):
    def test_api_should_register_user(self):
        user = {
            'username': 'test',
            'password': '1234'
        }
        expected = {
            'id': '1', 
            'username': 'test'
        }

        response = self.client.post(url_for('api.register'), json=user)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['username'], expected['username'])

    def test_api_does_not_register_user_when_missing_a_fields(self):
        user = {
            'username': 'test',
        }

        expected = {'password': ['Missing data for required field.']}

        response = self.client.post(url_for('api.register'), json=user)
        self.assertEqual(response.status_code, 400)

        self.assertEqual(response.json, expected)


class LoginTests(BaseTests):
    def test_login_sould_return_200(self):
        user = {
            'username': 'api_movies_test', 
            'password': 'q1w2e3r4'
        }
        response  = self.client.post(url_for('api.login'), json=user)
        self.assertEqual(200, response.status_code)

    def test_wrong_login_sould_return_error_message(self):
        user = {
            'username': 'api_movies', 
            'password': 'q1w2e3r4'
        }
        expected = {"message": "Credenciais invalidas"}
        response  = self.client.post(url_for('api.login'), json=user)
        
        self.assertEqual(401, response.status_code)

        self.assertEqual(response.json, expected)