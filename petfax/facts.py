from flask import Blueprint, render_template, request, redirect
from . import models

bp = Blueprint('fax', __name__, url_prefix="/new")

@bp.route('/', methods=['GET'])
def new_fact_form():
    return render_template('fax.html')  
       
@bp.route('/facts', methods=['GET', 'POST']) 
def fact():
    if request.method == 'POST':
        submitter = request.form['name']
        fact_text = request.form['fact']

        new_fact = models.Fact(submitter=submitter, fact=fact_text)
        models.db.session.add(new_fact)
        models.db.session.commit()
        return redirect('/new/facts')

    results = models.Fact.query.all()
    return render_template('facts.html', facts=results)

@bp.route('/update/<int:fact_id>', methods=['GET', 'POST']) 
def update(fact_id):
    fact = models.Fact.query.get_or_404(fact_id)

    if request.method == 'POST':
        submitter = request.form['name']
        fact_text = request.form['fact']

        fact.submitter = submitter
        fact.fact = fact_text

        models.db.session.commit()
        return redirect('/new/facts')

    return render_template('update.html', fact=fact)

@bp.route('/delete/<int:fact_id>', methods=['POST'])
def delete(fact_id): 
    fact = models.Fact.query.get_or_404(fact_id)
    models.db.session.delete(fact)
    models.db.session.commit()
    return redirect('/new/facts')

