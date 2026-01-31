from flask import Blueprint, render_template

bp = Blueprint('page_2', __name__)

@bp.route('/2')
def show():
    return render_template('2.html')