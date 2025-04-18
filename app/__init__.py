from flask import Flask
from config import config
from .data.db import DataBaseConnect
from flask_login import LoginManager

from flask_restful import Api
from api.jobs import jobs_resource
from api.users import users_resource


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
    
    
    api = Api(app)
    
    api.add_resource(jobs_resource.JobsListResource, '/api/jobs') 
    api.add_resource(jobs_resource.JobResource, '/api/jobs/<int:job_id>')
    
    api.add_resource(users_resource.UsersListResource, '/api/users') 
    api.add_resource(users_resource.UserResource, '/api/users/<int:user_id>')
    
    
    return app
