from flask import (Blueprint, render_template)
import json

bp = Blueprint('pets', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    pets = json.load(open('pets.json'))
    return render_template('index.html', pets=pets)

@bp.route('/<int:index>')
def show(index):
    pets = json.load(open('pets.json'))
    pet = pets[index]
    return render_template('show.html', pet=pet)
