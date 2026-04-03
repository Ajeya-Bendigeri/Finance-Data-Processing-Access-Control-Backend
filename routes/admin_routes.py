from flask import Blueprint
from controllers.admin_controller import get_users, update_user, delete_user_controller

admin_bp = Blueprint("admin", __name__, url_prefix="/api/admin")

admin_bp.route("/users", methods=["GET"])(get_users)
admin_bp.route("/users/<user_id>", methods=["PATCH"])(update_user)
admin_bp.route("/users/<user_id>", methods=["DELETE"])(delete_user_controller)