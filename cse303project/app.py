
from flask import Flask
from flask_login import LoginManager
from .config.config import Config
from .database import init_database, test_connection, get_user_by_id
from .routes import auth_bp, main_bp, inventory_bp
from .models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'

    @login_manager.user_loader
    def load_user(user_id):
        user_data = get_user_by_id(user_id)
        if user_data:
            return User(user_data['id'], user_data['username'], user_data['email'], user_data['password_hash'])
        return None

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(inventory_bp, url_prefix='/inventory')

    return app
