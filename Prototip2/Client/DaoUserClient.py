import requests
from User import *
from flask import jsnonify
from client import User

class DaoUserClient:
    base_URL = "http://localhost:5000"  # URL base del WebService

    def login(self,user):
        # validació parametres
        # TO-DO
        # Petició HTTP al WebService per fer login
        URL_peticio = self.base_URL + "/login"
        params_POST = {
            "username": user.username,  # o user.email
            "password": user.password
        }
        response = requests.post(URL_peticio, json=params_POST)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response = user_data_raw['coderesponse']
            if code_response == "0":
                return None
            else: #usuari validat (self, id , username, password, email, idrole, token):
                user=User(user_data_raw['id'], # crear objecte User a partir de la resposta del servidor
                          user_data_raw['username'],
                          user_data_raw['password'],
                          user_data_raw['email'],
                          user_data_raw['idrole'],
                          user_data_raw['token'])
            #retornar objeto User
            return user
        else:
            return None