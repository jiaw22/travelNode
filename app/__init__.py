from flask import Flask
from config import Config
from app import routes, models

app = Flask(__name__)
