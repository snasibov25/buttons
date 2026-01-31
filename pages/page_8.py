from flask import Blueprint, render_template

bp = Blueprint('page_8', __name__)

@bp.route('/8')
def show():
    return render_template('8.html')