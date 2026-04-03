from flask import Blueprint
from controllers.record_controller import create, get_all, update, delete
from middleware.auth_middleware import jwt_required_custom, role_required

records_bp = Blueprint("records", __name__, url_prefix="/api/records")

records_bp.route("/", methods=["POST"])(
    jwt_required_custom(role_required(["admin"])(create))
)

records_bp.route("/", methods=["GET"])(
    jwt_required_custom(get_all)
)

records_bp.route("/<record_id>", methods=["PATCH"])(
    jwt_required_custom(role_required(["admin"])(update))
)

records_bp.route("/<record_id>", methods=["DELETE"])(
    jwt_required_custom(role_required(["admin"])(delete))
)