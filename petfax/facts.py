from flask import Blueprint, render_template

# Create a new blueprint for facts
bp = Blueprint('fax', __name__, url_prefix="/new")

@bp.route('/', methods=['GET'])
def new_fact_form():
    # Render the template for submitting a new fact
    return render_template('fax.html') 


