
from flask import Blueprint, render_template, request
from flask_login import login_required
from ..database import (
    get_batch_by_id, 
    get_processing_inputs_for_session, 
    get_processing_outputs_for_session, 
    get_product_by_id, 
    get_supplier_by_id,
    get_all_processing_sessions,
    get_all_batches
)

traceability_bp = Blueprint('traceability', __name__, template_folder='templates')

@traceability_bp.route('/traceability', methods=['GET', 'POST'])
@login_required
def traceability_report():
    if request.method == 'POST':
        batch_id = request.form.get('batch_id')
        if batch_id:
            batch = get_batch_by_id(batch_id)
            product = get_product_by_id(batch['product_id'])
            supplier = get_supplier_by_id(product['supplier_id']) if product else None
            
            # Find which processing session this batch was used in
            # This is a simplified approach. A real-world app might need a more complex query.
            all_sessions = get_all_processing_sessions()
            usage = []
            for session in all_sessions:
                inputs = get_processing_inputs_for_session(session['id'])
                for input_batch in inputs:
                    if input_batch['batch_id'] == int(batch_id):
                        outputs = get_processing_outputs_for_session(session['id'])
                        usage.append({'session': session, 'outputs': outputs, 'inputs': inputs})

            batches = get_all_batches()
            return render_template(
                'inventory/traceability_report.html',
                batch=batch,
                product=product,
                supplier=supplier,
                usage=usage,
                batches=batches
            )
    
    batches = get_all_batches()
    return render_template('inventory/traceability_report.html', batches=batches)
