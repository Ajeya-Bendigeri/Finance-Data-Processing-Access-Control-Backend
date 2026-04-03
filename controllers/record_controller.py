from flask import request
from flask_jwt_extended import get_jwt_identity, get_jwt
from services.record_service import create_record, get_records, update_record, delete_record

def create():
    data = request.get_json()
    user_id = get_jwt_identity()
    role = get_jwt().get("role")
    if role == "viewer":
        return {"error": "Unauthorized"}, 403
    return create_record(data, user_id)


def get_all():
    user_id = get_jwt_identity()
    role = get_jwt().get("role")
    filters = request.args.to_dict()
    user_id = get_jwt_identity()
    return get_records(filters, user_id, role)


def update(record_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    role = get_jwt().get("role")
    if role == "viewer":
        return {"error": "Unauthorized"}, 403
    return update_record(record_id, data, user_id, role)


def delete(record_id):
    user_id = get_jwt_identity()
    role = get_jwt().get("role")
    if role == "viewer":
        return {"error": "Unauthorized"}, 403
    if role != "admin":
        return {"error": "Only admin can delete"}, 403
    return delete_record(record_id, user_id, role)