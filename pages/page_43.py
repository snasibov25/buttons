from flask import Blueprint, render_template
import random
from global_land_mask import globe

bp = Blueprint('page_43', __name__)


@bp.route('/random-travel')
def show():
    # Loop forever until we find land
    while True:
        # 1. Generate totally random coordinates
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)

        # 2. Check if it is on land
        # (is_land returns True for continents and islands)
        if globe.is_land(lat, lon):
            # Found one! Break the loop and render.
            return render_template('page_43.html',
                                   lat=round(lat, 5),
                                   lon=round(lon, 5))