from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Flask tutorial'
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

from app import routes, models
