from flask import Flask, render_template
from .pets import bp as pets_bp
from .facts import bp as facts_bp

# factory 
def create_app():
    app = Flask(__name__)

    # register pet blueprint 
    app.register_blueprint(pets_bp)
    app.register_blueprint(facts_bp)

    @app.route("/") 
    def index():
        return render_template('home.html') 

    # return the app 
    return app

