from models.user_model import User
from utils.helpers import hash_password, check_password
from flask_jwt_extended import create_access_token

def register_user(data):
    if User.objects(email=data["email"]).first():
        return {"error": "Email already exists"}, 400

    user = User(
        name=data["name"],
        email=data["email"],
        password=hash_password(data["password"]),
        role=data.get("role", "viewer")
    )
    user.save()

    return {
        "message": f"{user.role.capitalize()} registered successfully",
    }, 201


def login_user(data):
    user = User.objects(email=data["email"]).first()

    if not user:
        return {"error": "User not found"}, 404

    if not check_password(data["password"], user.password):
        return {"error": "Invalid credentials"}, 401

    access_token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role}
    )

    return {
        "message": "Login successful",
        "access_token": access_token
    }, 200