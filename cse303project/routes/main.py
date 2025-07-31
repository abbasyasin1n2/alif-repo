
from flask import Blueprint, render_template
from flask_login import login_required
from ..database import get_user_stats, get_expired_batches, get_soon_to_expire_batches

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    stats = get_user_stats()
    expired_batches = get_expired_batches()
    soon_to_expire_batches = get_soon_to_expire_batches()
    return render_template('dashboard.html', stats=stats, expired_batches=expired_batches, soon_to_expire_batches=soon_to_expire_batches)
