from flask import Flask, render_template, redirect, url_for
import random

# Import your page modules
from pages.page_72 import page_72_bp

app = Flask(__name__)

# --- REGISTRATION ---
# Register the blueprints so Flask knows they exist
app.register_blueprint(page_72_bp)

# --- CONFIGURATION ---
# Map a number to the specific FUNCTION name of that page's route.
# Format: { number: 'blueprint_name.function_name' }
PAGE_DIRECTORY = {
    72: 'page_72.show',
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lucky')
def go_to_random():
    """Pick a random number from keys, find the endpoint, and redirect."""
    if not PAGE_DIRECTORY:
        return "No pages configured", 404

    # 1. Pick a random key (e.g., 1 or 2)
    random_key = random.choice(list(PAGE_DIRECTORY.keys()))

    # 2. Get the endpoint name (e.g., 'page_1.show')
    endpoint = PAGE_DIRECTORY[random_key]

    # 3. Redirect to that endpoint
    return redirect(url_for(endpoint))


if __name__ == '__main__':
    app.run(debug=True)