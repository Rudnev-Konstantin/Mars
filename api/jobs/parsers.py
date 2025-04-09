from flask_restful import reqparse


parser_job = reqparse.RequestParser()
parser_job.add_argument("team_leader", required=True, type=int)
parser_job.add_argument("job", required=True, type=str)
parser_job.add_argument("work_size", required=True, type=int)
parser_job.add_argument("collaborators", required=True, type=str)
parser_job.add_argument("is_finished", required=True, type=bool)
