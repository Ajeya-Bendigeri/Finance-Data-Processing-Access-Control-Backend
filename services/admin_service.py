from models.user_model import User
from models.record_model import FinancialRecord
from bson import ObjectId

def get_all_users():
    users = User.objects()

    result = []
    for u in users:
        result.append({
            "id": str(u.id),
            "name": u.name,
            "email": u.email,
            "role": u.role
        })

    return {"users": result}, 200


def update_user_role(user_id, role):
    user = User.objects(id=user_id).first()

    if not user:
        return {"error": "User not found"}, 404

    user.role = role
    user.save()

    return {"message": "Role updated successfully"}, 200


def delete_user(user_id, current_user_id):
    user = User.objects(id=user_id).first()

    if not user:
        return {"error": "User not found"}, 404
    
    if str(user.id) == current_user_id:
        return {"error": "Cannot delete yourself"}, 400
    
    if user.role == "admin":
        return {"error": "Cannot delete admin"}, 400
    
    if str(user.id) == current_user_id:
        return {"error": "Cannot delete yourself"}, 400

    user.delete()

    return {"message": "User deleted successfully"}, 200