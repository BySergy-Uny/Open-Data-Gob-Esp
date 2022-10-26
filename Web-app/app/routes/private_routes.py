from app import app
from flask import redirect, url_for, render_template

@app.route("/profile")
def profile():
    return render_template('profile.html')