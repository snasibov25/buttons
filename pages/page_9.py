from flask import Blueprint, render_template

bp = Blueprint('page_9', __name__)

@bp.route('/9')
def show():
    return render_template('9.html')