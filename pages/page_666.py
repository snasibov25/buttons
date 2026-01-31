from flask import Blueprint, render_template

bp = Blueprint('page_666', __name__)

@bp.route('/do-not-press')
def show():
    return render_template('page_666.html')