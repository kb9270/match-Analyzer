from flask import Flask

# L'application Flask
application = Flask(__name__)

# Route principale
@application.route("/")
def index():
    return "Bienvenue sur mon application Flask hébergée sur Render !"
