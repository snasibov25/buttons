from flask import Blueprint, render_template

bp = Blueprint('page_7', __name__)

@bp.route('/7')
def show():
    return render_template('7.html')