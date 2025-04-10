from flask_restful import reqparse


parser_user = reqparse.RequestParser()
parser_user.add_argument("surname", required=True, type=str)
parser_user.add_argument("name", required=True, type=str)
parser_user.add_argument("age", required=True, type=int)
parser_user.add_argument("speciality", required=True, type=str)
parser_user.add_argument("email", required=True, type=str)
parser_user.add_argument("hashed_password", required=True, type=str)
