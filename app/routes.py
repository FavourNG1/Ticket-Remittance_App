from flask import Blueprint, render_template

bp = Blueprint('routes', __name__)

@bp.route('/')
def landing_page():
    return render_template('landing.html')

@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
