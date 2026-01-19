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

class UserDAO:
    def __init__(self):
        self.users = users

    def getUserByUsername(self, username):
        user = None
        for u in self.users:
            if u.username == username:
                user =  u.__dict__
        return user
    
    def addUser(self, user):
        self.users.append(user)
        return user
    
    def getAllUsers(self):
        return [user.__dict__ for user in self.users]
        # return self.users

# Prova del DAO
user_dao = UserDAO()
response = user_dao.getUserByUsername("jdoe")
print(response)
response = user_dao.getUserByUsername("")
print(response)


app = Flask(__name__)
@app.route('/user', methods=['GET'])
def user():
    resposta=""
    # Paramentres
    username = request.args.get("username",default="")

    # Si els parametres OK
    if username != "":
    # Anar al DAO Server i cercar User per Username
        
        response = user_dao.getUserByUsername(username)
        # respondre amb dades d'usuari trobat
        if response == None:
            resposta = {"msg": "User not found"}
        else:
            resposta = {"username": response['username'], "nom": response['nom'], "password": response['password'], "email": response['email'], "rol": response['rol']}

    else:
        resposta = {"msg": "Falta parametre username"}

    return jsonify(resposta)

@app.route('/getUsers', methods=['GET'])
def users():
    all_users = user_dao.getAllUsers()
    resposta = {"users": all_users}
    return jsonify(resposta)

@app.route('/addUser', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    nom = data.get("nom")
    password = data.get("password")
    email = data.get("email")
    rol = data.get("rol")

    if not all([username, nom, password, email, rol]):
        return jsonify({"msg": "Error: Missing user data"}), 400

    new_user = User(username=username, nom=nom, password=password, email=email, rol=rol)
    user_dao.addUser(new_user)

    return jsonify({"msg": "User added successfully", "user": new_user.__dict__}), 201

if __name__ == '__main__':
    app.run(debug=True)


