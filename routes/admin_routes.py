from flask import Blueprint
from controllers.admin_controller import get_users, update_user, delete_user_controller

admin_bp = Blueprint("admin", __name__, url_prefix="/api/admin")

admin_bp.route("/users", methods=["GET", "OPTIONS"])(get_users)
admin_bp.route("/users/<user_id>", methods=["PATCH", "OPTIONS"])(update_user)
admin_bp.route("/users/<user_id>", methods=["DELETE", "OPTIONS"])(delete_user_controller)