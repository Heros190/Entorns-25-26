from flask import request, jsonify
from src.dao.user_dao import UserDao
from src.utils.token import generate_token

class AuthService:
    def __init__(self):
        self.user_dao = UserDao()

    def login(self, username, password):
        user = self.user_dao.authenticate_user(username, password)
        if user:
            token = generate_token(user.id)
            return {
                "coderesponse": "1",
                "data": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "token": token,
                    "idrole": user.role
                },
                "msg": "Authenticated"
            }, 200
        else:
            return {
                "coderesponse": "0",
                "msg": "No validat"
            }, 400

    def login_with_token(self, token):
        user = self.user_dao.get_user_by_token(token)
        if user:
            return {
                "coderesponse": "1",
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "token": token,
                "idrole": user.role,
                "msg": "Usuari Ok"
            }, 200
        else:
            return {
                "coderesponse": "0",
                "msg": "No validat"
            }, 400