from flask import Blueprint, render_template

bp = Blueprint('page_1', __name__)

@bp.route('/1')
def show():
    return render_template('1.html')