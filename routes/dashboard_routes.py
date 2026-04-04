from flask import Blueprint
from controllers.dashboard_controller import summary, category, trends, recent
from middleware.auth_middleware import jwt_required_custom

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/api/dashboard")

dashboard_bp.route("/summary", methods=["GET", "OPTIONS"])(jwt_required_custom(summary))
dashboard_bp.route("/category", methods=["GET", "OPTIONS"])(jwt_required_custom(category))
dashboard_bp.route("/trends", methods=["GET", "OPTIONS"])(jwt_required_custom(trends))
dashboard_bp.route("/recent", methods=["GET", "OPTIONS"])(jwt_required_custom(recent))