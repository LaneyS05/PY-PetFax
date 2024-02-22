from flask import Flask
from .pets import bp as pets_bp
import json
# factory
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "this is home"

    # register pet blueprint 
    from . import pets
    app.register_blueprint(pets.bp)

    # return the app 
    return app
