import os
import pkgutil
import importlib
import random
from flask import Flask, render_template, redirect, url_for, Blueprint

app = Flask(__name__)

# Dictionary to hold our dynamic page map
# Format: { number: 'blueprint_name.function_name' }
PAGE_DIRECTORY = {}


def register_pages():
    """
    Scans the 'pages' folder.
    Finds files named 'page_X.py'.
    Registers their blueprint and adds them to PAGE_DIRECTORY.
    """
    package_name = 'pages'
    package_path = os.path.join(os.path.dirname(__file__), package_name)

    # Iterates through every file in the 'pages/' folder
    for _, module_name, _ in pkgutil.iter_modules([package_path]):

        # Only process files that start with 'page_' (e.g., page_72.py)
        if module_name.startswith('page_'):
            try:
                # 1. Dynamically import the module
                module = importlib.import_module(
                    f"{package_name}.{module_name}")

                # 2. Find the Blueprint object inside the module
                # We look for any variable that is an instance of flask.Blueprint
                bp = None
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if isinstance(attribute, Blueprint):
                        bp = attribute
                        break

                if bp:
                    # 3. Register the Blueprint
                    app.register_blueprint(bp)

                    # 4. Extract the number from the filename (page_72 -> 72)
                    # We assume the format is strictly 'page_<number>'
                    page_number = int(module_name.split('_')[1])

                    # 5. Add to Directory
                    # We assume the main function in your page file is always named 'show'
                    endpoint = f"{bp.name}.show"
                    PAGE_DIRECTORY[page_number] = endpoint
                    print(f"✅ Loaded Page {page_number} (Endpoint: {endpoint})")

            except Exception as e:
                print(f"❌ Failed to load {module_name}: {e}")


# Run the registration function once on startup
register_pages()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lucky')
def go_to_random():
    if not PAGE_DIRECTORY:
        return "No pages found. Create a file like pages/page_1.py!", 404

    # Pick a random number from the loaded pages
    random_key = random.choice(list(PAGE_DIRECTORY.keys()))
    endpoint = PAGE_DIRECTORY[random_key]

    return redirect(url_for(endpoint))


if __name__ == '__main__':
    app.run(debug=True)