from flask import Flask
from app.config import Config
# from app.webhook_routes import webhook_blueprint

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Register routes
    # app.register_blueprint(webhook_blueprint, url_prefix="/api")

    return app
