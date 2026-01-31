from flask import Blueprint, render_template

bp = Blueprint('page_3', __name__)

@bp.route('/3')
def show():
    return render_template('3.html')