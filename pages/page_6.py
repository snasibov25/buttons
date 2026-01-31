from flask import Blueprint, render_template

bp = Blueprint('page_6', __name__)

@bp.route('/6')
def show():
    return render_template('6.html')