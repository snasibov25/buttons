from flask import Blueprint, render_template

bp = Blueprint('page_4', __name__)

@bp.route('/4')
def show():
    return render_template('4.html')