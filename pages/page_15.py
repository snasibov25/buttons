from flask import Blueprint, render_template

bp = Blueprint('page_15', __name__)

@bp.route('/15')
def show():
    return render_template('hydra.html')