from flask_jwt_extended import get_jwt_identity, get_jwt
from services.dashboard_service import get_summary, category_breakdown, monthly_trends, recent_transactions

def summary():
    user_id = get_jwt_identity()
    role = get_jwt().get("role")
    return get_summary(user_id, role)

def category():
    user_id = get_jwt_identity()
    role = get_jwt().get("role")
    return category_breakdown(user_id, role)

def trends():
    user_id = get_jwt_identity()
    role = get_jwt().get("role")
    return monthly_trends(user_id, role)

def recent():
    user_id = get_jwt_identity()
    role = get_jwt().get("role")
    return recent_transactions(user_id, role)