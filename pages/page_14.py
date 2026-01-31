from flask import Blueprint, render_template

bp = Blueprint('page_14', __name__)

@bp.route('/14')
def show():
    return render_template('14.html')