from flask import request
from services.auth_service import register_user, login_user

def register():
    data = request.get_json()
    return register_user(data)

def login():
    data = request.get_json()
    return login_user(data)