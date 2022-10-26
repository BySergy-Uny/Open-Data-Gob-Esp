from app import app
from flask import redirect, url_for, render_template

@app.route("/")
def main():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template('home.html')
