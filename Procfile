web: gunicorn main:app
from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Page d’accueil"
