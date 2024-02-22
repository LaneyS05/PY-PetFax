from flask import Flask
# factory
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "this is home"

    # register pet blueprint 
    from . import pets
    app.register_blueprint(pets.bp)

    @app.route('/pets/adopt')
    def adopt():
        return "i have a pet"

    # return the app 
    return app
