from flask import Flask
from config import config
from .data.db import DataBaseConnect
from flask_login import LoginManager

from flask import request, abort, jsonify


def create_app(mode="default", db_cone_url="sqlite:///db/main.sqlite"):
    app = Flask(__name__)
    app.config.from_object(config[mode])
    
    app.db_connect = DataBaseConnect(db_cone_url)
    app.db_connect.create_tables()
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    from .data.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        session = app.db_connect.get_session()
        return session.query(User).get(user_id)
    
    from .routes.main import bp
    app.register_blueprint(bp)
    
    from .routes.jobs_api import bp
    app.register_blueprint(bp)
    
    @app.errorhandler(404)
    def not_found(error):
        if request.path.startswith("/api/"):
            return jsonify({"error": "Not found",}), 404
        else:
            return abort(404)
    
    @app.errorhandler(400)
    def bad_request(error):
        if request.path.startswith("/api/"):
            return jsonify({"error": "Not found",}), 400
        else:
            return abort(400)
    
    return app
