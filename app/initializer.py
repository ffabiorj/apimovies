from flask import Flask
from flask_cors import CORS
from app.api import api
from app.config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api, url_prefix='/api')
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})


from app.models import db
Migrate(app, db)
