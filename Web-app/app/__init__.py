from flask import Flask
from dotenv import dotenv_values

config = dotenv_values("./.env")
app = Flask(__name__)

from app.routes import routes