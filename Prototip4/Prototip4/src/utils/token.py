from datetime import datetime, timedelta
import jwt
import os

SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
TOKEN_EXPIRATION_MINUTES = 30

def generate_token(user_id, username):
    expiration = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    token = jwt.encode({'sub': user_id, 'username': username, 'exp': expiration}, SECRET_KEY, algorithm='HS256')
    return token

def validate_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None