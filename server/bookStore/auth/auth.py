import json
import requests
import flask
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token
)
from flask_restful import Resource, reqparse
from .models import Users
from bookStore.config import BookStoreConfig


class Auth(Resource):
    @jwt_required
    def get(self):
        resp = Users.objects().to_json()

        # user = BookStoreConfig.auth.create_user_with_email_and_password(
        #     "fuoexxhpaltcawvext@ttirv.com", "agv12345")
        # print("The user response is " + user)

        return flask.Response(resp)


class SignUpWithEmailAndPassword(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'email', type=str, required=True, location='json'
        )
        self.parser.add_argument(
            'password', type=str, required=True, location='json'
        )
        super(SignInWithEmailAndPassword, self).__init__()


    def verifyEmailAddress(self, user):
        BookStoreConfig.auth.send_email_verification(user['idToken'])
        return "Please check your email to activate."

    def post(self):
        args = self.parser.parse_args()
        email = args.get('email')
        password = args.get('password')

        user = BookStoreConfig.auth.create_user_with_email_and_password(
            email, password
        )
        return "User created successfully."


class ResetPassword(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'email', type=str, required=True, location='json'
        )
        super(SignInWithEmailAndPassword, self).__init__()

    def post(self):
        args = self.parser.parse_args()
        email = args.get('email')
        try:
            BookStoreConfig.auth.send_password_reset_email(email)
        except Exception:
            return "Not a valid email. Please check."

        return "Sent email to reset password successfully"


class SignInWithEmailAndPassword(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'email', type=str, required=True, location='json'
        )
        self.parser.add_argument(
            'password', type=str, required=True, location='json'
        )
        super(SignInWithEmailAndPassword, self).__init__()


    def post(self):
        args = self.parser.parse_args()
        email = args.get('email')
        password = args.get('password')

        try:
            user = BookStoreConfig.auth.sign_in_with_email_and_password(
                email, password
            )
        except requests.HTTPError as e:
            return "Failed to authenticate the user."
            print(e)

        access_token = create_access_token(identity=email)
        # refresh_token = create_refresh_token(identity=email)

        return {
            "accessToken": access_token
        }, 200
