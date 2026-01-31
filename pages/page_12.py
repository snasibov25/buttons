from flask import Blueprint, render_template

bp = Blueprint('page_12', __name__)

@bp.route('/12')
def show():
    return render_template('12.html')