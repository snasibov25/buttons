from flask import Blueprint, render_template

page_42_bp = Blueprint('page_42', __name__)

@page_42_bp.route('/flappy-head')
def show():
    """Flappy Bird controlled by head movements via webcam."""
    return render_template('page_42.html')
