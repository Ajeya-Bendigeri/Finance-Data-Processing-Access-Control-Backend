from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps
from flask import request

def jwt_required_custom(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if request.method == "OPTIONS":
            return {}, 200
        verify_jwt_in_request()
        return fn(*args, **kwargs)
    return wrapper


def role_required(roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if request.method == "OPTIONS":
                return {}, 200

            verify_jwt_in_request()
            claims = get_jwt()

            if claims.get("role") not in roles:
                return {"error": "Forbidden"}, 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator