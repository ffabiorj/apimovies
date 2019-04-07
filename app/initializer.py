from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.api import api
from app.config import Config
from app.models import db
from app.serializers import ma
from flask_migrate import Migrate


app = Flask(__name__)

def init_app():
    app.config.from_object(Config)
    register_extensions()
    app.register_blueprint(api, url_prefix='/api/v1')
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

    return app

def register_extensions():
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    JWTManager(app)