from flask import Blueprint, render_template, request
import random

bp = Blueprint('page_55', __name__)


@bp.route('/captcha-hell', methods=['GET', 'POST'])
def show():
    # --- IMPOSSIBLE PROMPTS ---
    prompts = [
        "Select all images containing **The concept of Time**",
        "Select all images containing **A sound you can smell**",
        "Select all images containing **Your unfulfilled dreams**",
        "Select all images containing **The number Q**",
        "Select all images containing **A color that doesn't exist**",
        "Select all images containing **Emotional Baggage**",
        "Select all images containing **The Soul**",
        "Select all images containing **Silence**"
    ]

    # --- REJECTION MESSAGES ---
    errors = [
        "Please try again.",
        "Incorrect. Please try again.",
        "You missed a spot.",
        "Robot detected. Try again.",
        "Verification failed.",
        "That's exactly what a robot would click."
    ]

    current_error = None

    # If they clicked "Verify" (POST), we reject them and reload
    if request.method == 'POST':
        current_error = random.choice(errors)

    # Pick a new random prompt
    current_prompt = random.choice(prompts)

    # Generate 9 random seeds for unique images from Picsum
    # We use random seeds so the images are different every time
    image_seeds = [random.randint(1, 10000) for _ in range(9)]

    return render_template('page_55.html',
                           prompt=current_prompt,
                           images=image_seeds,
                           error=current_error)