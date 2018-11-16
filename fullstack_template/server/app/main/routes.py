from app.main import bp
from flask import render_template


@bp.route("/")
def index():
	return render_template("index.html")

@bp.route("/hello")
def hello():
	return 'Hello World!'