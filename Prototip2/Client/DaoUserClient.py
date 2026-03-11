import requests
from Child import *
from User import *
from flask import jsonify
#from client import User

class DaoUserClient:
    base_URL = "http://localhost:5000"  # URL base del WebService

    def login(self,user):
        # validació parametres
        # TO-DO
        # Petició HTTP al WebService per fer login
        URL_peticio = self.base_URL + "/login"
        params_POST = {
            "identifier": user.username or user.email,
            "password": user.password
        }
        response = requests.post(URL_peticio, json=params_POST)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response = user_data_raw['coderesponse']
            if code_response == "0":
                return None
            
               
            else: #usuari validat (self, id , username, password, email, idrole, token): 
                user_raw = user_data_raw['data']
                user=User(user_raw['id'], # crear objecte User a partir de la resposta del servidor
                          user_raw['username'],
                          user_raw['password'],
                          user_raw['email'],
                          user_raw['idrole'],
                          user_raw['token'])
            #retornar objeto User
            return user
        else:
            return None
    

    def getChilds(self, user: User):
        payload = {"id_user": user.id}
        r = requests.post(f"{self.base_URL}/child", json=payload)
        if r.status_code == 200:
            res = r.json()
            if res['coderesponse'] == "1":
                childs = []
                for c in res['data']:
                    childs.append(Child(
                        id=c.get('id'),
                        child_name=c.get('child_name'),
                        sleep_average=c.get('sleep_average'),
                        treatment_id=c.get('treatment_id'),
                        time=c.get('time')
                    ))
                return childs
        return []
    
    
#TEST
daoClient=DaoUserClient()
user = User(id="", username="mare", password="12345", email="user1@example.com", idrole=1, token="")
resposta=daoClient.login(user)
print(resposta)