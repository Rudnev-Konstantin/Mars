from flask import current_app

from app.data.models.jobs import Jobs
from .parsers import parser_job

from flask_restful import Resource, abort


def abort_if_job_not_found(job_id):
    with current_app.db_connect.get_session() as session:
        job = session.get(Jobs, job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        
        with current_app.db_connect.get_session() as session:
            job = session.get(Jobs, job_id)
        
        return {
                "job": job.to_dict(only=tuple(column.name for column in Jobs.__table__.columns))
            }
    
    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        
        with current_app.db_connect.get_session() as session:
            job = session.get(Jobs, job_id)
            session.delete(job)
            session.commit()
        
        return {'success': 'OK'}

class JobsListResource(Resource):
    def get(self):
        with current_app.db_connect.get_session() as session:
            jobs = session.query(Jobs).all()
        return {
                "jobs": [
                        item.to_dict(only=tuple(column.name for column in Jobs.__table__.columns))
                        for item in jobs
                    ]
            }
    
    def post(self):
        args = dict(parser_job.parse_args())
        
        with current_app.db_connect.get_session() as session:
            job = Jobs(**args)
            session.add(job)
            session.commit()
            
            job_id = job.id
        
        return {"id": job_id}, 201
