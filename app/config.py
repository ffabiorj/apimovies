import os

class Config:
    # # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Statement for enabling the development environment
    DEBUG = True
    TESTING = False
    ENV = os.getenv('RACK_ENV', default='development')


    # # Define the database - we are working with
    # # SQLite for this example
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', default='sqlite:///' + os.path.join(BASE_DIR, 'movie.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}

    # # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # # Use a secure, unique and absolutely secret key for
    # # signing the data.
    CSRF_SESSION_KEY = "secret"

    # # Secret key for signing cookies
    SECRET_KEY = "secret"

    # # JWT Secret key
    JWT_SECRET_KEY = "secret"