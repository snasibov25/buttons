from flask import Blueprint, render_template

bp = Blueprint('page_13', __name__)

@bp.route('/13')
def show():
    return render_template('13.html')