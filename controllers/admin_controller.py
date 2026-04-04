from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity
from services.admin_service import get_all_users, update_user_role, delete_user
from flask import request

def get_users():
    role = get_jwt().get("role")

    if role != "admin":
        return {"error": "Unauthorized"}, 403

    return get_all_users()


def update_user(user_id):
    role = get_jwt().get("role")

    if role != "admin":
        return {"error": "Unauthorized"}, 403

    data = request.get_json()
    new_role = data.get("role")

    if new_role not in ["admin", "analyst", "viewer"]:
        return {"error": "Invalid role"}, 400

    return update_user_role(user_id, new_role)


def delete_user_controller(user_id):
    role = get_jwt().get("role")
    current_user_id = get_jwt_identity()

    if role != "admin":
        return {"error": "Unauthorized"}, 403

    return delete_user(user_id, current_user_id)