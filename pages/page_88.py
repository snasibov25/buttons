from flask import Blueprint, render_template

bp = Blueprint('page_88', __name__)

@bp.route('/time-challenge')
def show():
    return render_template('page_88.html')