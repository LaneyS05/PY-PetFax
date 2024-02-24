from flask import (Blueprint, render_template, request, redirect) 

# Create a new blueprint for facts
bp = Blueprint('fax', __name__, url_prefix="/new")

@bp.route('/', methods=['GET'])
def new_fact_form():
    return render_template('fax.html')  

@bp.route('/facts', methods=['GET', 'POST']) 
def fact(): 
    if request.method == 'POST':
       print(request.form)
       return redirect('/new') 




