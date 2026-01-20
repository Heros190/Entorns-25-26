from flask import Flask, jsonify, request

class User:
    def __init__(self, username, nom, password, email, rol):
        self.username = username
        self.nom = nom
        self.password = password
        self.email = email
        self.rol = rol

    def __str__(self):
        return (self.nom)
users = [
    User(username= "jdoe", nom="John Doe", password="12345", email="johnD@gmail.com", rol="tutor"),
    User(username= "asmith", nom="Alice Smith", password="password", email="adjkad@adkm", rol= "tutor")
]


'''
app = Flask(__name__)
@app.route('/user', methods=['GET'])
def user():
    resposta=""
    # Paramentres
    username = request.args.get("username",default="")

    # Si els parametres OK
    if username != "":
        
    # Anar al DAO Server i cercar User per Username
    # respondre amb dades d'usuari trobat
        resposta ="username: " + username
    else:
        resposta ="Error: Missing username parameter"
    # Si no OK
    # respondre amb error
    return resposta

if __name__ == '__main__':
    app.run(debug=True)

'''
