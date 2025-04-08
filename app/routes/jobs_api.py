from flask import Blueprint, current_app

from ..data.models.jobs import Jobs

from flask import request, abort, jsonify


bp = Blueprint("jobs_api", __name__, url_prefix="/api")


@bp.route("/jobs")
def get_jobs():
    with current_app.db_connect.get_session() as session:
        jobs = session.query(Jobs).all()
    return jsonify(
        {
            "jobs": [
                    item.to_dict(only=tuple(column.name for column in Jobs.__table__.columns))
                    for item in jobs
                ]
        }
    )

@bp.route("/jobs/<int:id>")
def get_job(id):
    with current_app.db_connect.get_session() as session:
        job = session.get(Jobs, id)
    if not job:
        return abort(404)
    return jsonify(
        {
            "job": job.to_dict(only=tuple(column.name for column in Jobs.__table__.columns))
        }
    )

@bp.route("/jobs", methods=["POST"])
def create_job():
    columns = {
        "team_leader": int,
        "job": str,
        "work_size": int,
        "collaborators": str,
        "is_finished": bool
    }
    
    if not request.json:
        abort(400)
    elif not all(key in request.json for key in columns):
        abort(400)
    elif not all(type(request.json[key]) == columns[key] for key in columns):
        abort(400)
    
    with current_app.db_connect.get_session() as session:
        job = Jobs(**request.json)
        session.add(job)
        session.commit()
        
        job_id = job.id
    
    return jsonify({"id": job_id}), 201
