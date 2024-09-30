"""
The flask application package.
"""
import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Configure session and database
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Setup logging
if not app.debug:  # Only enable logging in production mode
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.mkdir('logs')

    # Set up rotating log handler
    file_handler = RotatingFileHandler('logs/flask_app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)  # Set the log level to INFO

    app.logger.addHandler(file_handler)

    # Set the log level for the app
    app.logger.setLevel(logging.INFO)
    app.logger.info('FlaskWebProject startup')

# Import views after the app and logging setup
from FlaskWebProject import views
