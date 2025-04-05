from flask import Flask
from config import config
from .data.db import DataBaseConnect
from flask_login import LoginManager


def create_app(mode="default"):
    app = Flask(__name__)
    app.config.from_object(config[mode])
    
    app.bd_connect = DataBaseConnect("sqlite:///db/main.sqlite")
    app.bd_connect.create_tables()
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    from .data.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        session = app.bd_connect.get_session()
        return session.query(User).get(user_id)
    
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
