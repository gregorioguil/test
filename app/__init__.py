from flask import Flask

def initialize(application):
    from app import app
    application.register_blueprint(app, url_prefix='')

def create_app():
    application = Flask(__name__)
    initialize(application)
    return application
