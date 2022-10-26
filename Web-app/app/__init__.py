from flask import Flask
from dotenv import dotenv_values

config = dotenv_values("./.env")
app = Flask(__name__)

from app.routes import public_routes
from app.routes import private_routes