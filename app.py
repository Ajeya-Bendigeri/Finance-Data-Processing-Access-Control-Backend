from flask import Flask
from database.db import init_db
from extensions.jwt import init_jwt
from routes.record_routes import records_bp
from routes.dashboard_routes import dashboard_bp
from routes.auth_routes import auth_bp
from flask_cors import CORS
from flask import send_from_directory
from routes.admin_routes import admin_bp


def create_app():
    app = Flask(__name__)

    CORS(
        app,
        resources={r"/*": {"origins": "*"}},
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    )

    init_db()
    init_jwt(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(records_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)

    @app.route("/")
    def serve_frontend():
        return send_from_directory("frontend", "login.html")

    @app.route("/<path:path>")
    def serve_static_files(path):
        return send_from_directory("frontend", path)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)