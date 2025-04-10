from flask import current_app

from app.data.models.user import User
from .parsers import parser_user

from flask_restful import Resource, abort


def abort_if_user_not_found(user_id):
    with current_app.db_connect.get_session() as session:
        user = session.get(User, user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        
        with current_app.db_connect.get_session() as session:
            user = session.get(User, user_id)
        
        return {
                "user": user.to_dict(only=tuple(column.name for column in User.__table__.columns))
            }
    
    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        
        with current_app.db_connect.get_session() as session:
            user = session.get(User, user_id)
            session.delete(user)
            session.commit()
        
        return {'success': 'OK'}

class UsersListResource(Resource):
    def get(self):
        with current_app.db_connect.get_session() as session:
            users = session.query(User).all()
        return {
                "users": [
                        item.to_dict(only=tuple(column.name for column in User.__table__.columns))
                        for item in users
                    ]
            }
    
    def post(self):
        args = dict(parser_user.parse_args())
        
        with current_app.db_connect.get_session() as session:
            user = User(**args)
            session.add(user)
            session.commit()
            
            user_id = user.id
        
        return {"id": user_id}, 201
