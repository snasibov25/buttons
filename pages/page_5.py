from flask import Blueprint, render_template

bp = Blueprint('page_5', __name__)

@bp.route('/5')
def show():
    return render_template('5.html')