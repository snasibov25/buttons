from flask import Blueprint, redirect

bp = Blueprint('page_20', __name__)

@bp.route('/go-external')
def show():
    # Flask's redirect function works for external URLs too!
    return redirect("https://bendingspoons.com")