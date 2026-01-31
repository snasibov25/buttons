# app.py
from flask import Flask, render_template, request, redirect, abort, jsonify
import random
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/random")
def random_page():
    pages = [
        f for f in os.listdir(app.template_folder)
        if f.endswith(".html") and f[:-5].isdigit()
    ]
    n = random.choice(pages)
    return redirect(f"/page/{n[:-5]}")

@app.route("/page/<int:n>")
def page(n):
    template = f"{n}.html"
    if not os.path.exists(os.path.join(app.template_folder, template)):
        abort(404)
    return render_template(template)

@app.route("/action", methods=["POST"])
def action():
    action_type = request.form.get("action")

    if action_type == "baby_name":
        return jsonify(result=random.choice(["Luna", "Noah", "Aria"]))
    elif action_type == "startup":
        return jsonify(result="AI CRM for dentists")
    elif action_type == "counter":
        count = int(request.form.get("count", 0)) + 1
        return jsonify(result=count)

    return jsonify(result="Unknown action")

if __name__ == "__main__":
    app.run(debug=True)
