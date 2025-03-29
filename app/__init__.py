from flask import Flask
from config import config
from .data.db import DataBaseConnect


def create_app(mode="default"):
    app = Flask(__name__)
    app.config.from_object(config[mode])
    
    app.bd_connect = DataBaseConnect("sqlite:///db/main.sqlite")
    app.bd_connect.create_tables()
    
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
