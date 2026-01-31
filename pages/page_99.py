from flask import Blueprint, render_template
import random

bp = Blueprint('page_99', __name__)


@bp.route('/excuse-generator')
def show():
    # We construct the excuse from 3 parts: Intro, Technical Jargon, and The Consequence.
    intros = [
        "I couldn't deploy because",
        "The system crashed when",
        "I'm currently blocked because",
        "The project is delayed because"
    ]

    jargon = [
        "the dorsal docker container",
        "the asynchronous CSS grid",
        "the legacy spaghetti code",
        "the blockchain AI algorithm",
        "the VPN tunnel to the mainframe"
    ]

    consequences = [
        "became sentient and refused to compile.",
        "is stuck in an infinite loop of despair.",
        "migrated to the cloud without permission.",
        "was eaten by a memory leak.",
        "requires a blood sacrifice to debug."
    ]

    # Generate the string in Python
    excuse = f"{random.choice(intros)} {random.choice(jargon)} {random.choice(consequences)}"

    return render_template('page_99.html', excuse=excuse)