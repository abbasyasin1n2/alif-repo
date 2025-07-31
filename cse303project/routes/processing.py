
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..database import (
    get_all_processing_sessions, get_processing_session_by_id, add_processing_session,
    get_processing_outputs_for_session, add_processing_output, get_all_products
)

processing_bp = Blueprint('processing', __name__, template_folder='templates')

@processing_bp.route('/sessions')
@login_required
def list_sessions():
    sessions = get_all_processing_sessions()
    return render_template('processing/list_sessions.html', sessions=sessions)

@processing_bp.route('/sessions/<int:id>')
@login_required
def view_session(id):
    session = get_processing_session_by_id(id)
    outputs = get_processing_outputs_for_session(id)
    return render_template('processing/view_session.html', session=session, outputs=outputs)

@processing_bp.route('/sessions/add', methods=['GET', 'POST'])
@login_required
def add_session():
    if request.method == 'POST':
        session_name = request.form['session_name']
        session_date = request.form['session_date']
        notes = request.form['notes']
        add_processing_session(session_name, session_date, notes)
        flash('Processing session added successfully!', 'success')
        return redirect(url_for('processing.list_sessions'))
    return render_template('processing/add_session.html')

@processing_bp.route('/sessions/<int:id>/add_output', methods=['GET', 'POST'])
@login_required
def add_output(id):
    if request.method == 'POST':
        product_id = request.form['product_id']
        output_type = request.form['output_type']
        weight = request.form['weight']
        add_processing_output(id, product_id, output_type, weight)
        flash('Processing output added successfully!', 'success')
        return redirect(url_for('processing.view_session', id=id))
    
    products = get_all_products()
    return render_template('processing/add_output.html', session_id=id, products=products)
