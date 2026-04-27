from flask import Flask, request, jsonify
from ChildDAO import ChildDAO
from UserDAO import UserDAO
from dataclasses import dataclass, asdict

@dataclass
class ApiResponse:
    msg: str
    coderesponse: str
    data: any
app = Flask(__name__)

userDao = UserDAO()
childDao = ChildDAO()


# -------------------------
# LOGIN
# -------------------------
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    identifier = data.get("identifier")
    password = data.get("password")

    if not identifier or not password:
        return jsonify({
            "msg": "Missing parameters",
            "coderesponse": "0",
            "data": None
        }), 400

    user = userDao.login(identifier, password)

    if user:
        # el DAO ya añade token dentro del user
        return jsonify({
            "msg": "Authenticated",
            "coderesponse": "1",
            "data": {
                "id": user.get("id"),
                "username": user.get("username"),
                "token": user.get("token")
            }
        }), 200

    return jsonify({
        "msg": "Not authenticated",
        "coderesponse": "0",
        "data": None
    }), 401


# -------------------------
# CHILDS
# -------------------------

@app.route('/childs', methods=['POST'])
def childs():
    token = request.headers.get("apikeyproven")
    user=None
    if(token):
        #comprovar que el token existeix a un usuari
        user=UserDAO.getUserByToken(token)
    
    if not user:
        response = ApiResponse(
            msg="Acces",
            coderesponse="0"
            data=""
        )
        return jsonify(asdict(response)),400

    data=request.get_json()
    childs=childDao.getChilds(user['id'])
    response = ApiResponse(
        msg="getChilds",
        coderesponse="1"
        data=childs
    )
    return jsonify(asdict(response)),200
    
# -------------------------
# RUN SERVER
# -------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)