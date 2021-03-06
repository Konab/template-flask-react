from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
	app = Flask(__name__, static_folder="../../static/dist", template_folder="../../static")
	app.config.from_object(config_class)

	# with app.app_context():
	db.init_app(app)
	migrate.init_app(app, db)

	from app.errors import bp as errors_bp
	app.register_blueprint(errors_bp)

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	return app


from app import models

