from flask import Flask
from flask_cors import CORS

from app.api import api


app = Flask(__name__)


def init_webapp():
    """Initialize the web application."""
    app.config.from_object('app.config')

    app.register_blueprint(api, url_prefix='/api')

    # Initialize Flask-CORS
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

    return app