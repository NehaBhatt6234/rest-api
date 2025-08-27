from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db
from blocklist import BLOCKLIST
from item import blp as ItemBlueprint
from user import blp as UserBlueprint

def create_app():
    app = Flask(__name__)

    # Config
    app.config["API_TITLE"] = "User Auth + Items API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["JWT_SECRET_KEY"] = "super-secret-key"  # 🔑 move to .env in prod

    db.init_app(app)
    api = Api(app)
    jwt = JWTManager(app)

    # Register blueprints
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(UserBlueprint)

    # JWT callbacks
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return {"message": "Token has been revoked."}, 401

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
