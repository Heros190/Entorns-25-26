from flask import Flask, request, jsonify
from ChildDAO import ChildDAO
from UserDAO import UserDAO


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
""" 
@app.route('/childs', methods=['POST'])
def childs():
    data = request.get_json()
    token = data.get("token")

    if not token:
        return jsonify({
            "msg": "Missing token",
            "coderesponse": "0",
            "data": None
        }), 400

    childs = childDao.listChilds(token)

    return jsonify({
        "msg": "Childs retrieved",
        "coderesponse": "1",
        "data": childs
    }), 200
 """
# -------------------------
# RUN SERVER
# -------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)