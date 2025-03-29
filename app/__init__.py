from flask import Flask
from config import config


def create_app(mode="default"):
    app = Flask(__name__)
    app.config.from_object(config[mode])
    
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
