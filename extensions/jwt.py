from flask_jwt_extended import JWTManager

jwt = JWTManager()

def init_jwt(app):
    app.config["JWT_SECRET_KEY"] = "SECRET_KEY_2026"
    jwt.init_app(app)