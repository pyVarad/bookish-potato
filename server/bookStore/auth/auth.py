from flask_restful import Resource
from .models import Books
from flask import Response


class Auth(Resource):
    def get(self):
        resp = Books.objects().to_json()
        return Response(resp)

