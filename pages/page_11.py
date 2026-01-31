from flask import Blueprint, render_template

bp = Blueprint('page_11', __name__)

@bp.route('/11')
def show():
    return render_template('11.html')