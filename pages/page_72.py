from flask import Blueprint, render_template, request, flash
import google.generativeai as genai
import os

# Define the blueprint
page_72_bp = Blueprint('page_72', __name__)

# --- CONFIGURATION ---
# ideally, put this in an environment variable, but for this demo:
# os.environ["GEMINI_API_KEY"] = "PASTE_YOUR_API_KEY_HERE"
# Or, if you set it in your terminal, we just read it:
API_KEY = "AIzaSyAVrFW0sdblYvBbTxuoRpXkk8BP-KZoPWg"

if API_KEY:
    genai.configure(api_key=API_KEY)


@page_72_bp.route('/startup-generator', methods=['GET', 'POST'])
def show():
    startup_name = None

    # If the user clicked the "Generate" button (POST request)
    if request.method == 'POST':
        if not API_KEY:
            startup_name = "Error: API Key missing. Please set GEMINI_API_KEY."
        else:
            try:
                # 1. Select the model (Flash is fast/free)
                model = genai.GenerativeModel('gemini-2.5-flash')

                # 2. The Prompt
                prompt = "Generate 1 unique, stealthy B2B SaaS AI startup name. No explanations, just the name."

                # 3. Call the API
                response = model.generate_content(prompt)
                startup_name = response.text.strip()

            except Exception as e:
                startup_name = f"API Error: {str(e)}"

    return render_template('page_72.html', result=startup_name)