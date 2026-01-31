from flask import Blueprint, render_template

bp = Blueprint('page_10', __name__)

@bp.route('/10')
def show():
    return render_template('10.html')