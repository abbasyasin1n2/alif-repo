
from flask import Blueprint, render_template, jsonify
from flask_login import login_required
from ..database import (
    get_user_stats, 
    get_expired_batches, 
    get_soon_to_expire_batches,
    get_product_counts_by_animal_type,
    get_inventory_over_time
)
import json
from decimal import Decimal

main_bp = Blueprint('main', __name__, template_folder='templates')

def default_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    stats = get_user_stats()
    expired_batches = get_expired_batches()
    soon_to_expire_batches = get_soon_to_expire_batches()

    # Data for Pie Chart
    animal_counts = get_product_counts_by_animal_type()
    pie_chart_data = {
        "labels": [item['animal_type'] for item in animal_counts],
        "series": [item['product_count'] for item in animal_counts]
    }

    # Data for Line Chart
    inventory_data = get_inventory_over_time()
    line_chart_data = {
        "categories": [item['arrival_date'].strftime('%Y-%m-%d') for item in inventory_data],
        "series": [item['total_quantity'] for item in inventory_data]
    }

    return render_template(
        'dashboard.html', 
        stats=stats, 
        expired_batches=expired_batches, 
        soon_to_expire_batches=soon_to_expire_batches,
        pie_chart_data=json.dumps(pie_chart_data),
        line_chart_data=json.dumps(line_chart_data, default=default_serializer)
    )
