from flask import (Blueprint, render_template)
import json

bp = Blueprint('pets', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    pets = json.load(open('pets.json'))
    print(pets)
    return render_template('index.html', pets=pets)

@bp.route('/adopt')
def adopt():
    return "I have a pet"
