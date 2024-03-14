from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .pets import bp as pets_bp 
from .facts import bp as facts_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     


    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)



    # Register blueprints
    app.register_blueprint(pets_bp)
    app.register_blueprint(facts_bp)

    @app.route("/") 
    def index():
        return render_template('home.html') 

    return app


